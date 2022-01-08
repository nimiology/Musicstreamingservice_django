import os
from django.core.exceptions import ValidationError
import random
import string

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView


def slug_generator():
    letters_str = string.ascii_letters + string.digits
    letters = list(letters_str)
    return "".join(random.choice(letters) for _ in range(50))


def Validator(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.wave']
    if not ext.lower() in valid_extensions:
        raise ValidationError('song should be MP3 or WAVE')


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_cover_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{slug_generator()}{ext}"
    return f"{instance.artist}/{final_name}"


class CreateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    pass