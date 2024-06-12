from ultralytics import YOLO

model = YOLO(r'C:\Users\User\yoloray\model\runs\detect\train13\weights\best.pt')

model.predict(r'C:\Users\User\Desktop\yoloray_data\x-ray_data\images\train\E3S690_20220810_012165_S_Knife-A_022-001_5.png', device='0',save=True,conf=0.5)
