import os
import shutil

from scripts.classpathsearcher import find_all_jars, get_class_paths_from_dependencies
from scripts.commands import git
from scripts.commands import maven
from scripts.diffparser import get_changed_file
from scripts.errorprone.runner import run_error_prone


PATH_TO_DATABASE = "/home/yuliia/PycharmProjects/bugs-dot-jar"
PATH_TO_LOGS = "/home/yuliia/PycharmProjects/masters/logs"
PATH_TO_RESULTS = "/home/yuliia/PycharmProjects/masters/results"

BUG_FOLDER = "bug"
FIX_FOLDER = "fix"

if __name__ == '__main__':
    proj = "accumulo"
    proj_path = os.path.join(PATH_TO_DATABASE, proj)

    class_paths = get_class_paths_from_dependencies(proj)

    os.chdir(proj_path)

    git.revert_changes()
    all_branches = git.get_all_branches()

    for i, branch in enumerate(all_branches):
        if i + 1 <= 50:
            continue
        # accumulo 1-62, 65 67 69 74 75 78 85 86 90-93 95-98 ok, 63 64 66 68 70-73 76 77 79-84 87-89 94 fail
        # flink all done
        # logging-log4j2 5 + 61 i cant fix
        print(i + 1, branch)
        git.checkout_branch(branch)
        buggy_files = get_changed_file(proj_path)

        shutil.rmtree(".bugs-dot-jar")

        git.apply_proj_specific_patches(proj)

        maven.clean_install()
        run_error_prone(
            buggy_files,
            class_paths + find_all_jars(proj_path),
            os.path.join(PATH_TO_RESULTS, BUG_FOLDER, 'ep_output'),
            proj + "_" + branch.split('/')[-1],
            os.path.join(PATH_TO_LOGS, BUG_FOLDER),
        )
        # TODO: run spotbugs
        # TODO: run infer

        git.revert_changes()
        git.apply_developer_patch()

        shutil.rmtree(".bugs-dot-jar")
        git.apply_proj_specific_patches(proj)

        maven.clean_install()
        run_error_prone(
            buggy_files,
            class_paths + find_all_jars(proj_path),
            os.path.join(PATH_TO_RESULTS, FIX_FOLDER, "ep_output"),
            proj + "_" + branch.split('/')[-1],
            os.path.join(PATH_TO_LOGS, FIX_FOLDER),
        )
        # TODO: run spotbugs
        # TODO: run infer

        git.revert_changes()
