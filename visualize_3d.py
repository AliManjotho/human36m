import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from utils import skeleton


SUBJECT = 8
FRAME_INDEX = 190600


sub_data_path = './extracted/subject' + str(SUBJECT) + '_annotations.json'
sub_data_file = open(sub_data_path, 'r')
sub_data = json.loads(sub_data_file.read())


image_file_path = sub_data['annotations'][FRAME_INDEX]['file_name']
w = sub_data['annotations'][FRAME_INDEX]['width']
h = sub_data['annotations'][FRAME_INDEX]['height']
keypoints_3d = sub_data['annotations'][FRAME_INDEX]['keypoints_3d']

img = mpimg.imread('./extracted/' + image_file_path)


x = [joint[0] for joint in keypoints_3d]
y = [joint[1] for joint in keypoints_3d]
z = [joint[2] for joint in keypoints_3d]


fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.imshow(img)

ax = fig.add_subplot(1, 2, 2, projection='3d')

ax.scatter(x, y, z, linewidth=3)

for b in skeleton:
    xs = [keypoints_3d[b[0]][0], keypoints_3d[b[1]][0]]
    ys = [keypoints_3d[b[0]][1], keypoints_3d[b[1]][1]]
    zs = [keypoints_3d[b[0]][2], keypoints_3d[b[1]][2]]
    ax.plot(xs, ys, zs, linewidth=3)

ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
ax.set_xlim(-800, 800)
ax.set_ylim(-800, 800)
ax.set_zlim(0,1600)
ax.set_title('3D Pose plot')
ax.set_xticks([-800, -400, 0, 400, 800])
ax.set_yticks([-800, -400, 0, 400, 800])
ax.set_zticks([0, 400, 800, 1200, 1600])
ax.set_xticklabels('')
ax.set_yticklabels('')
ax.set_zticklabels('')
plt.show()

sub_data_file.close()