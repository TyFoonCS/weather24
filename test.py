import os
import random


def get_pics(day):
    if day:
        word = 'd'
    else:
        word = 'n'
    images = os.listdir(path="static/images")
    res = list()
    for image in images:
        if image[0] == word:
            res.append(image)
    res = random.choices(res, k=4)
    return res


print(get_pics(False))
