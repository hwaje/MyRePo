import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# MNIST 데이터 로드 및 전처리
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 데이터 정규화 (0~255 → 0~1)
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# 라벨 원-핫 인코딩
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# MLP 모델 정의
model = Sequential([
    Flatten(input_shape=(28, 28)),  # MNIST 이미지(28x28)를 1차원 벡터로 변환
    Dense(128, activation='relu'),  # 첫 번째 은닉층
    Dense(64, activation='relu'),  # 두 번째 은닉층
    Dense(10, activation='softmax')  # 출력층 (10개의 클래스)
])

# 모델 컴파일
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 모델 학습
model.fit(
    x_train, y_train,
    validation_split=0.2,  # 20%의 데이터를 검증 세트로 분리
    epochs=10,  # 학습 에포크 수
    batch_size=32,  # 미니배치 크기
    verbose=1  # 학습 로그 출력
)

# 모델 평가
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"테스트 데이터 정확도: {test_acc:.4f}")