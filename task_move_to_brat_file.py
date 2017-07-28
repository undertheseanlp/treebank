import shutil
from os.path import dirname, join

from os import listdir

if __name__ == '__main__':
    brat = join(dirname(__file__), "brat")
    files = listdir(brat)
    files = [f for f in files if f.endswith(".ann") or f.endswith(".txt")]
    brat_final = join(dirname(__file__), "brat_final")
    for f in files:
        shutil.move(join(brat, f), join(brat_final, f))
