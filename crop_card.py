from datetime import datetime
import timeit
from PIL import Image


IMAGE_PATH = './png/'
BASE_IMG = 'poker_card.png'


card_width = 160
card_high = 225
gap = 4.5
start_x = 90
start_y = 50


def get_card_area(x, y):
    sx = int(start_x + card_width * x + (gap * (x + 1)))
    sy = int(start_y + card_high * y + (gap * (y + 1)))

    ex = sx + card_width
    ey = sy + card_high

    return sx, sy, ex, ey


def each_card_save():
    im = Image.open(IMAGE_PATH + BASE_IMG)

    for j, k in enumerate(('D', 'C', 'H', 'S')):
        for i in range(12):
            area = get_card_area(i, j)
            im2 = im.crop(area)
            im2.save(f"{IMAGE_PATH}{k}{i+2}.png")
            print(f"{k}{i+2} > {area}")
        area = get_card_area(12, j)
        im2 = im.crop(area)
        im2.save(f"{IMAGE_PATH}{k}1.png")
        print(f"{k}1 > {area}")


if __name__ == '__main__':
    st = timeit.default_timer()

    each_card_save()

    process_time = (timeit.default_timer() - st)
    if process_time < 100:
        print(__file__, f"Python Elapsed {process_time:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    elif process_time < 6000:
        print(__file__,
              f"Python Elapsed {process_time / 60:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
    else:
        print(__file__,
              f"Python Elapsed {process_time / 3600:.02f} seconds, current time; {datetime.now().strftime('%H:%M')}")
