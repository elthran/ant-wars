from random import uniform as rand


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
            row = i*self.height
            s += ''.join(map(str, self[row:row+self.width])) + '\n'
        return s


tunnels = Bitmap(10, 10)
print(tunnels)



def build_tunnels(bitmap, depth=6):
    center = bitmap.width // 2
    bitmap[center] = 1

    rules = {
        0: [
            [rand(0.05, 0.15), 1, rand(0.05, 0.15)],
            [rand(0.03, 0.07), rand(0.03, 0.07), rand(0.03, 0.07)]
        ],
    }

    for i in range(depth):
        row = i*bitmap.height
        b = row + center
        a = b - 1
        c = b + 1
        e = row + bitmap.height + center
        d = e - 1
        f = e + 1
        bitmap[a] = bitmap[a] + rules[0][0][0] % 2
        bitmap[b] = bitmap[b] + rules[0][0][1] % 2
        bitmap[c] = bitmap[c] + rules[0][0][2] % 2
        bitmap[d] = bitmap[d] + rules[0][1][0] % 2
        bitmap[e] = bitmap[e] + rules[0][1][1] % 2
        bitmap[f] = bitmap[f] + rules[0][1][2] % 2


build_tunnels(tunnels)
print(tunnels)
