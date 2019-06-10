import pickle
from datetime import datetime
import timeit
from random import randint

from PIL import Image, ImageOps
import numpy as np

IMAGE_PATH = './png/'
BASE_IMG = 'poker_card.png'
ROTATION_DEG = (-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30)


def get_label():
    label = list()
    for j, k in enumerate(('D', 'C', 'H', 'S')):
        for i in range(12):
            label.append(f"{k}{i + 2:02}.png")
        label.append(f"{k}01.png")
    label.sort()
    return label


def get_gray_image(l):
    im = Image.open(f"{IMAGE_PATH}{l}")
    im2 = im.crop((6, 6, 36, 66)).convert('L')
    return ImageOps.invert(im2)


def get_test_rotation_deg():
    ret = list()
    for _ in range(round(len(ROTATION_DEG)*0.3)):
        ret.append(randint(ROTATION_DEG[0], ROTATION_DEG[-1]))
    return ret


def save_image_data(type_='train'):
    if type_ == 'train':
        deg = ROTATION_DEG
    elif type_ == 'test':
        deg = get_test_rotation_deg()
    else:
        raise Exception(f"type error(train, test); {type_}")

    img_data = list()
    for i, l in enumerate(get_label()):
        print(i, l)
        im2 = get_gray_image(l)
        for d in deg:
            img_data.append(((np.array(im2.rotate(d, fillcolor='white'))), i))
            if d != 0:
                img_data.append(((np.array(im2.rotate(d, fillcolor='gray'))), i))
                img_data.append(((np.array(im2.rotate(d, fillcolor='black'))), i))
    with open(f"./{type_}.pickle", 'wb') as f:
        pickle.dump(img_data, f, pickle.HIGHEST_PROTOCOL)


def load_image_data(type_='train'):
    if type_ not in ('train', 'test'):
        raise Exception(f"type error(train, test); {type_}")

    return pickle.load(open(f"./{type_}.pickle", 'rb'))


def load_train_data():
    train_ = load_image_data('train')
    return [r[0] for r in train_], [r[1] for r in train_]


def load_test_data():
    test_ = load_image_data('test')
    return [r[0] for r in test_], [r[1] for r in test_]


if __name__ == '__main__':
    st = timeit.default_timer()

    # save_image_data('train')
    # save_image_data('test')

    # x_train, y_train = load_train_data()
    # for i in range(2):
    #     print(x_train[i], y_train[i])

    # load_image_data('test')

    process_time = (timeit.default_timer() - st)
    if process_time < 100:
        print(__file__, f"Python Elapsed {process_time:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    elif process_time < 6000:
        print(__file__,
              f"Python Elapsed {process_time / 60:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    else:
        print(__file__,
              f"Python Elapsed {process_time / 3600:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
