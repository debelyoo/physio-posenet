"""
-*- coding: utf-8 -*-
"""

import cv2
import numpy as np
from .constants import *


def valid_resolution(width, height, output_stride=16):
    """
    Utility function to check whether the image dimensions are compatible with the stride.
    
    :param int width                                : the width of the image
    :param int height                               : the height of the image
    :param int output_stride                        : the stride
    :return tuple                                   : the compatible witdth and height 
    """
    target_width = (int(width) // output_stride) * output_stride + 1
    target_height = (int(height) // output_stride) * output_stride + 1
    return target_width, target_height


def process_input(source_img, scale_factor=1.0, output_stride=16):
    """
    Utility function to preprocess the image before feeding. The pre-processing
    consists of:
        1. resizing the image to be compatible with the stride
        2. convert it to RGB
        3. scale the values
    
    :param source_img                               : the image to process
    :param int scale_factor                         : the scaling factor of the values
    :param int output_stride                        : the stirde
    :return: 
    """
    target_width, target_height = valid_resolution(source_img.shape[1] * scale_factor,
                                                   source_img.shape[0] * scale_factor,
                                                   output_stride=output_stride)

    scale = np.array([source_img.shape[0] / target_height, source_img.shape[1] / target_width])

    input_img = cv2.resize(source_img, (target_width, target_height), interpolation=cv2.INTER_LINEAR)
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB).astype(np.float32)
    input_img = input_img * (2.0 / 255.0) - 1.0
    input_img = input_img.reshape(1, target_height, target_width, 3)
    return input_img, source_img, scale


def get_adjacent_keypoints(keypoint_scores, keypoint_coords, min_confidence=0.1):
    """
    This function detects whether there is a connection between the detected key points
    in the image. If there is a connection, it saves the inverted coordinates of the
    pair.
    
    :param np.array keypoint_scores                 : the score for each possible key-point
    :param np.array keypoint_coords                 : the coordinates in the image of the key-points
    :param float min_confidence                     : the minimum score threshold for a key-point to be considered
    :return                                         : list of coordinate pairs of the connected key-points
    """
    results = []
    # iterate over the connected pairs indices
    for left, right in CONNECTED_PART_INDICES:
        # if the score of one pair is less than the threshold, skip the pair of key points
        if keypoint_scores[left] < min_confidence or keypoint_scores[right] < min_confidence:
            continue

        # otherwise add the inverted coordinates (for the CV representation)
        results.append(np.array([keypoint_coords[left][::-1], keypoint_coords[right][::-1]]).astype(np.int32))

    return results


def draw_skel_and_kp(img, instance_scores, keypoint_scores, keypoint_coords, min_pose_score=0.5, min_part_score=0.5):
    """
    Utility function to draw the key points and the connections between them

    :param img                      : the image to draw the lines
    :param instance_scores          : the score of a detected pose in the image
    :param keypoint_scores          : the score of a detected key-point in each pose
    :param keypoint_coords          : the coordinates of each detected key-point
    :param min_pose_score           : the minimum score threshold for a pose to be considered
    :param min_part_score           : the minimum score threshold for a key-point to be considered
    :return                         : image with drawn detected key-points and connected parts
    """
    # the resulting image
    out_img = img
    # the detected adjacent key-points
    adjacent_keypoints = []
    # the list of cv.KeyPoint objects
    cv_keypoints = []

    # iterate over the score of each detected pose
    for ii, score in enumerate(instance_scores):
        if score < min_pose_score:
            continue

        # detect connections
        new_keypoints = get_adjacent_keypoints(keypoint_scores[ii, :], keypoint_coords[ii, :, :], min_part_score)
        adjacent_keypoints.extend(new_keypoints)

        # add the key-points in the image
        for ks, kc in zip(keypoint_scores[ii, :], keypoint_coords[ii, :, :]):
            if ks < min_part_score:
                continue
            cv_keypoints.append(cv2.KeyPoint(kc[1], kc[0], 10. * ks))

    # use the key-points we inserted to draw the lines
    out_img = cv2.drawKeypoints(out_img, cv_keypoints, outImage=np.array([]), color=(255, 255, 0),
                                flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    out_img = cv2.polylines(out_img, adjacent_keypoints, isClosed=False, color=(255, 255, 0))
    return out_img
