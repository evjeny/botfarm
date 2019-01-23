import os


def remove_ext(file_name):
    return os.path.splitext(file_name)[0]