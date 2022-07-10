import os
import subprocess

from classpathsearcher import find_all_jars
from diffparser import get_changed_file
import json
from runners.errorprone.runner import run_error_prone

PATH_TO_DATABASE = "/home/yuliia/PycharmProjects/bugs-dot-jar"

if __name__ == '__main__':
    proj = "logging-log4j2"
    proj_path = os.path.join(PATH_TO_DATABASE, proj)

    with open("classpaths.json", "r") as file:
        data = json.load(file)
        class_paths = data[proj]

    os.chdir(proj_path)

    with subprocess.Popen('git branch -a'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as proc:
        all_branches = []
        for branch in proc.stdout.readlines():
            if "bugs-dot-jar_" in branch.decode("UTF-8") and not "HEAD" in branch.decode("UTF-8"):
                all_branches.append(branch.decode("UTF-8").strip())

    for branch in sorted(all_branches):
        subprocess.call(f'git checkout {branch}'.split())

        with subprocess.Popen('mvn clean install -DskipTests=true'.split(), stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT) as proc:
           pass

        buggy_files = get_changed_file(proj_path)

        run_error_prone(
            buggy_files,
            class_paths + find_all_jars(proj_path),
            '/home/yuliia/PycharmProjects/masters/results/bug/ep_output',
            '/home/yuliia/PycharmProjects/masters/logs/bug/ep_logs',
        )

        # TODO: run spotbugs
        # TODO: run last one

        # with subprocess.Popen('git apply .bugs-dot-jar/developer-patch.diff'.split(), stdout=subprocess.PIPE,
        #                       stderr=subprocess.STDOUT) as proc:
        #     pass
        #
        # with subprocess.Popen('mvn clean install -DskipTests=true'.split(), stdout=subprocess.PIPE,
        #                       stderr=subprocess.STDOUT) as proc:
        #     pass
        #
        # run_error_prone(
        #     buggy_files,
        #     class_paths,
        #     '/home/yuliia/PycharmProjects/masters/results/fix/ep_output',
        #     '/home/yuliia/PycharmProjects/masters/logs/fix/ep_logs',
        # )

        with subprocess.Popen('git checkout .'.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
            pass
