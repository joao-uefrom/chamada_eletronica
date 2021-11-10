import io
import mimetypes

import face_recognition
import numpy as np
from PIL import Image


def binary2image(binary):
    return Image.open(io.BytesIO(binary))


def rgba2rgb(image):
    image_rgb = Image.new('RGB', image.size, (255, 255, 255))
    image_rgb.paste(image, mask=image.getchannel('A'))

    return image_rgb


def image2array(image):
    return np.asarray(image)


def image2gray(image):
    return image.convert(mode='L')


def image_extension(content_type: str):
    return mimetypes.guess_extension(content_type)


def number_of_faces(image):
    width, height = image.size

    if width > 450 or height > 450:
        ratio = width / height
        new_size = (int(450 * ratio), 450)
        image = image.resize(new_size)

    face_bounding_boxes = face_recognition.face_locations(image2array(image))

    return len(face_bounding_boxes)
