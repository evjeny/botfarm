from itertools import combinations
import random
import os

import dlib
from scipy.spatial import distance
from skimage.io import imread


def get_face_descriptor(image):
    global shape_predictor, face_recognition, detector

    detected = detector(image, 1)
    for k, d in enumerate(detected):
        shape = shape_predictor(image, d)

        face_descriptor = face_recognition.compute_face_descriptor(image, shape)
        return face_descriptor


def compare(image1, image2):
    face_descriptor1 = get_face_descriptor(image1)
    face_descriptor2 = get_face_descriptor(image2)

    # if face wasn't found
    if not (face_descriptor1 and face_descriptor2):
        return None

    dist = distance.euclidean(face_descriptor1, face_descriptor2)
    return dist


def send_message(vk_api, event, message):
    random_id = random.randint(1, 2 ** 32)
    vk_api.messages.send(
        peer_id=event.object.peer_id,
        message=message,
        random_id=random_id
    )


def get_attached_photo_urls(event):
    attachments = event.object.attachments
    urls = []
    for attach in attachments:
        if attach["type"] == "photo":
            photo = attach["photo"]
            sizes = photo["sizes"]
            for sz in sizes:
                if sz["type"] == "x":
                    urls.append(sz["url"])
                    break
    return urls


def get_images_from_urls(urls):
    images = []
    for url in urls:
        images.append(imread(url))
    return images


def init():
    global shape_predictor, face_recognition, detector

    shape_predictor = dlib.shape_predictor(
        os.path.join(path, "pretrained_models", "shape_predictor_68_face_landmarks.dat")
    )
    face_recognition = dlib.face_recognition_model_v1(
        os.path.join(path, "pretrained_models", "dlib_face_recognition_resnet_model_v1.dat")
    )
    detector = dlib.get_frontal_face_detector()


def handle(event):
    global api, path

    if event.object.text == "сравни лица":
        urls = get_attached_photo_urls(event)
        images = get_images_from_urls(urls)

        if len(images) < 2:
            send_message(api, event, "слишком мало картинок с лицами :с")
            return

        result = []
        for i_a, i_b in combinations([i for i in range(len(images))], 2):
            val = compare(images[i_a], images[i_b])
            if not val:
                continue
            text = ""
            if val < 0.6:
                text = "на картинках {} и {} один и тот же человек".format(min(i_a, i_b) + 1, max(i_a, i_b) + 1)
            else:
                text = "на картинках {} и {} разные люди".format(min(i_a, i_b) + 1, max(i_a, i_b) + 1)
            text += "\nевклидово расстояние: {}\n".format(round(val, 5))
            result.append(text)

        if len(result) < 2:
            send_message(api, event, "слишком мало картинок с лицами :с")
            return

        res = "\n".join(result)

        send_message(api, event, res)

