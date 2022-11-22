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

def get_total_size_of_diffs(proj_path: str) -> int:
    diff_path = os.path.join(proj_path, ".bugs-dot-jar/developer-patch.diff")
    total = 0
    with open(diff_path, "r") as file:
        for line in file:
            if (line.startswith("+") or line.startswith('-')) and not line.startswith("+++") and not line.startswith(("---")):
                total += 1
    return total




