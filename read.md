# Embedded OpenCV Practice

## 소개

임베디드 수업에서 OpenCV를 활용해 이미지 처리와 웹캠 기능을 연습한 실습 저장소입니다.

## 실습 내용

- OpenCV를 이용한 이미지 사이즈 수정
- OpenCV를 이용한 이미지 블러 처리
- 웹캠 실행 및 화면 출력
- Haar Cascade 모델을 활용한 얼굴 인식

## 파일 설명

- `image_resize.py`: 이미지 크기를 변경하는 예제
- `image_blur.py`: 이미지에 블러 효과를 적용하는 예제
- `webcam_read.py`: 웹캠을 실행하고 화면을 출력하는 예제
- `webcam.py`: 웹캠 화면에서 얼굴을 인식하는 예제
- `haarcascade_frontalface_default.xml`: 얼굴 인식에 사용하는 Haar Cascade 모델 파일

## 실행 환경

- Python
- OpenCV

```bash
pip install opencv-python
```

## 실행 예시

```bash
python image_resize.py
python image_blur.py
python webcam_read.py
python webcam.py
```
