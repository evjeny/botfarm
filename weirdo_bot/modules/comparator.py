"""
Class for comparison images using Structural similarity index
"""

from itertools import combinations
import random

from skimage.measure import structural_similarity as ssim
from skimage.io import imread
from skimage.transform import resize


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


def resize_images_to_one_size(images):
    coefficient = None
    ideal_coefficient = 1
    heights = []
    for image in images:
        image_shape = image.shape
        height: int = image_shape[0]
        width: int = image_shape[1]

        if height == 0 or width == 0:
            return []

        shape_coefficient = height / width
        if not coefficient or abs(ideal_coefficient - shape_coefficient) < abs(ideal_coefficient - coefficient):
            coefficient = shape_coefficient

        heights.append(height)
    middle_height: int = sum(heights) // len(heights)
    middle_width: int = middle_height // coefficient
    res = []
    for image in images:
        image_shape = image.shape
        height: int = image_shape[0]
        width: int = image_shape[1]
        if height / width > coefficient:
            height = int(coefficient * width)
        elif height / width < coefficient:
            width = int(height / coefficient)
        padding_height: int = (image_shape[0] - height) // 2
        padding_width: int = (image_shape[1] - width) // 2

        cropped = image[padding_height:padding_height+height, padding_width:padding_width+width]
        resized = resize(cropped, (middle_height, middle_width))
        res.append(resized)

    return res


def init(vk_api):
    global api

    api = vk_api


def handle(event):
    global api

    if event.object.text == "сравни":

        urls = get_attached_photo_urls(event)
        images = get_images_from_urls(urls)

        if len(images) < 2:
            send_message(api, event, "слишком мало картинок :с")
            return

        images = resize_images_to_one_size(images)
        result = []
        for i_a, i_b in combinations([i for i in range(len(images))], 2):
            val = ssim(images[i_a], images[i_b], multichannel=True) * 100
            val = round(val, 2)
            result.append("картинка {} сходна с картинкой {} на {}%".format(min(i_a, i_b) + 1, max(i_a, i_b) + 1, val))
        res = "\n".join(result)

        send_message(api, event, res)