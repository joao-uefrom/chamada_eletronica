import io
import mimetypes

import face_recognition
import numpy as np
from PIL import Image


def rgba2rgb(image):
    image_rgb = Image.new('RGB', image.size, (255, 255, 255))
    image_rgb.paste(image, mask=image.getchannel('A'))

    return image_rgb


def binary2image(binary):
    return Image.open(io.BytesIO(binary))


def image2array(image):
    return np.asarray(image)


def image_extension(mimetype: str):
    return mimetypes.guess_extension(mimetype)


def number_of_faces(image):
    face_locations = face_recognition.face_locations(image2array(image))

    return len(face_locations)
