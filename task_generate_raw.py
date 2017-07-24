import glob
import os
from os.path import join, dirname, basename
from shutil import copy2
from task_make_annotation import get_annotated_files


def get_new_files(folder):
    files = filter(os.path.isfile, glob.glob(join(folder, "*")))
    files.sort(key=lambda x: -os.path.getmtime(x))
    files = [basename(file) for file in files]
    return files


if __name__ == '__main__':
    data_folder = join(dirname(__file__), "sources", "corpus.vinews", "vn_news", "data")
    data_files = get_new_files(data_folder)
    raw_folder = join(dirname(__file__), "raw", "vinews")
    raw_files = os.listdir(raw_folder)
    new_files = set(data_files) - set(raw_files)
    new_files = list(new_files)[:30]
    for file in new_files:
        copy2(join(data_folder, file), raw_folder)
