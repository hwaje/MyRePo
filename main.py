import cv2

# 이미지를 읽어옵니다
image = cv2.imread('https://upload.wikimedia.org/wikipedia/ko/thumb/2/24/Lenna.png/440px-Lenna.png')

if image is None:
    print("이미지를 찾을 수 없습니다. 경로를 확인하세요.")
else:
    # 이미지를 창에 표시합니다
    cv2.imshow('Lenna', image)

    # 사용자가 키를 입력할 때까지 대기
    cv2.waitKey(0)

    # 모든 창 닫기
    cv2.destroyAllWindows()