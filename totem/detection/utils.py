import cv2
import numpy as np


def bgr2rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def bgr2gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def image2bytes(image, extension='.png'):
    _, array = cv2.imencode(extension, image)
    return array.tobytes()


def image2string(image, extension='.jpg'):
    _, array = cv2.imencode(extension, image)
    return array.tostring()


def crop(image: np.ndarray, width=None, height=None, center=False):
    h, w = image.shape[:2]

    if width is None and height is None:
        raise Exception("Forneça uma largura ou altura para cortar a imagem.")

    if center:
        if width is None:
            if height <= h:
                center = int(h / 2)

                i = center - int(height / 2)
                f = center + int(height / 2)

                return np.copy(image[i:f, i:f])

            else:
                raise Exception("A altura não pode ser maior do que a imagem.")

        if height is None:
            if width <= w:
                center = int(w / 2)

                i = center - int(width / 2)
                f = center + int(width / 2)

                return np.copy(image[i:f, i:f])

            else:
                raise Exception("A largura não pode ser maior do que a imagem.")

        if width >= w or height >= h:
            raise Exception("A largura ou altura não pode ser maior do que a imagem.")

        center_h = int(h / 2)
        center_w = int(w / 2)

        ix = center_h - int(height / 2)
        fx = center_h + int(height / 2)

        iy = center_w - int(width / 2)
        fy = center_w + int(width / 2)

        return np.copy(image[ix:fx, iy:fy])

    if width is None:
        if height <= h and height <= w:
            return np.copy(image[0:height, 0:height])
        else:
            raise Exception("A altura não pode ser maior do que as dimensões da imagem.")

    if height is None:
        if width <= w and width <= h:
            return np.copy(image[0:width, 0:width])
        else:
            raise Exception("A largura não pode ser maior do que as dimensões da imagem.")

    if width >= w or height >= h:
        raise Exception("A largura ou altura não pode ser maior do que a imagem.")

    return np.copy(image[0:width, 0:height])


def resize(image: np.ndarray, width=None, height=None, scale=None, interpolation=cv2.INTER_AREA):
    h, w = image.shape[:2]

    if width is None and height is None and scale is None:
        raise Exception("Forneça uma largura, altura ou escala para redimensionar a imagem.")

    if scale is not None:
        if scale > 0:
            return cv2.resize(image, dsize=(0, 0), fx=scale, fy=scale, interpolation=interpolation)
        else:
            raise Exception("Forneça uma escala maior que zero.")

    if width is None:
        ratio = height / float(h)
        dimensions = (int(w * ratio), height)

    elif height is None:
        ratio = width / float(w)
        dimensions = (width, int(h * ratio))

    else:
        dimensions = (width, height)

    return cv2.resize(image, dimensions, interpolation=interpolation)


def video_capture_dimensions(video_capture) -> tuple:
    # height x width
    return video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT), video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)


def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()
