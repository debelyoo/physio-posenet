"""
-*- coding: utf-8 -*-
"""
import numpy as np
from .constants import *
import scipy.ndimage as ndi


def build_part_with_score_fast(score_threshold, local_max_radius, scores):
    """
    
    :param score_threshold                  : the minimum score threshold for a pose to be considered
    :param local_max_radius                 : 
    :param scores                           : a heat map of the regions in the image where a pose might be detected
    :return tuple                           : 
    """
    # initialize
    parts = []
    num_keypoints = scores.shape[2]
    lmd = 2 * local_max_radius + 1

    # NOTE it seems faster to iterate over the keypoints and perform maximum_filter
    # on each subarray vs doing the op on the full score array with size=(lmd, lmd, 1)
    for keypoint_id in range(num_keypoints):
        kp_scores = scores[:, :, keypoint_id].copy()
        kp_scores[kp_scores < score_threshold] = 0.
        max_vals = ndi.maximum_filter(kp_scores, size=lmd, mode='constant')
        max_loc = np.logical_and(kp_scores == max_vals, kp_scores > 0)
        max_loc_idx = max_loc.nonzero()
        for y, x in zip(*max_loc_idx):
            parts.append((
                scores[y, x, keypoint_id],
                keypoint_id,
                np.array((y, x))
            ))

    return parts


def within_nms_radius_fast(pose_coords, squared_nms_radius, point):
    """
    
    :param pose_coords: 
    :param squared_nms_radius: 
    :param point: 
    :return: 
    """
    if not pose_coords.shape[0]:
        return False
    return np.any(np.sum((pose_coords - point) ** 2, axis=1) <= squared_nms_radius)


def traverse_to_targ_keypoint(edge_id, source_keypoint, target_keypoint_id, scores, offsets, output_stride,
                              displacements):
    """
    
    :param edge_id: 
    :param source_keypoint: 
    :param target_keypoint_id: 
    :param scores: 
    :param offsets: 
    :param output_stride: 
    :param displacements: 
    :return: 
    """
    height = scores.shape[0]
    width = scores.shape[1]

    source_keypoint_indices = np.clip(
        np.round(source_keypoint / output_stride), a_min=0, a_max=[height - 1, width - 1]).astype(np.int32)

    displaced_point = source_keypoint + displacements[
        source_keypoint_indices[0], source_keypoint_indices[1], edge_id]

    displaced_point_indices = np.clip(
        np.round(displaced_point / output_stride), a_min=0, a_max=[height - 1, width - 1]).astype(np.int32)

    score = scores[displaced_point_indices[0], displaced_point_indices[1], target_keypoint_id]

    image_coord = displaced_point_indices * output_stride + offsets[
        displaced_point_indices[0], displaced_point_indices[1], target_keypoint_id]

    return score, image_coord


def decode_pose(root_score, root_id, root_image_coord, scores, offsets, output_stride, displacements_fwd,
                displacements_bwd):
    """
    
    :param root_score: 
    :param root_id: 
    :param root_image_coord: 
    :param scores: 
    :param offsets: 
    :param output_stride: 
    :param displacements_fwd: 
    :param displacements_bwd: 
    :return: 
    """
    num_parts = scores.shape[2]
    num_edges = len(PARENT_CHILD_TUPLES)

    instance_keypoint_scores = np.zeros(num_parts)
    instance_keypoint_coords = np.zeros((num_parts, 2))
    instance_keypoint_scores[root_id] = root_score
    instance_keypoint_coords[root_id] = root_image_coord

    for edge in reversed(range(num_edges)):
        target_keypoint_id, source_keypoint_id = PARENT_CHILD_TUPLES[edge]
        if (instance_keypoint_scores[source_keypoint_id] > 0.0 and
                    instance_keypoint_scores[target_keypoint_id] == 0.0):
            score, coords = traverse_to_targ_keypoint(
                edge,
                instance_keypoint_coords[source_keypoint_id],
                target_keypoint_id,
                scores, offsets, output_stride, displacements_bwd)
            instance_keypoint_scores[target_keypoint_id] = score
            instance_keypoint_coords[target_keypoint_id] = coords

    for edge in range(num_edges):
        source_keypoint_id, target_keypoint_id = PARENT_CHILD_TUPLES[edge]
        if (instance_keypoint_scores[source_keypoint_id] > 0.0 and
                    instance_keypoint_scores[target_keypoint_id] == 0.0):
            score, coords = traverse_to_targ_keypoint(
                edge,
                instance_keypoint_coords[source_keypoint_id],
                target_keypoint_id,
                scores, offsets, output_stride, displacements_fwd)
            instance_keypoint_scores[target_keypoint_id] = score
            instance_keypoint_coords[target_keypoint_id] = coords

    return instance_keypoint_scores, instance_keypoint_coords


def get_instance_score_fast(exist_pose_coords, squared_nms_radius, keypoint_scores, keypoint_coords):
    """
    
    :param exist_pose_coords: 
    :param squared_nms_radius: 
    :param keypoint_scores: 
    :param keypoint_coords: 
    :return: 
    """
    if exist_pose_coords.shape[0]:
        s = np.sum((exist_pose_coords - keypoint_coords) ** 2, axis=2) > squared_nms_radius
        not_overlapped_scores = np.sum(keypoint_scores[np.all(s, axis=0)])
    else:
        not_overlapped_scores = np.sum(keypoint_scores)
    return not_overlapped_scores / len(keypoint_scores)


def decode_multiple_poses(scores, offsets, displacements_fwd, displacements_bwd, output_stride, max_pose_detections=10,
                          score_threshold=0.5, nms_radius=20, min_pose_score=0.5):
    """
    Takes the posenet model outputs and calculates the score of each pose detected in the image. Also for
    each pose it returns the scores of the key-points and their coordinates.
    
    :param scores                       : a heat map of the regions in the image where a pose might be detected
    :param offsets                      : output from the posenet model
    :param displacements_fwd            : output from the posenet model
    :param displacements_bwd            : output from the posenet model
    :param output_stride                : the stride 
    :param max_pose_detections          : the maximum number of poses to detect
    :param score_threshold              : the minimum score threshold for a pose to be considered
    :param nms_radius                   : 
    :param min_pose_score               : 
    :return tuple                       : 
    """
    # initialize
    pose_count = 0
    pose_scores = np.zeros(max_pose_detections)
    pose_keypoint_scores = np.zeros((max_pose_detections, NUM_KEYPOINTS))
    pose_keypoint_coords = np.zeros((max_pose_detections, NUM_KEYPOINTS, 2))

    squared_nms_radius = nms_radius ** 2

    scored_parts = build_part_with_score_fast(score_threshold, LOCAL_MAXIMUM_RADIUS, scores)
    scored_parts = sorted(scored_parts, key=lambda x: x[0], reverse=True)

    # change dimensions from (h, w, x) to (h, w, x//2, 2) to allow return of complete coord array
    height = scores.shape[0]
    width = scores.shape[1]
    offsets = offsets.reshape(height, width, 2, -1).swapaxes(2, 3)
    displacements_fwd = displacements_fwd.reshape(height, width, 2, -1).swapaxes(2, 3)
    displacements_bwd = displacements_bwd.reshape(height, width, 2, -1).swapaxes(2, 3)

    for root_score, root_id, root_coord in scored_parts:
        root_image_coords = root_coord * output_stride + offsets[
            root_coord[0], root_coord[1], root_id]

        if within_nms_radius_fast(
                pose_keypoint_coords[:pose_count, root_id, :], squared_nms_radius, root_image_coords):
            continue

        keypoint_scores, keypoint_coords = decode_pose(
            root_score, root_id, root_image_coords,
            scores, offsets, output_stride,
            displacements_fwd, displacements_bwd)

        pose_score = get_instance_score_fast(
            pose_keypoint_coords[:pose_count, :, :], squared_nms_radius, keypoint_scores, keypoint_coords)

        # NOTE this isn't in the original implementation, but it appears that by initially ordering by
        # part scores, and having a max # of detections, we can end up populating the returned poses with
        # lower scored poses than if we discard 'bad' ones and continue (higher pose scores can still come later).
        # Set min_pose_score to 0. to revert to original behaviour
        if min_pose_score == 0. or pose_score >= min_pose_score:
            pose_scores[pose_count] = pose_score
            pose_keypoint_scores[pose_count, :] = keypoint_scores
            pose_keypoint_coords[pose_count, :, :] = keypoint_coords
            pose_count += 1

        if pose_count >= max_pose_detections:
            break

    return pose_scores, pose_keypoint_scores, pose_keypoint_coords
