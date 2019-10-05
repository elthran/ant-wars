from tunnels import Bitmap

bitmap = Bitmap(width=7, height=5)


def test_from_xy():
    assert bitmap.from_xy(x=3, y=2) == 17


def test_to_xy():
    assert bitmap.to_xy(27) == (3, 6)
