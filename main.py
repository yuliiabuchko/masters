import os
import shutil

from scripts.classpathsearcher import find_all_jars, get_class_paths_from_dependencies
from scripts.commands import git
from scripts.commands import maven
from scripts.diffparser import get_changed_file
from scripts.errorprone.runner import run_error_prone
from scripts.spotbugs.runner import run_spotbugs


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
        if i + 1 <= 0:
            continue
        print(i + 1, branch)
        git.checkout_branch(branch)
        buggy_files = get_changed_file(proj_path)

        shutil.rmtree(".bugs-dot-jar")

        git.apply_proj_specific_patches(proj)

        maven.clean_install()
        # run_error_prone(
        #     buggy_files,
        #     class_paths + (find_all_jars(proj_path) if proj != "maven" else []),
        #     os.path.join(PATH_TO_RESULTS, BUG_FOLDER, 'ep_output'),
        #     proj + "_" + branch.split('/')[-1],
        #     os.path.join(PATH_TO_LOGS, BUG_FOLDER),
        # )
        run_spotbugs(
            buggy_files,
            class_paths + find_all_jars(proj_path) if proj != "maven" else [],
            os.path.join(PATH_TO_RESULTS, BUG_FOLDER, 'sb_output'),
            proj + "_" + branch.split('/')[-1],
            os.path.join(PATH_TO_LOGS, BUG_FOLDER),
        )
        # TODO: run infer

        git.revert_changes()
        git.apply_developer_patch()

        shutil.rmtree(".bugs-dot-jar")
        git.apply_proj_specific_patches(proj)

        maven.clean_install()
        # run_error_prone(
        #     buggy_files,
        #     class_paths + (find_all_jars(proj_path) if proj != "maven" else []),
        #     os.path.join(PATH_TO_RESULTS, FIX_FOLDER, "ep_output"),
        #     proj + "_" + branch.split('/')[-1],
        #     os.path.join(PATH_TO_LOGS, FIX_FOLDER),
        # )
        run_spotbugs(
            buggy_files,
            class_paths + (find_all_jars(proj_path) if proj != "maven" else []),
            os.path.join(PATH_TO_RESULTS, FIX_FOLDER, "sp_output"),
            proj + "_" + branch.split('/')[-1],
            os.path.join(PATH_TO_LOGS, FIX_FOLDER),
        )
        # TODO: run infer

        git.revert_changes()


# accumulo 77 + 94 fail - compilation errors
# camel build fail for all
# common-math all ok (but cannot find symbol in logs)
# flink all done
# jackrabbit-oak 1-25 27-101 104-124 126-198 200-206 208 210 211 213-220 224-225 227 237 243-244 ok 26 102 103 125 199f 207 209 212 221-223 226 228-236 238-242 fail 245+??
# logging-log4j2 5 + 61 i can't fix
# maven - strange issues (error opening zip files anyways) 9 11 15-24 26-34 36-39 ok 1-8 10 12-14 25 35 40-48 fail
# wicket build fails all the time
