import random


def random_char_challenge(length):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    ret = ''
    for i in range(length):
        ret += random.choice(chars)
    return ret.upper()


def filter_smooth(image, filter_code):
    return image.filter(filter_code)


def noise_dots(draw, image, fill):
    size = image.size
    for p in range(int(size[0] * size[1] * 0.1)):
        draw.point((random.randint(0, size[0]), random.randint(0, size[1])), fill=fill)
    return draw


def noise_arcs(draw, image, fill):
    size = image.size
    draw.arc([-20, -20, size[0], 20], 0, 295, fill=fill)
    draw.line([-20, 20, size[0] + 20, size[1] - 20], fill=fill)
    draw.line([-20, 0, size[0] + 20, size[1]], fill=fill)
    return draw