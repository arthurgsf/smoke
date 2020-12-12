import cv2
import glob

class ImageFile:
    def __init__(self, mat, path):
        self.mat = mat
        self.path = path
        self.features = []

def load_imgs(dir_path):
    img_file_array = []

    for img_path in glob.glob(dir_path):
      	mat = cv2.imread(img_path)
      	img_file_array.append(ImageFile(mat, img_path))
    return img_file_array

# def remove_repeated(lista):
#     att = []

#     for i in lista:
#         if i not in att and (i is not ''):
#             att.append(i)
    
#     return att