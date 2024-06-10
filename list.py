import json
import os
import yaml
from collections import defaultdict

def collect_categories(json_folder):
    category_names = set()

    # 폴더 내 모든 JSON 파일 처리
    for filename in os.listdir(json_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(json_folder, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                # 각 파일의 카테고리 이름 추가
                for category in data['categories']:
                    category_names.add(category['name'])

    return list(category_names)

def create_yaml_file(categories, output_file):
    yaml_data = {
        'nc': len(categories),  # 클래스의 수
        'names': sorted(categories)  # 정렬된 클래스 이름 리스트
    }

    # YAML 파일로 저장
    with open(output_file, 'w') as file:
        yaml.dump(yaml_data, file, default_flow_style=False)

# 사용 예시
json_folder = r'C:\Users\User\Desktop\yoloray_modeling\test_data\val\labels'
output_yaml = 'output.yaml'
categories = collect_categories(json_folder)
create_yaml_file(categories, output_yaml)
