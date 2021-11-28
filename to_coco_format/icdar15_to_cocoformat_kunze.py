
from pyxllib.data.coco import CocoGtData
from typing import List
from pprint import pprint
import json

# images = CocoGtData.gen_images('/home/datasets/textGroup/ICDAR2015/task4.1Text Localization/ch4_training_images/')
# ann = CocoGtData.gen_annotation(image_id=i, points=bboxes[:, :, j].T, iscrowd=0)

"""
思路：
1、已经生成了图片列表
2、遍历图片列表，
然后取出文件名字，然后打开gt，生成ann
同时将文件信息和gt信息，以及类别信息，
装进去一个label里面
3、遍历结束返回label
"""

train_image_path = '/home/datasets/textGroup/ICDAR2015/task4.1Text Localization/ch4_training_images/'
test_image_path = '/home/datasets/textGroup/ICDAR2015/task4.1Text Localization/ch4_test_images/'

categories_list = ['text']
ann_dir = '/home/datasets/textGroup/ICDAR2015/task4.1Text Localization/ch4_training_localization_transcription_gt/'

train_image_save_path = "/home/datasets/textGroup/ICDAR2015/task4.1Text Localization/train_image_icdar2015_to_coco.json"
test_image_save_path = "/home/datasets/textGroup/ICDAR2015/task4.1Text Localization/test_image_icdar2015_to_coco.json"

def icdar_to_coco(path, categories_list, ann_dir, save_path):
    images = CocoGtData.gen_images(path) #生成图片列表
    categories = CocoGtData.gen_categories(categories_list)  # 生成标签，只有一个文本类
    annotations = []

    for image in images:
        annotation_txt_path = (ann_dir + 'gt_' + image['file_name']).replace('jpg','txt')
        with open(annotation_txt_path) as f:
            for line in f.readlines():
                line = line.strip('\ufeff').strip('\xef\xbb\xbf').strip()
                bboxes = list(map(int, line.split(",")[:8]))
                annotation = CocoGtData.gen_annotation(image_id=image['id'], points=bboxes, iscrowd=0)
                annotations.append(annotation)
    label = CocoGtData.gen_gt_dict(images, annotations, categories,save_path)
    # ori_annotation_file = {
    #     "images": images,
    #     "categories": categories,
    #     "annotations": annotations
    # }
    cgd = CocoGtData(label)
    cgd.reset_box_id(inplace=True)
    return label


# def save_coco_json(save_path, ori_annotation_file):
#     # json_label = json.dumps(ori_annotation_file)
#     with open(save_path,'w') as f:
#         json.dump(ori_annotation_file,f)


labels = icdar_to_coco(train_image_path, categories_list, ann_dir,train_image_save_path)
# save_coco_json(train_image_save_path,ori_annotation_file_list)

# ori_annotation_file_list = icdar_to_coco(test_image_path, categories_list, ann_dir, test_image_save_path)
# save_coco_json(test_image_save_path,ori_annotation_file_list)

