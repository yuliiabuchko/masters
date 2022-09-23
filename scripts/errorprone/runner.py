from typing import List
import subprocess
import os


def run_error_prone(buggy_files: List[str], class_paths: List[str], path_out: str, branch_name: str, path_logs: str) -> None:
    os.makedirs(path_out, exist_ok=True)
    os.makedirs(path_logs, exist_ok=True)

    log = open(os.path.join(path_logs, 'ep_logs'), 'a+')
    f = open(os.path.join(path_out, branch_name), 'w+')

    for buggy_f in buggy_files:
        cmd = "javac  " \
              "-J-Xbootclasspath/p:/home/yuliia/PycharmProjects/masters/javac-9+181-r4173-1.jar " \
              "-XDcompilePolicy=simple " \
              "-processorpath /home/yuliia/PycharmProjects/masters/error_prone_core-2.10.0-with-dependencies.jar:/home/yuliia/PycharmProjects/StaticBugCheckers/static-checkers/dataflow-errorprone-3.15.0.jar:/home/yuliia/PycharmProjects/masters/jFormatString-3.0.0.jar ".split() \
              + ['-Xplugin:ErrorProne -Xep:CollectionIncompatibleType:WARN'] \
              + ['-cp', ':'.join(class_paths), buggy_f]

        log.write(" ".join(cmd) + "\n\n")

        p = subprocess.Popen(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (cmd_out, _) = p.communicate()

        # for line in cmd_out.split("\n"):
        #     print(line)

        f.write(cmd_out)

        log.write(cmd_out + "\n")
        log.write("*" * 24 + "\n\n")

    log.write("#" * 212 + "\n\n")
    log.close()
