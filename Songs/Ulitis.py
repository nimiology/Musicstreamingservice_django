import os
from django.core.exceptions import ValidationError
import random
import string


def slug_genrator():
    letters_str = string.ascii_letters + string.digits
    letters = list(letters_str)
    return "".join(random.choice(letters) for _ in range(101))


def Validator(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.wave']
    if not ext.lower() in valid_extensions:
        raise ValidationError('song should be MP3 or WAVE')


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_album_cover_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.Slug}{ext}"
    return f"singleTrack/cover/{final_name}"


def upload_playlist_cover_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.Slug}{ext}"
    return f"Playlist/cover/{final_name}"


def upload_song_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.Slug}{ext}"
    return f"singleTrack/song/{final_name}"
