import json
import cv2
from utils import skeleton


SUBJECT = 1
FRAME_INDEX = 3501
JOINT_COLOR = (0,255,255)
JOINT_SIZE = 5
BONE_COLOR = (255,0,0)
BONE_SIZE = 3

sub_data_path = './extracted/subject' + str(SUBJECT) + '_annotations.json'
sub_data = open(sub_data_path, 'r')
sub_data = json.loads(sub_data.read())


image_file_path = sub_data['annotations'][FRAME_INDEX]['file_name']
w = sub_data['annotations'][FRAME_INDEX]['width']
h = sub_data['annotations'][FRAME_INDEX]['height']
keypoints_2d = sub_data['annotations'][FRAME_INDEX]['keypoints_2d']


img = cv2.imread('./extracted/' + image_file_path)


for b in skeleton:
    p1 = (int(keypoints_2d[b[0]][0]), int(keypoints_2d[b[0]][1]))
    p2 = (int(keypoints_2d[b[1]][0]), int(keypoints_2d[b[1]][1]))
    cv2.line(img, p1, p2, BONE_COLOR, BONE_SIZE, cv2.LINE_AA)

for kp in keypoints_2d:
    cv2.circle(img, (int(kp[0]), int(kp[1])), JOINT_SIZE, JOINT_COLOR, -1, cv2.LINE_AA)


cv2.imshow('Visualize 2D Joints', img)
cv2.waitKey(0)