import posenet.constants
import numpy as np
import numpy.linalg as la
from math import atan2, degrees

skeleton_ref = {"nose": (0.9962466359138489, 148.35870453, 180.41607903),
            "leftEye": (0.9963536262512207, 139.87018601, 188.4293473),
            "rightEye": (0.986567497253418, 140.1823944,  172.25242458),
            "leftEar": (0.9324114322662354, 141.86653883, 197.118494),
            "rightEar": (0.6488268971443176, 143.261837,   163.75082437),
            "leftShoulder": (0.9953372478485107, 184.10835139, 212.55056701),
            "rightShoulder": (0.4123726189136505, 167.01951437, 157.67663907),
            "leftElbow": (0.9783155918121338, 236.48241832, 226.81994127),
            "rightElbow": (0.8626391887664795, 145.91839257, 104.66117221),
            "leftWrist": (0.9668490886688232, 270.45304043, 248.39246361),
            "rightWrist": (0.4943605661392212, 100.07990276, 135.34512398),
            "leftHip": (0.9124510884284973, 284.11480307, 198.07031853),
            "rightHip": (0.947083055973053, 280.72610375, 159.53378467),
            "leftKnee": (0.9745336771011353, 351.01245897, 210.2366404),
            "rightKnee": (0.9629436731338501, 354.96116947, 161.98790337),
            "leftAnkle": (0.9289294481277466, 402.24599382, 215.34011441),
            "rightAnkle": (0.907148003578186, 411.16178168, 161.20101248)}

skeleton_reading = {"nose": (0.9978408217430115, 178.36749079, 186.77125158),
                    "leftEye": (0.9987517595291138, 170.74162981, 195.73443203),
                    "rightEye": (0.992919921875, 171.44001301, 180.94609174),
                    "leftEar": (0.959613025188446, 173.56771854, 206.18314754),
                    "rightEar": (0.6068293452262878, 172.51799554, 170.43667077),
                    "leftShoulder": (0.9944915771484375, 215.25862299, 220.8995101),
                    "rightShoulder": (0.8322478532791138, 201.43620957, 162.75742485),
                    "leftElbow": (0.9511736631393433, 262.81435612, 242.30142728),
                    "rightElbow": (0.9075787663459778, 175.32676419, 111.39943758),
                    "leftWrist": (0.7705433368682861, 297.4107207,  262.88706836),
                    "rightWrist": (0.5962886214256287, 133.10328049, 143.58476698),
                    "leftHip": (0.8096626996994019, 307.8186492,  207.85400455),
                    "rightHip": (0.966626763343811, 304.90343479, 164.18220157),
                    "leftKnee": (0.7564150094985962, 371.47889373, 229.06661231),
                    "rightKnee": (0.9551177620887756, 378.14329754, 154.89793156),
                    "leftAnkle": (0.6144176721572876, 410.36916435, 220.25930994),
                    "rightAnkle": (0.9289039373397827, 411.08232827, 163.30428101)}


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


for node in posenet.CONNECTED_PART_NAMES:

    reference_part = (skeleton_ref[node[0]], skeleton_ref[node[1]])
    reading_part = (skeleton_reading[node[0]], skeleton_reading[node[1]])

    print("part name: {}".format(node))
    angle_diff = angle_between_matching_parts(reference_part, reading_part)
    print("angle_part_diff: {}".format(angle_diff))