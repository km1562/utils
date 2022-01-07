from pyxllib.data.coco import Coco2Labelme, CocoGtData

path = r"C:\Users\Weng\Desktop\OneDrive - stu.xmut.edu.cn\compute_labor\map_file\AdelaiDet\datasets\totaltext\test_images_labelme"
gt_path = r"C:\Users\Weng\Desktop\OneDrive - stu.xmut.edu.cn\compute_labor\map_file\AdelaiDet\datasets\totaltext\cocoformat.json"
cocogt = CocoGtData(gt_path)
cocogt.to_labelme(path, bbox=False, seg=True).writes()
"""
直接将coco转为labelme
"""