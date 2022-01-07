import cv2
import os
import json
#from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt
import matplotlib as mpl

# img = cv2.imread("/home/datasets/textGroup/ICDAR2013/Task2.4_End_to_End/ch2_training_images/img_152.jpg")
# #print(img)
# # plt.imshow(img)
# # plt.show()
# # print(mpl.get_backend())

"""coco's annotation"""
# img_root = "/home/datasets/textGroup/ICDAR2013/Task2.4_End_to_End/ch2_training_images/"
# images = []
# categories = []
# annotations = []
# filename = "img_68.jpg"
# img_idx = 1
# ann_idx = 1
#
# categories.append({
#     "id": 1,
#     "name": "text",
#     "supercategory": "text"
# })

"""coco's imgage"""
# #annotation_file = "ch2_training_localizatioin_transcription_gt"
# img_path = img_root + filename
# img = cv2.imread(img_path)
# print(type(img))
# images.append({
#     "file_name": filename,
#     "height": img.shape[0],
#     "id": img_idx,
#     "width": img.shape[1]
# })

icdar_image_path = "/home/datasets/textGroup/ICDAR2013/Task2.4_End_to_End/ch2_training_localizatioin_transcription_gt/"
json_path = "/home/wengkangming/map_file/TextFuse11111-master/icdar2013/"

def icdar2013_to_cocoformat(icdar_image_path, json_path,is_train_gt=True):
    """
    将icadar2013转成coco

    :param icdar_image_path:
    :param json_path:
    :param is_train_gt:
    :return:
    """
    annotations = []
    categories = []
    images = []
    categories.append({
        "id": 1,
        "name": "text",
        "supercategory": "text"
    })
    img_idx = 1
    ann_idx = 1
    for filename in os.listdir(icdar_image_path):
        with open(
                icdar_image_path + "gt_" + filename.replace(
                    ".jpg", ".txt")) as f:
            for line in f.readlines():
                # line.lstrip('\ufeff41')
                # #cordinate = line.split(",")[:8].lstrip('\ufeff41')
                # x1, y1, _, _, x2, y2, _, _ = list(map(int, line.split(",")[:8]))
                line = line.strip('\ufeff').strip('\xef\xbb\xbf').strip()
                x1, y1, _, _, x2, y2, _, _ = list(map(int, line.split(",")[:8]))

                """生成掩码的代码我居然有，而且是调用cv2"""
                # mask = np.zeros(shape=img.shape[:2])
                # mask[y1:y2,x1:x2] = 1
                # contours, hierarchy = cv2.findContours((mask).astype(np.uint8), cv2.RETR_TREE,
                #                                                         cv2.CHAIN_APPROX_SIMPLE)

                # segmentation = []

                # for contour in contours:
                #     contour = contour.flatten().tolist()
                #     # segmentation.append(contour)
                #     if len(contour) > 4:
                #         segmentation.append(contour)

                annotations.append({
                    "area": abs(x2 - x1) * abs(y2 - y1),
                    "bbox": [
                        x1,
                        y1,
                        x2,
                        y2
                    ],
                    "category_id": 1,
                    "id": ann_idx,
                    "image_id": img_idx,
                    "iscrowd": 0,
                    "segmentation":
                        [
                            [
                                x1, y1, x1, y2, x2, y2, x2, y1, x1, y1
                            ]
                        ]
                })
                ann_idx += 1
        img_idx += 1

    # 转为json格式
    data = {
        "images": images,
        "categories": categories,
        "annotations": annotations
    }

    if is_train_gt:
        json.dump(data, open(json_path + "train.json", "w"))
    else:
        json.dump(data, open(json_path + "test.json", "w"))