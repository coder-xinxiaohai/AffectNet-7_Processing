import os
import cv2
import numpy as np

from aligner import FaceAligner
import pickle
from tqdm import tqdm

data_pickle = pickle.load(open('./result/data_affectnet.pkl', 'rb'))
root_dir = './Manually_Annotated/Manually_Annotated_Images'
save_root_dir = './result/aligned_crop_affectnet_imgs'

crop_face = True
aligner = FaceAligner()

for data_type in ['train', 'val']:
    data = data_pickle[data_type]
    for sample in tqdm(data):
        img_name = os.path.join(root_dir, sample.image_path)
        image = cv2.imread(img_name)[..., ::-1]
        image, M = aligner.align(image, sample.left_eye, sample.right_eye)
        if crop_face:
            # Keep only the face region of the image
            face_x = int(sample.face_x)
            face_y = int(sample.face_y)
            face_width = int(sample.face_width)
            face_height = int(sample.face_height)

            point = (face_x, face_y)
            rotated_point = M.dot(np.array(point + (1,)))
            image = image.crop(
                (rotated_point[0], rotated_point[1], rotated_point[0] + face_width, rotated_point[1] + face_height))
        save_path = os.path.join(save_root_dir, sample.image_path.split('/')[0])
        os.makedirs(save_path, exist_ok=True)
        image.save(save_path + '\\' + sample.image_path.split('/')[-1])
