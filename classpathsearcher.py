from typing import List

import os

def find_all_jars(path: str) -> List[str]:
    res = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jar'):
                res.append(os.path.join(root, *dirs, file))
    return res

