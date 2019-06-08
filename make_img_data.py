import pickle
from datetime import datetime
import timeit
from PIL import Image
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


def save_train_data():
    img_data = list()
    for i, l in enumerate(get_label()):
        im2 = get_gray_image(l)
        for d in ROTATION_DEG:
            img_data.append(((np.array(im2.rotate(d, fillcolor='white'))), i))
            img_data.append(((np.array(im2.rotate(d, fillcolor='gray'))), i))
            if d != 0:
                img_data.append(((np.array(im2.rotate(d, fillcolor='black'))), i))
        print(i, l)
    with open('./png/train.pickle', 'wb') as f:
        pickle.dump(img_data, f, pickle.HIGHEST_PROTOCOL)


def get_gray_image(l):
    im = Image.open(f"{IMAGE_PATH}{l}")
    return im.crop((6, 6, 36, 66)).convert('L')


def load_taine_data():
    with open('./png/train.pickle', 'rb') as f:
        data = pickle.load(f)
        for i in range(5):
            print(data[i])


if __name__ == '__main__':
    st = timeit.default_timer()

    save_train_data()

    load_taine_data()

    process_time = (timeit.default_timer() - st)
    if process_time < 100:
        print(__file__, f"Python Elapsed {process_time:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    elif process_time < 6000:
        print(__file__,
              f"Python Elapsed {process_time / 60:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    else:
        print(__file__,
              f"Python Elapsed {process_time / 3600:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
