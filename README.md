## 포커 카드 인식하기

### 설정 

1. 설치 패키지
    1. pip install jupyter
    1. [numpy-1.16.4+mkl-cp37-cp37m-win_amd64.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)
    1. pip install tensorflow
    1. pip install keras
    1. pip install pillow matplotlib opencv-python
    1. pip install scipy scikit-learn pandas
    1. pip install watermark
        - [watermark](https://github.com/rasbt/watermark#installation-and-updating)
        - 설치된 패키지 버전 확인시 사용
    1. pip install pydot
        - [[Keras] MNIST 데이터 셋을 이용한 필기 글씨에 대한 CNN Tutorial](https://pinkwink.kr/1121?category=580892)

1. [주피터 실행하기](https://dojang.io/mod/page/view.php?id=2457) 
    - 파이참에서 로컬 터미널을 열고 다음을 입력
    - python -m notebook


### 작업순서

* 하나의 카드를 잘라내어 저장하기
    1. 주피터를 이용하여 전체 이미지에서 하나의 카드가 갖는 정보 확인
        - notebook/image_edit.ipynb
    1. TDD 방법론을 이용하여 전체 이미지에서 각 카드가 갖는 위치를 확인
        - tests/test_crop_card.py
    1. 개별이미지 저장을 반복하면서 세부적인 옵셋을 조정하고 이미지 저장
        - crop_card.py
 

## 참고자료

1. 사용이미지
    - [cards1.zip](http://snap2objects.com/downloads/cards1.zip)
        - 다운로드 받은 후 png 로 변환하여 사용함.
1. 이미지 처리
    * [Pillow - 파이썬을 이용한 이미지 처리](https://wikidocs.net/26471)
    * [파이썬으로 이미지 불러오기, 다른이름으로 저장하기](https://classicismist.blogspot.com/2019/03/by-pillow.html)
        * pillow 에서 이미지 보여주기 기능 확인
    * [이미지 처리 기초](https://datascienceschool.net/view-notebook/9af8d8e93c084bc49f0ac2bb8a20e2a4/)
        * 다양한 이미지 처리 라이브러리 설명

1. [[Keras] MNIST 데이터 셋을 이용한 필기 글씨에 대한 CNN Tutorial](https://pinkwink.kr/1121?category=580892)

1. [파이썬 라이브러리를 활용한 머신러닝](http://www.yes24.com/Product/Goods/42806875)
    - [예제 샘플 코드](https://github.com/rickiepark/introduction_to_ml_with_python)    
1. [케라스 창시자에게 배우는 딥러닝](http://www.yes24.com/Product/goods/65050162)
    - [예제 샘플 코드](https://github.com/gilbutITbook/006975)    
