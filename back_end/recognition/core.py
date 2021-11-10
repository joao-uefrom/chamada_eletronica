import filecmp
import os
import pickle
import uuid

import face_recognition
from sklearn import neighbors

from chamada_eletronica.settings import BASE_DIR
from . import utils

train_dir = os.path.join(BASE_DIR, 'static')
model_path = os.path.join(train_dir, 'trained_knn_model.clf')


def add_face(id: str, image_data: bytes, content_type: str):
    extension = utils.image_extension(content_type)

    image = utils.binary2image(image_data)

    face_dir = os.path.join(train_dir, id)

    if not os.path.exists(face_dir):
        os.makedirs(face_dir)

    images_in_dir = os.listdir(face_dir)

    name = str(len(images_in_dir) + 1) + extension
    definitive_image_path = os.path.join(face_dir, name)

    if utils.number_of_faces(image) != 1:
        return

    if len(images_in_dir) > 0:
        temp_name = 'temp-' + str(uuid.uuid4().hex) + extension
        temp_image_path = os.path.join(face_dir, temp_name)

        image.save(temp_image_path)

        for image_in_dir in images_in_dir:
            image_to_compare_path = os.path.join(face_dir, image_in_dir)

            if filecmp.cmp(temp_image_path, image_to_compare_path, shallow=False):
                os.remove(temp_image_path)
                return

        os.rename(temp_image_path, definitive_image_path)

    else:
        image.save(definitive_image_path)


def train():
    x, y = [], []

    classes_dir = [class_dir for class_dir in os.listdir(train_dir) if os.path.isdir(class_dir)]

    for class_id in classes_dir:
        images_path = os.listdir(os.path.join(train_dir, class_id))

        for img_path in images_path:
            image = face_recognition.load_image_file(img_path)
            face_locations = face_recognition.face_locations(image)

            if len(face_locations) == 1:
                x.append(face_recognition.face_encodings(image, known_face_locations=face_locations)[0])
                y.append(class_id)

    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=1, algorithm='ball_tree', weights='distance')
    knn_clf.kneighbors()
    knn_clf.fit(x, y)

    with open(model_path, 'wb') as model:
        pickle.dump(knn_clf, model)


def recognition_face(image_data: bytes):
    image = utils.image2array(utils.binary2image(image_data))
    distance_threshold = 0.5

    with open(model_path, 'rb') as model:
        knn_clf = pickle.load(model)

    x_face_locations = face_recognition.face_locations(image)

    if len(x_face_locations) == 0:
        return []

    faces_encodings = face_recognition.face_encodings(image, known_face_locations=x_face_locations)

    closest_distances = knn_clf.kneighbors(faces_encodings)

    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(x_face_locations))]

    return [
        [pred, loc] if rec else ['Desconhecido', loc]
        for pred, loc, rec in zip(knn_clf.predict(faces_encodings), x_face_locations, are_matches)
    ]


if __name__ == "__main__":
    print("Treinando classificador KNN...")
    train()
    print("Treinamento Completo!")
