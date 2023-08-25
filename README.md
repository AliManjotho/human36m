# Human3.6M - Dataset processing and visualization
A library for processing and generating readable annotations for Human3.6M dataset.

## Steps
### 1. Extract all dataset files
```
python extract_all.py
```
First put all dataset ZIP files in to directory "compressed". The files will be extracted to folder "extracted"

### 2. Generate annotations
```
python extract_annotations.py
```
The annotations will be generated for each subject as json file in "extracted" folder.


## 3D Pose Visualization
To visualize a pose in 3D
```
python visualize_3d.py
```
![vis3d_1](resources/vis3d_1.png)
![vis3d_1](resources/vis3d_2.png)

## 2D Pose Visualization
<img src="resources/vis2d_1.png" width="300"> <img src="resources/vis2d_2.png" width="367">

