from django.http import JsonResponse
# from PIL import Image


VALID_FILE_EXTENSIONS = [
    ".pdf",
    ".docs",
    ".docx",
    ".xlsx",
    ".xls",
    ".ppt",
    ".pptx",
    ".jpg",
    ".jpeg",
    ".png",
    ".xlsm",
    ".txt"

]
import os.path
import random
import string
from os import path
from time import gmtime, strftime
import time
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def handle_uploaded_file(file):

    extension = ""
    for e in VALID_FILE_EXTENSIONS:
        if file.name.endswith(e):
            extension = e
            break
    if extension == "":
        raise Exception('ErrorFileType')
        
    if not path.exists(f"uploads/{extension[1:]}"):
        os.mkdir(f"uploads/{extension[1:]}")
    

    result = "".join(strftime(f"%d%b%Y_%H-%M-%S {time.time()}", gmtime()))
    directory = f"upload/{extension[1:]}/{result}.{extension[1:]}"
    try:
        pathh = default_storage.save(directory, ContentFile(file.read()))
        # file.save(directory)
    except Exception as x:
        raise Exception('ErrorWhileSaving')
    return directory, file.name, extension[1:]
    

