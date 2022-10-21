import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf8") as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        file_list = list(file_reader)
        return file_list
