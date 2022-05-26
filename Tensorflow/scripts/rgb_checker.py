from scipy.misc import imread, imsave, imresize
from PIL import Image
import glob
import os
WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
APIMODEL_PATH = 'Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'

# for img in glob.glob("Tensorflow/workspace/images/train/*.jpg"):
#     image = imread(img)
#     if(len(image.shape) < 3):
#         print('gray')
#         # print(image)
#         # print(os.path.dirname(os.path.abspath(__file__)))
#         # print(__file__)
#         x = Image.open(img)
#         # print(os.path.basename('image'))
#         print(x.filename)
#     elif len(image.shape) == 3:
#         print('Color(RGB)')
#     else:
#         print('others')

path = 'Tensorflow/workspace/images/train/'
for file in os.listdir(path):
    extension = file.split('.')[-1]
    if extension == 'jpg':
        fileLoc = path+file
        img = Image.open(fileLoc)
        if img.mode != 'RGB':
            print(file+', '+img.mode)
# image = imread('Tensorflow/workspace/images/train/No Mask45.jpg')
# if(len(image.shape) < 3):
#     print('gray')
# elif len(image.shape) == 3:
#     print('Color(RGB)')
# else:
#     print('others')
