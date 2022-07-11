import os

from typing import List


def get_changed_file(proj_path) -> List[str]:
    diff_path = os.path.join(proj_path, ".bugs-dot-jar/developer-patch.diff")
    changed = []

    with open(diff_path, "r") as file:
        for line in file:
            if line.startswith("---"):
                changed.append(line.strip()[6:])
    return changed



