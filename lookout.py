import sys
from datetime import datetime
import timeit

import numpy as np

from tensorflow.python.keras.models import load_model
from PIL import Image, ImageOps

from make_img_data import get_label


if __name__ == '__main__':
    st = timeit.default_timer()

    try:
        im = Image.open(sys.argv[1])
    except:
        print(f"Using python lookout card.png")
        exit(1)

    im2 = im.crop((6, 6, 36, 66))
    im5 = im2.convert('L')
    im6 = ImageOps.invert(im5)
    img_arr = np.array(im6)
    x_arr = img_arr.reshape(1, 30 * 60)

    model = load_model('model_poker_card.h5')
    idx = model.predict_classes(x_arr)[0]

    lables = get_label()
    print('=' * 30)
    print(f"Predict Card : {lables[idx]}")
    print('=' * 30)

    process_time = (timeit.default_timer() - st)
    if process_time < 100:
        print(__file__, f"Python Elapsed {process_time:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    elif process_time < 6000:
        print(__file__,
              f"Python Elapsed {process_time / 60:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    else:
        print(__file__,
              f"Python Elapsed {process_time / 3600:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
