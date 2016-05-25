# coding: utf-8
from __future__ import unicode_literals

import requests

from RaPo3.settings import BASE_DIR

UPLOAD_PATH = BASE_DIR + '/static'


def save_image(url, name="default.jpg"):
    try:
        dir_path = '/upload/image/{0}'.format(name)
        save_path = '{0}{1}'.format(UPLOAD_PATH, dir_path)
        response = requests.get(url, stream=True)
        image = response.content
        with open(save_path, "wb") as jpg:
            jpg.write(image)
            return True, '/s{0}'.format(dir_path)
    except IOError:
        print("IO Error\n")
        return False, None
    except Exception, e:
        return False, None
