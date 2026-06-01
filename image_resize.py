import cv2

img = cv2.imread('image.jpg')

# 1. 이미지 크기 조절(가로400, 세로300 픽셀로 고정)
resized_img = cv2.resize(img, (400,300))

# 2. 이미지 크기 조절 (비율로 조절 - 0.5배)
resized_ratio = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# 3. 이미지 자르기(Clipped / Crop)
# NumPy 배열 슬라이싱 사용 [y축 시작: y축 끝, x축 시작: x축 끝]

cropped_img = img[100:400, 200:500]

cv2.imshow('Resized', resized_img)
cv2.imshow('ratio', resized_ratio)
cv2.imshow('Cropped', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()