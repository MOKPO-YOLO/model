from ultralytics import YOLO

model = YOLO(r'C:\Users\User\yoloray\model\runs\detect\train36\weights\best.pt')

model.predict(r'C:\Users\User\Desktop\yoloray_modeling\test_data\val\images\E3S690_20221011_02830841_M_Bullet_005-008_Cable_575-063_2.png', device='0',save=True,conf=0.5)
