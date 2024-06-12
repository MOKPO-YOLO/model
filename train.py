from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n.pt") # YOLO 모델 설정
    # 학습 옵션 설정
    # 'freeze': 첫 10개 레이어의 가중치를 고정
    # 'epochs': 전체 학습 횟수
    # 'batch': 배치 크기
    # 'lrf': 최종 학습률 (학습률 감소를 위한 최종 목표값)
    # 'weights': 사용자 정의 초기 가중치 파일 (선택적)
    # 'optimizer': 최적화 알고리즘 선택 (예: 'SGD', 'Adam')
    # 'weight_decay': 가중치 감소 비율 설정
    model.train(data="data.yaml", epochs=30, batch=16, lrf=0.001)