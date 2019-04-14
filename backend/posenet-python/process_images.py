import tensorflow as tf
import cv2
import time
import argparse
import os
from math import atan2, degrees
import pprint
import numpy as np
pp = pprint.PrettyPrinter(depth=4)

import posenet
from posenet.constants import PART_NAMES


parser = argparse.ArgumentParser()
parser.add_argument('--model', type=int, default=101)
parser.add_argument('--scale_factor', type=float, default=1.0)
parser.add_argument('--notxt', action='store_true')
parser.add_argument('--image_dir', type=str, default='./images')
parser.add_argument('--output_dir', type=str, default='./output')
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
    img = np.full((370, 520, 3), 255, dtype=np.uint8)
    out_img = cv2.polylines(img, adjacent_reference_keypoints_list,
                            isClosed=False, color=(255, 255, 0))
    out_img = cv2.polylines(out_img, adjacent_reading_keypoints_list,
                            isClosed=False, color=(255, 0, 0))
    cv2.imshow("skeleton overlay", out_img)

def main():

    with tf.Session() as sess:
        model_cfg, model_outputs = posenet.load_model(args.model, sess)
        output_stride = model_cfg['output_stride']

        if args.output_dir:
            if not os.path.exists(args.output_dir):
                os.makedirs(args.output_dir)

        # filenames = [
        #     f.path for f in os.scandir(args.image_dir) if f.is_file() and f.path.endswith(('.png', '.jpg'))]
        filenames = ["images/Photos/IMG_20190413_203051876.jpg",
                     "images/Photos/IMG_20190413_203052672.jpg" ] #input output
        skeleton_keypoints_list = []

        start = time.time()
        for f in filenames:
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

            if args.output_dir:
                draw_image = posenet.draw_skel_and_kp(
                    draw_image, pose_scores, keypoint_scores, keypoint_coords,
                    min_pose_score=0.25, min_part_score=0.25)

                cv2.imwrite(os.path.join(args.output_dir, os.path.relpath(f, args.image_dir)), draw_image)
                cv2.imshow(f, draw_image)
                #cv2.draw()

            if not args.notxt:
                print()
                print("Results for image: %s" % f)
                for pi in range(len(pose_scores)):
                    if pose_scores[pi] == 0.:
                        break
                    print('Pose #%d, score = %f' % (pi, pose_scores[pi]))
                    key_point_dict = {}
                    for ki, (s, c) in enumerate(zip(keypoint_scores[pi, :], keypoint_coords[pi, :, :])):
                        #print('Keypoint %s, score = %f, coord = %s' % (posenet.PART_NAMES[ki], s, c))
                        #print(posenet.PART_NAMES[ki], s, c)
                        key_point_dict[PART_NAMES[ki]] = (s, c[0], c[1])
                    print(key_point_dict)
                    skeleton_keypoints_list.append(key_point_dict)

        skeleton_matched = compare_skeleton(skeleton_keypoints_list[0],
                                            skeleton_keypoints_list[1])
        draw_overlayed_skeleton(skeleton_keypoints_list[0],
                                skeleton_keypoints_list[1])


        pp.pprint(skeleton_matched)


        print('Average FPS:', len(filenames) / (time.time() - start))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
