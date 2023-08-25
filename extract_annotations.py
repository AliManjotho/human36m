import json
import numpy as np
import cv2
from utils import Keypoints3Dto2D

SUBJECTS = [1, 5, 6, 7, 8, 9, 11]

for SUBJECT in SUBJECTS:

    data_file_path = './extracted/annotations/Human36M_subject' + str(SUBJECT) + '_data.json'
    joint_3d_file_path = './extracted/annotations/Human36M_subject' + str(SUBJECT) + '_joint_3d.json'
    camera_file_path = './extracted/annotations/Human36M_subject' + str(SUBJECT) + '_camera.json'
    output_file_path = './extracted/subject' + str(SUBJECT) + '_annotations.json'

    data_file = open(data_file_path, 'r')
    joint_3d_file = open(joint_3d_file_path, 'r')
    camera_file = open(camera_file_path, 'r')
    output_file = open(output_file_path, 'w')

    data_annots = json.load(data_file)
    joints_3d_annots = json.load(joint_3d_file)
    camera_annots = json.load(camera_file)


    anns = []
    imgs = []
    cams = []

    for a in data_annots['images']:
        d = {}
        d['id'] = a['id']
        d['file_name'] = a['file_name']
        d['width'] = a['width']
        d['height'] = a['height']
        d['subject'] = a['subject']
        d['action_name'] = a['action_name']
        d['action_idx'] = a['action_idx']
        d['subaction_idx'] = a['subaction_idx']
        d['cam_idx'] = a['cam_idx']
        d['frame_idx'] = a['frame_idx']

        d['keypoints_3d'] = joints_3d_annots[str(a['action_idx'])][str(a['subaction_idx'])][str(a['frame_idx'])]

        cam = str(a['cam_idx'])
        d['R'] = camera_annots[cam]['R']
        d['t'] = camera_annots[cam]['t']
        d['c'] = camera_annots[cam]['c']
        d['f'] = camera_annots[cam]['f']
        
        d['keypoints_2d'] = Keypoints3Dto2D(d['keypoints_3d'], d['R'], d['t'], d['f'], d['c'], None)
        
        anns.append(d)
        
    for a in data_annots['annotations']:
        d = {}
        d['image_id'] = a['image_id']
        d['keypoints_vis'] = a['keypoints_vis']
        d['bbox'] = a['bbox']
        
        imgs.append(d)
        
        
    for i in range(0, len(anns)):
        anns[i]['image_id'] = imgs[i]['image_id']
        anns[i]['keypoints_vis'] = imgs[i]['keypoints_vis']
        anns[i]['bbox'] = imgs[i]['bbox']


    json_str = json.dumps({'annotations': anns})
    output_file.write(json_str)


    data_file.close()
    joint_3d_file.close()
    camera_file.close()
    output_file.close()
    
    print('Subject ' + str(SUBJECT) + ' -------- DONE!!!!!')