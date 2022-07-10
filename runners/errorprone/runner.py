from typing import List
import subprocess


def run_error_prone(buggy_files: List[str], class_paths: List[str], path_out: str, path_logs: str) -> None:
    log = open(path_logs, 'a')

    f = open(path_out, 'w')

    for buggy_f in buggy_files:
        cmd = "javac  " \
              "-J-Xbootclasspath/p:/home/yuliia/PycharmProjects/masters/javac-9+181-r4173-1.jar " \
              "-XDcompilePolicy=simple " \
              "-processorpath /home/yuliia/PycharmProjects/masters/error_prone_core-2.10.0-with-dependencies.jar:/home/yuliia/PycharmProjects/StaticBugCheckers/static-checkers/dataflow-errorprone-3.15.0.jar:/home/yuliia/PycharmProjects/masters/jFormatString-3.0.0.jar ".split() \
              + ['-Xplugin:ErrorProne -Xep:CollectionIncompatibleType:WARN'] \
              + ['-cp', ':'.join(class_paths), buggy_f]

        # cmd = "javac  " \
        #       "-J--add-exports=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED  " \
        #       "-J--add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED   " \
        #       "-J--add-exports=jdk.compiler/com.sun.tools.javac.main=ALL-UNNAMED   " \
        #       "-J--add-exports=jdk.compiler/com.sun.tools.javac.model=ALL-UNNAMED   " \
        #       "-J--add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED   " \
        #       "-J--add-exports=jdk.compiler/com.sun.tools.javac.processing=ALL-UNNAMED   " \
        #       "-J--add-exports=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED   " \
        #       "-J--add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED   " \
        #       "-J--add-opens=jdk.compiler/com.sun.tools.javac.code=ALL-UNNAMED   " \
        #       "-J--add-opens=jdk.compiler/com.sun.tools.javac.comp=ALL-UNNAMED   " \
        #       "-XDcompilePolicy=simple " \
        #       "-processorpath /home/yuliia/PycharmProjects/masters/error_prone_core-2.10.0-with-dependencies.jar:/home/yuliia/PycharmProjects/StaticBugCheckers/static-checkers/dataflow-errorprone-3.15.0.jar   " \
        #       " ".split() \
        #       + ['-Xplugin:ErrorProne']  \
        #       + ['-cp', ':'.join(class_paths), buggy_f]

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
