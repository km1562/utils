import numpy as np
import torch
import torch.nn as nn
from torch.optim import Adam
from shapely.geometry import Point, Polygon
from torch.nn.functional import smooth_l1_loss

torch.device('cpu')

model = nn.Linear(1, 12)
opt = Adam(model.parameters(), lr=0.01)

target_y = torch.Tensor([5])
x = torch.Tensor(np.array([10], dtype='float32'))
y = model(x)
print(y)

# loss = y.sum()
y = y.reshape(-1,2)
coor_tuple = y.split(3)
x, y = coor_tuple
pts1 = Polygon(x)
pts2 = Polygon(y)
intersection = pts1.intersection(pts2).area
union = pts1.union(pts2).area
iou = intersection / union
iou = torch.Tensor([iou])

loss = smooth_l1_loss(iou, target_y)

opt.zero_grad()
loss.backward()
# (y * iou).backward()
opt.step()

print(model(x))