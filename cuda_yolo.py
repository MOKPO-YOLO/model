from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

for i in range(1):
    result = model.predict(r'C:\Users\User\Desktop\yoloray_modeling\test_data\val\images\E3S690_20221011_02830841_M_Bullet_005-008_Cable_575-063_2.png', device='0',save=True,conf=0.5)

plots = result[0].plot()
cv2.imshow('plot',plots)
cv2.waitKey(0)
cv2.destroyAllWindows()
