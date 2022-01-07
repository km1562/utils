from pyxllib.algo.geo import ComputeIou

def nms_basic(boxes, func, iou=0.5, *, key=None, index=False):
    """ 假设boxes已经按权重从大到小排过序

    :param boxes: 支持输入一组box列表 [box1, box2, box3, ...]
    :param key: 将框映射为可计算对象
    :param index: 返回不是原始框，而是对应的下标 [i1, i2, i3, ...]
    """
    # 1 映射到items来操作
    if callable(key):
        items = list(enumerate([key(b) for b in boxes]))
    else:
        items = list(enumerate(boxes))

    # 2 排序并且记录下标,new_idx to ori_index
    operate_boxes = boxes
    sort_boxes = sorted(operate_boxes, key=lambda x: x[1])
    new_index_to_ori_index = {i:box[0] for i, box in enumerate(sort_boxes)}

    # 3 正常nms功能
    idxs = []
    while items:
        # 1 加入权值大的框
        i, b = items[0]
        idxs.append(i)
        # 2 抑制其他框
        left_items = []
        for j in range(1, len(items)):
            if func(b, items[j][1]) < iou:
                left_items.append(items[j])
        items = left_items

    # 4 判断哪些坐标
    ori_box_keep = [new_index_to_ori_index[i] for i in idxs ]

    if index:
        return ori_box_keep
    else:
        return [boxes[i] for i in ori_box_keep]

boxes = [[]]
nms_basic(boxes, ComputeIou.polygon, iou=0.5, keep=True)