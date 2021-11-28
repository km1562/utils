import json
import os
from collections import Counter
from pyxllib.data.labelme import LabelmeDict
from pyxllib.data.coco import CocoData
# if seg:
#     # 把分割也显示出来（用灰色）
#     for features in ann['segmentation']:
#         an = {'box_id': ann['id'], 'xltype': 'seg', 'shape_color': [191, 191, 191]}
#         ori_annotation_file = json.dumps(an, ensure_ascii=False)
#         lmdict['shapes'].append(LabelmeDict.gen_shape(ori_annotation_file, features))
root = r"C:\Users\Weng\Desktop\OneDrive - stu.xmut.edu.cn\compute_labor\map_file\AdelaiDet\output\batext\totaltext\attn_R_50\inference\test_images_labelme"
dt_json_file = r"C:\Users\Weng\Desktop\OneDrive - stu.xmut.edu.cn\compute_labor\map_file\AdelaiDet\output\batext\totaltext\attn_R_50\inference\coco_format_text_result.json"
gt_json_file = r"C:\Users\Weng\Desktop\OneDrive - stu.xmut.edu.cn\compute_labor\map_file\AdelaiDet\datasets\totaltext\test.json"

def draw_labelme_dt(source, gt_json_file, json_file="", label='segmentation'):
    #不如先打开json，然后图片id相同的，把segementation添加进去同一个

    cocodata = CocoData(gt_json_file, dt_json_file)
    for image, annotation in cocodata.group_dt():
        image_file = os.path.join(source, image["file_name"])
        lmdict = LabelmeDict.gen_data(image_file)
        for ann in annotation:
            for seg in ann["segmentation"]:
                lmdict['shapes'].append(LabelmeDict.gen_shape(label, seg))
        with open(image_file.replace(".jpg", ".json"), "w") as f:
            json.dump(lmdict, f)
#
#
#     img_cnt = Counter()
#     # annotation = {}
#     # annotation["segmentation"] = []
#     # segementation_per_image = []
#     with open(json_file, "r") as f:
#         datas = json.load(f)
#     i = 0
#     while i < len(datas):
#         # print(i)
#         # segementation_per_image = []
#         image_id = datas[i]["image_id"]
#         print(image_id)
#         image_file = str(image_id).zfill(7) + ".jpg"
#         image_file = os.path.join(source, image_file)
#         lmdict = LabelmeDict.gen_data(image_file)
#         img_cnt[image_file] += 1
#
#         j = i
#         while j < len(datas):
#
#             if datas[j]["image_id"] == image_id:  #如果image_id相同，就把segmentation添加进来
#                 for values in datas[j]["segmentation"]:
#                     # segementation_per_image.append(values) #这里已经是两层了[[]]了
#                     lmdict['shapes'].append(LabelmeDict.gen_shape(ori_annotation_file, values))
#                 j += 1
#             else:
#                 # annotation["segmentation"].append(segementation_per_image)
#                 # image_file = str(image_id).zfill(7) + ".jpg"
#                 # image_file = os.path.join(source, image_file)
#                 # lmdict = LabelmeDict.gen_data(image_file)  # 生成一张照片
#                 # lmdict['shapes'].append(LabelmeDict.gen_shape(ori_annotation_file, segementation_per_image))
#                 with open(image_file.replace(".jpg", ".json"), "w") as f:
#                     json.dump(lmdict, f)
#                 i = j
#                 break
#
#         if j == len(datas):
#             with open(image_file.replace(".jpg", ".json"), "w") as f:
#                 json.dump(lmdict, f)
#             i = j
#
#     print(img_cnt)
#     # for i in range(len(datas)):
#     #     segementation_per_image = []
#     #     image_id = datas[i]["image_id"]
#     #     for j in range(i,len(datas)):
#     #         if datas[j]["image_id"] == image_id:
#     #             for values in datas[j]["segmentation"]:
#     #                 segementation_per_image.append(values) #这里已经是两层了[[]]了
#     #         else:
#     #             # annotation["segmentation"].append(segementation_per_image)
#     #             image_file = str(image_id).zfill(7)
#     #             image_file = os.path.join(source, image_file) + ".jpg"
#     #             lmdict = LabelmeDict.gen_data(image_file)  # 生成一张照片
#     #             lmdict['shapes'].append(LabelmeDict.gen_shape(ori_annotation_file, segementation_per_image))
#     #             i = j
#     #             break
#
#
# # lmdict = LabelmeDict.gen_data(imfile)
# #
# # #读取str(ori_annotation_file-segementation),然后数值
# #
# # lmdict['shapes'].append(LabelmeDict.gen_shape(ori_annotation_file, features))
draw_labelme_dt(root, gt_json_file, json_file="", label='segmentation')