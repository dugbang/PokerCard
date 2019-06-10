## 포커 카드 인식하기

### 설정 

1. 설치 패키지
    1. pip install jupyter
    1. [numpy-1.16.4+mkl-cp37-cp37m-win_amd64.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)
    1. pip install tensorflow
    1. pip install pillow matplotlib opencv-python
    1. pip install watermark
        - [watermark](https://github.com/rasbt/watermark#installation-and-updating)
        - 설치된 패키지 버전 확인시 사용

1. [주피터 실행하기](https://dojang.io/mod/page/view.php?id=2457) 
    - 파이참에서 로컬 터미널을 열고 다음을 입력
    - python -m notebook


### 작업순서 및 파일 설명

1. 기준이 되는 이미지 저장하기
    1. 주피터를 이용하여 전체 이미지에서 하나의 카드가 갖는 정보 확인
        - notebook/image_edit.ipynb
    1. TDD 방법론을 이용하여 전체 이미지에서 각 카드가 갖는 위치를 확인
        - tests/test_crop_card.py
    1. 개별이미지 저장을 반복하면서 세부적인 옵셋을 조정하고 이미지 저장
        - **crop_card.py**
1.  신경망 입력 데이터 생성하기
    1. 기준이 되는 이미지를 읽어들어 학습데이터 및 테스트 데이터 생성 연습
        - notebook/make_ing_data.ipynb
        - notebook/image_invert.ipynb
    1. 위에서 연습한 것을 파이썬 파일에 정리
        - **make_img_data.py**
1. 신경망 모델 학습 및 활용하기
    1. 입력데이터 가공 및 모델 학습 방법 연습
        - notebook/model_learn.ipynb
    1. 위에서 연습한 것을 파이썬 파일에 정리
        - **model_learn.py**
    1. 저장된 모델 정보를 이용하여 실제 사용하는 방법 연습
        - notebook/using_model.ipynb
1. 기타파일
    * 참고자료의 예제를 연습하면서 만든 파일
        - notebook/mnist_cnn.ipynb
        - notebook/mnist_normal.ipynb 
        - notebook/mnist_normal2.ipynb


## 참고자료

1. 사용이미지
    - [cards1.zip](http://snap2objects.com/downloads/cards1.zip)
        - 다운로드 받은 후 png 로 변환하여 사용함.
        - ./png/poker_card.png
1. 이미지 처리
    * [Pillow - 파이썬을 이용한 이미지 처리](https://wikidocs.net/26471)
    * [파이썬으로 이미지 불러오기, 다른이름으로 저장하기](https://classicismist.blogspot.com/2019/03/by-pillow.html)
        * pillow 에서 이미지 보여주기 기능 확인
    * [이미지 처리 기초](https://datascienceschool.net/view-notebook/9af8d8e93c084bc49f0ac2bb8a20e2a4/)
        * 다양한 이미지 처리 라이브러리 설명
    * [파이썬에서 image를 처리합시다.](https://frhyme.github.io/python-lib/img_preprocessing/)
        * 이미지 파일 읽고 잘라내는 방법 등
    * [파이썬 이미지 처리](http://pythonstudy.xyz/python/article/406-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%B2%98%EB%A6%AC)
        * 잘라내기, 회전 및 리사이징 등
1. 신경망 학습
    * [[Keras] MNIST 데이터 셋을 이용한 필기 글씨에 대한 CNN Tutorial](https://pinkwink.kr/1121?category=580892)
    * [케라스 강좌 내용](https://tykimos.github.io/lecture/)
    * [tf.keras - 4. MNIST (Korean)](https://youtu.be/QqmugTjVbz4)
        * [tf.keras/2. MNIST.ipynb](https://github.com/jkh911208/tf.keras/blob/master/2.%20MNIST.ipynb)

