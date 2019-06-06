from unittest import TestCase

card_width = 160
card_high = 225
gap = 5
start_x = 90
start_y = 50


def get_card_area(x, y):
    sx = start_x + card_width * x + (gap * (x + 1))
    sy = start_y + card_high * y + (gap * (y + 1))

    ex = sx + card_width
    ey = sy + card_high

    return sx, sy, ex, ey


class TestCardArea(TestCase):
    def setUp(self):
        pass

    def test_pos_0_1(self):
        self.assertEqual((95, 285, 255, 510), get_card_area(0, 1))

    def test_pos_2_0(self):
        self.assertEqual((425, 55, 585, 280), get_card_area(2, 0))

    def test_pos_1_0(self):
        self.assertEqual((260, 55, 420, 280), get_card_area(1, 0))

    def test_pos_0_0(self):
        self.assertEqual((95, 55, 255, 280), get_card_area(0, 0))
