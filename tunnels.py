from random import random as rand


class Bitmap:
    def __init__(self, width=10, height=10):
        self._bits = [0] * width * height
        self.width = width
        self.height = height

    def __getitem__(self, key):
        return self._bits[key]

    def __setitem__(self, key, value):
        self._bits[key] = value

    def __len__(self):
        return len(self._bits)

    def __str__(self):
        s = ''
        for i in range(self.height):
            row = i*self.width
            s += ''.join(map(str, self[row:row+self.width])) + '\n'
        return s

    def from_xy(self, x, y):
        return y * self.width + x

    def to_xy(self, n):
        return n // self.width, n % self.width


tunnels = Bitmap(10, 10)
print(tunnels)


def build_tunnels(bitmap, depth=6):
    center = bitmap.width // 2
    bitmap[center] = 1

    rules = {
        0: [
            [round(rand()-0.4), 1, round(rand()-0.4)],
            [round(rand()-0.1), round(rand()-0.1), round(rand()-0.1)]
        ],
    }

    for steps in range(depth):
        for i in range(steps):
            row = i*bitmap.height
            for j in range(bitmap.width):
                b = row + j
                if bitmap[b] == 1:
                    a = b - 1
                    c = b + 1
                    e = row + bitmap.height + j
                    d = e - 1
                    f = e + 1
                    bitmap[a] |= rules[0][0][0]
                    bitmap[b] |= rules[0][0][1]
                    bitmap[c] |= rules[0][0][2]
                    bitmap[d] |= rules[0][1][0]
                    bitmap[e] |= rules[0][1][1]
                    bitmap[f] |= rules[0][1][2]


build_tunnels(tunnels)
print(tunnels)

