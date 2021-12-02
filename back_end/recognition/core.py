import os
import pickle

import face_recognition
from sklearn import neighbors

from chamada_eletronica.settings import BASE_DIR
from . import utils

train_dir = os.path.join(BASE_DIR, 'static')
model_path = os.path.join(train_dir, 'trained_knn_model.clf')


def add_face(label: str, image_data: bytes, mimetype: str):
    image = utils.binary2image(image_data)
    extension = utils.image_extension(mimetype)

    if utils.number_of_faces(image) != 1:
        return

    face_dir = os.path.join(train_dir, label)

    if not os.path.exists(face_dir):
        os.makedirs(face_dir)

    number_of_images = len(os.listdir(face_dir))

    name = str(number_of_images + 1) + extension
    definitive_image_path = os.path.join(face_dir, name)

    image.save(definitive_image_path)


def train():
    x, y = [], []

    labels = [label for label in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, label))]

    for label in labels:
        images_path = os.listdir(os.path.join(train_dir, label))

        for img_path in images_path:
            image = face_recognition.load_image_file(os.path.join(train_dir, label, img_path))
            face_locations = face_recognition.face_locations(image)

            if len(face_locations) == 1:
                x.append(face_recognition.face_encodings(image, known_face_locations=face_locations)[0])
                y.append(label)

    if len(labels) > 0:
        with open(model_path, 'wb') as model:
            knn_clf = neighbors.KNeighborsClassifier(n_neighbors=1, algorithm='ball_tree', weights='distance')
            knn_clf.fit(x, y)
            pickle.dump(knn_clf, model)


def recognition_face(image_data: bytes):
    image = utils.image2array(utils.binary2image(image_data))
    distance_threshold = 0.5

    with open(model_path, 'rb') as model:
        knn_clf = pickle.load(model)

    face_locations = face_recognition.face_locations(image)

    if len(face_locations) != 1:
        return None

    faces_encodings = face_recognition.face_encodings(image, known_face_locations=face_locations)

    closest_distance = knn_clf.kneighbors(faces_encodings)[0][0][0]

    are_match = closest_distance <= distance_threshold

    return knn_clf.predict(faces_encodings)[0] if are_match else None
