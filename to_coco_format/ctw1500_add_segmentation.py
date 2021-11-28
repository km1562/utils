# """
# 思路：
# 用原始的text文件，去生成seg， 然后加到adelaide的json文件上，
# 就是打开照片，然后根据左上角去生成seg，
# 添加进相应的image_Id的annotation
#这个不用，数量对不上

# """
# import os
# import json
#
# ctw_ori_txt_ann_path = "/home/datasets/textGroup/CTW1500/ctw1500/train/text_label_curve/"
# ctw_json_ann_path = "/home/wengkangming/map_file/AdelaiDet/datasets/CTW1500/annotations/train_ctw1500_maxlen160_v2.json"
# ctw_json_ann_add_seg_path = "/home/wengkangming/map_file/AdelaiDet/datasets/CTW1500/annotations/train_ctw1500_maxlen160_v2_add_seg.json"
#
# def ctw_json_add_seg(ctw_ori_txt_ann_path, ctw_json_ann_path, ctw_json_ann_add_seg_path):
#     file = os.walk(ctw_ori_txt_ann_path)
#     with open(ctw_json_ann_path, 'r') as f1:
#         ctw_json_label = json.load(f1)
#         annotations = ctw_json_label["annotations"]
#     i = 0
#     for path, dir_list, file_list in file:
#         file_list.sort()
#         for file_name in file_list:
#             same_iamge_id_anns = {annotation if file_name == annotation["image_id"] for annotation in annotations}
#             txtpath = (os.path.join(path, file_name))
#             with open(txtpath, "r") as f2:
#                 for line in f2.readlines():
#                     line = line.strip('\ufeff').strip('\xef\xbb\xbf').strip()
#                     vals = list(map(int, line.split(',')))  # 得到32个数字
#                     x0, y0 = vals[:2]
#                     segmentation = [((y0 + vals[i]) if i % 2 else (x0 + vals[i])) for i in range(4, 32)]
#                     """
#                     如果image_id跟bbox前两个相同，再添加进去
#                     """
#                     for same_image_id_ann in same_iamge_id_anns:
#                         if x0,y0 == same_image_id_ann["bbox"]:
#
#
#
#         with open(ctw_json_ann_add_seg_path, "w") as f3:
#             json.dump(ctw_json_label, f3)
#         print(i)
#
# if __name__ == "__main__":
#     ctw_json_add_seg(ctw_ori_txt_ann_path, ctw_json_ann_path, ctw_json_ann_add_seg_path)
#

#这个不是数量对不上吗