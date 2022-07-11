from typing import List

import os
import json


def get_class_paths_from_dependencies(proj: str) -> List[str]:
    with open("classpaths.json", "r") as file:
        data = json.load(file)
        return data[proj]


def find_all_jars(path: str) -> List[str]:
    res = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jar'):
                res.append(os.path.join(root, *dirs, file))
    return res
