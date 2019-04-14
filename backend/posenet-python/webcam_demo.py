import tensorflow as tf
import cv2
import time
import argparse
from posenet.constants import PART_NAMES
from math import atan2, degrees, pi
import pprint
pp = pprint.PrettyPrinter(depth=4)
import numpy as np

import posenet

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=int, default=101)
parser.add_argument('--cam_id', type=int, default=0)
parser.add_argument('--cam_width', type=int, default=1280)
parser.add_argument('--cam_height', type=int, default=720)
parser.add_argument('--scale_factor', type=float, default=1.0)
args = parser.parse_args()

def angle_between_matching_parts(reference_part, reading_part):
    """ get angle between reference part and reading part
        returns angle difference between reference and reading part"""

    # calculate angle of part inclination
    part_ref_angle = atan2(abs(reference_part[0][2] - reference_part[1][2]),
                           abs(reference_part[0][1] - reference_part[1][1]))

    part_read_angle = atan2(abs(reading_part[0][2] - reading_part[1][2]),
                            abs(reading_part[0][1] - reading_part[1][1]))

    angle_diff = part_ref_angle - part_read_angle
    return angle_diff


def compare_skeleton(skeleton_reference, skeleton_reading):
    """ iterate over all body parts and check the angle differences
        between reference and reading parts """
    skeleton_matched = {}
    for body_part in posenet.CONNECTED_PART_NAMES:
        reference_part = (skeleton_reference[body_part[0]], skeleton_reference[body_part[1]])
        reading_part = (skeleton_reading[body_part[0]], skeleton_reading[body_part[1]])
        angle_diff = angle_between_matching_parts(reference_part, reading_part)

        reading_part_score_0 = skeleton_reading[body_part[0]][0]
        reading_part_score_1 = skeleton_reading[body_part[1]][0]
        min_score = 0.5
        if (reading_part_score_0 < min_score) and (reading_part_score_1 < min_score):
            skeleton_matched[body_part] = 999
        else:
            skeleton_matched[body_part] = degrees(angle_diff)
    return skeleton_matched


def draw_overlayed_skeleton(skeleton_reference, skeleton_reading):
    adjacent_reference_keypoints_list = []
    adjacent_reading_keypoints_list = []
    for body_part in posenet.CONNECTED_PART_NAMES:
        reference_part = [list(skeleton_reference[body_part[0]])[::-1][0:2],
                          list(skeleton_reference[body_part[1]])[::-1][0:2]]
        reading_part = [list(skeleton_reading[body_part[0]])[::-1][0:2],
                        list(skeleton_reading[body_part[1]])[::-1][0:2]]
        adjacent_reference_keypoints_list.append(np.array(reference_part,
                                                          np.int32))
        adjacent_reading_keypoints_list.append(np.array(reading_part,
                                                        np.int32))
    img = np.full((480, 360, 3), 255, dtype=np.uint8)
    out_img = cv2.polylines(img, adjacent_reference_keypoints_list,
                            isClosed=False, color=(255, 255, 0))
    out_img = cv2.polylines(out_img, adjacent_reading_keypoints_list,
                            isClosed=False, color=(255, 0, 0))
    cv2.imshow("skeleton overlay", out_img)

def main():

    ref_key_point_dict = {}
    good_counter = 0

    with tf.Session() as sess:
        model_cfg, model_outputs = posenet.load_model(args.model, sess)
        output_stride = model_cfg['output_stride']

        # cap = cv2.VideoCapture("images/TestVideo.mp4")
        cap = cv2.VideoCapture(0)
        cap.set(3, args.cam_width)
        cap.set(4, args.cam_height)

        start = time.time()
        frame_count = 0

        #Loading ref file
        f = "images/Shoulder/Shoulder_exercise_good3.jpg"
        input_image, draw_image, output_scale = posenet.read_imgfile(
            f, scale_factor=args.scale_factor, output_stride=output_stride)

        heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = sess.run(
            model_outputs,
            feed_dict={'image:0': input_image}
        )

        pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multiple_poses(
            heatmaps_result.squeeze(axis=0),
            offsets_result.squeeze(axis=0),
            displacement_fwd_result.squeeze(axis=0),
            displacement_bwd_result.squeeze(axis=0),
            output_stride=output_stride,
            max_pose_detections=10,
            min_pose_score=0.25)


        keypoint_coords *= output_scale

        for pi in range(len(pose_scores)):
            if pose_scores[pi] == 0.:
                break
            print('Pose #%d, score = %f' % (pi, pose_scores[pi]))
            key_point_dict = {}
            for ki, (s, c) in enumerate(zip(keypoint_scores[pi, :], keypoint_coords[pi, :, :])):
                key_point_dict[PART_NAMES[ki]] = (s, c[0], c[1])
            print(key_point_dict)
            ref_key_point_dict = key_point_dict


        while True:
            input_image, display_image, output_scale = posenet.read_cap(
                cap, scale_factor=args.scale_factor, output_stride=output_stride)

            heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = sess.run(
                model_outputs,
                feed_dict={'image:0': input_image}
            )

            pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multi.decode_multiple_poses(
                heatmaps_result.squeeze(axis=0),
                offsets_result.squeeze(axis=0),
                displacement_fwd_result.squeeze(axis=0),
                displacement_bwd_result.squeeze(axis=0),
                output_stride=output_stride,
                max_pose_detections=10,
                min_pose_score=0.15)

            keypoint_coords *= output_scale

            # TODO this isn't particularly fast, use GL for drawing and display someday...
            overlay_image = posenet.draw_skel_and_kp(
                display_image, pose_scores, keypoint_scores, keypoint_coords,
                min_pose_score=0.15, min_part_score=0.1)

            for pi in range(len(pose_scores)):
                if pose_scores[pi] == 0.:
                    break
                print('Pose #%d, score = %f' % (pi, pose_scores[pi]))
                key_point_dict = {}
                for ki, (s, c) in enumerate(zip(keypoint_scores[pi, :], keypoint_coords[pi, :, :])):
                    key_point_dict[PART_NAMES[ki]] = (s, c[0], c[1])

            skeleton_matched = compare_skeleton(ref_key_point_dict,
                                                key_point_dict)
            draw_overlayed_skeleton(ref_key_point_dict,
                                    key_point_dict)
            pp.pprint(skeleton_matched)
            pp.pprint(skeleton_matched[('rightElbow', 'rightShoulder')])
            if (abs(skeleton_matched[('rightElbow',
                                      'rightShoulder')]) < 20.0) and \
               (abs(skeleton_matched[('rightElbow',
                                      'rightWrist')]) < 20.0):
                good_counter = good_counter + 1
            elif abs(skeleton_matched[('leftElbow', 'leftShoulder')]) == 999:
                print("SKELETON NOT FOUND")
                good_counter = 0
            else:
                print("WRONG!!!")
                good_counter = 0

            if good_counter > 5:
                print("GOOD!!!")
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,300)
                fontScale              = 1
                fontColor              = (0,255,0)
                lineType               = 2

                cv2.putText(overlay_image,'GOOD!',
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    lineType)
            else:
                print("BAD!!!")
                # font                   = cv2.FONT_HERSHEY_SIMPLEX
                # bottomLeftCornerOfText = (10,300)
                # fontScale              = 1
                # fontColor              = (0,0,255)
                # lineType               = 2
                #
                # cv2.putText(overlay_image,'BAD!',
                #     bottomLeftCornerOfText,
                #     font,
                #     fontScale,
                #     fontColor,
                #     lineType)

            cv2.imshow('posenet', overlay_image)
            frame_count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        print('Average FPS: ', frame_count / (time.time() - start))


if __name__ == "__main__":
    main()
