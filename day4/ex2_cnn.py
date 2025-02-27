# TensorFlow와 기타 필요한 라이브러리 임포트
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# CIFAR-10 데이터셋 불러오기
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# 데이터셋 정규화 (0~1 범위로)
x_train, x_test = x_train / 255.0, x_test / 255.0

# 클래스 이름 정의
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# CNN 모델 설계
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),

    # Flatten and Dense Layers
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# 모델 학습
history = model.fit(x_train, y_train, epochs=10,
                    validation_data=(x_test, y_test))


# 테스트 데이터에서 몇 개를 예측하고 결과 시각화
def plot_sample_predictions(model, x_test, y_test, class_names, num_samples=5):
    plt.figure(figsize=(10, 5))
    indices = np.random.choice(range(len(x_test)), num_samples, replace=False)
    for i, idx in enumerate(indices):
        img, label = x_test[idx], y_test[idx][0]
        pred = model.predict(np.expand_dims(img, axis=0))
        predicted_label = np.argmax(pred)

        plt.subplot(1, num_samples, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(img)
        plt.xlabel(f"Pred: {class_names[predicted_label]}\nTrue: {class_names[label]}")
    plt.tight_layout()
    plt.show()


plot_sample_predictions(model, x_test, y_test, class_names)