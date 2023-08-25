import numpy as np
import cv2

skeleton = [
    (0, 1),
    (1, 2),
    (2, 3),
    (0, 4),
    (4, 5),
    (5, 6),
    (0, 7),
    (7, 8),
    (8, 9),
    (9, 10),
    (8, 11),
    (11, 12),
    (12, 13),
    (8, 14),
    (14, 15),
    (15, 16)
]

def Keypoints3Dto2D(points_3d, R, t, f, c, distortion=None):
    
    camera_matrix = [[f[0], 0, c[0]], [0, f[1], c[1]], [0, 0, 1]]
    kp_2d =  cv2.projectPoints(np.array(points_3d).reshape(-1, 3), np.array(R), np.array(t).reshape(-1, 1), np.array(camera_matrix), distortion)
    kp_2d = [[kp[0][0], kp[0][1]] for kp in kp_2d[0]]

    return kp_2d