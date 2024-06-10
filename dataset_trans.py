import json
import os
from PIL import Image

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2] / 2.0) * dw
    y = (box[1] + box[3] / 2.0) * dh
    w = box[2] * dw
    h = box[3] * dh
    return (x, y, w, h)

def convert_annotations(json_folder, images_folder, output_folder):
    for json_filename in os.listdir(json_folder):
        if json_filename.endswith('.json'):
            json_path = os.path.join(json_folder, json_filename)

            data = None 

            with open(json_path, 'r') as file:
                data = json.load(file)

            base_filename = os.path.splitext(json_filename)[0]
            image_filename = base_filename + '.png'
            image_path = os.path.join(images_folder, image_filename)

            print(image_path)

            if not os.path.exists(image_path):
                img = Image.open(image_path)
                print(type(img))
                continue  # 이미지 파일이 없다면 건너뜀
        
            print(image_path)

            img = Image.open(image_path)
            width, height = img.size

            label_filename = base_filename + '.txt'
            label_path = os.path.join(output_folder, label_filename)

            

            with open(label_path, 'w') as label_file:
                for annotation in data['annotations']:

                    class_id = annotation['category_id'] - 1
                    if class_id == 4:
                        bbox = annotation['bbox']
                        box = convert((width, height), bbox)
                        label_file.write(f"{class_id} {box[0]} {box[1]} {box[2]} {box[3]}\n")
    print("변환 완료")

if __name__ == "__main__":
    
    # 사용 예시
    json_folder = r'C:\Users\User\Desktop\yoloray_modeling\test_data\val\labels'
    images_folder = r'C:\Users\User\Desktop\yoloray_modeling\test_data\val\images'
    output_folder = r'C:\Users\User\Desktop\yoloray_modeling\test_data\val\labels'
    convert_annotations(json_folder, images_folder, output_folder)
