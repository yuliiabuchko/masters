import os
import shutil
import sys
from collections import defaultdict

from scripts.classpathsearcher import find_all_jars, get_class_paths_from_dependencies
from scripts.commands import git
from scripts.commands import maven
from scripts.diffparser import get_changed_file, get_total_size_of_diffs
from scripts.errorprone.runner import run_error_prone
from scripts.spotbugs.runner import run_spotbugs
from scripts.infer.runner import run_infer


PATH_TO_DATABASE = "/home/yuliia/PycharmProjects/bugs-dot-jar"
PATH_TO_LOGS = "/home/yuliia/PycharmProjects/masters/logs"
PATH_TO_RESULTS = "/home/yuliia/PycharmProjects/masters/results"

BUG_FOLDER = "bug"
FIX_FOLDER = "fix"

PROJECTS = ["accumulo", "camel", "commons-math", "flink", "jackrabbit-oak", "logging-log4j2", "maven", "wicket"]
# accumulo done
if __name__ == '__main__':

    number_of_buggy_files_per_bug = defaultdict(int)
    size_of_diff_per_bug = defaultdict(int)

    for proj in PROJECTS:
        proj_path = os.path.join(PATH_TO_DATABASE, proj)
        os.chdir(proj_path)
        git.revert_changes()
        all_branches = git.get_all_branches()

        for i, branch in enumerate(all_branches):
            print(i + 1, branch)
            git.checkout_branch(branch)
            number_of_buggy_files_per_bug[len(get_changed_file(proj_path))] += 1
            size_of_diff_per_bug[get_total_size_of_diffs(proj_path)] += 1
            git.revert_changes()

    print(number_of_buggy_files_per_bug)
    print("*" * 20)
    print(size_of_diff_per_bug)
