from typing import List
import os
import subprocess


def run_spotbugs(buggy_files: List[str], class_paths: List[str], path_out: str, branch_name: str,
                    path_logs: str) -> None:
    os.makedirs(path_out, exist_ok=True)
    os.makedirs(path_logs, exist_ok=True)

    # 21 stopeed

    log = open(os.path.join(path_logs, 'sb_logs'), 'a+')

    list(map(lambda name: name.replace("/", ".")[:-5].split(".java."), buggy_files))
    cmd = f"java -jar /home/yuliia/PycharmProjects/masters/spotbugs-4.7.2/lib/spotbugs.jar -textui  -xml:withMessages={os.path.join(path_out, branch_name)}".split() + \
          ["-onlyAnalyze",
           ",".join(list(map(lambda name: name[1], filter(lambda name: len(name) > 1, list(map(lambda name: name.replace("/", ".")[:-5].split(".java."), buggy_files))))))] + \
          ["-auxclasspath", ':'.join(class_paths)] + \
          ["-low", "."]

    log.write(" ".join(cmd) + "\n\n")

    p = subprocess.Popen(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (out, _) = p.communicate()

    for line in out.split("\n"):
        print(line)

    log.write(out + "\n")

    log.write("#" * 212 + "\n\n")
    log.close()

# java -jar /home/yuliia/PycharmProjects/masters/spotbugs-4.7.2/lib/spotbugs.jar -textui -xml:withMessages=spotbugs.xml -onlyAnalyze org.apache.accumulo.core.iterators.Filter -auxclasspath /home/yuliia/PycharmProjects/masters/jars/hadoop-core-1.0.4.jar:/home/yuliia/PycharmProjects/masters/jars/hadoop-tools-1.0.4.jar:/home/yuliia/PycharmProjects/masters/jars/zookeeper-3.3.1.jar:/home/yuliia/PycharmProjects/masters/jars/commons-codec-1.3.jar:/home/yuliia/PycharmProjects/masters/jars/slf4j-api-1.7.36.jar:/home/yuliia/PycharmProjects/masters/jars/slf4j-nop-1.7.36.jar:/home/yuliia/PycharmProjects/masters/jars/commons-cli-1.2.jar:/home/yuliia/PycharmProjects/masters/jars/log4j-1.2.16.jar:/home/yuliia/PycharmProjects/masters/jars/commons-vfs2-2.0.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/accumulo/test/system/auto/stress/simple/TestCombinerX.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/accumulo/test/system/auto/stress/simple/TestCombinerY.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/accumulo/src/start/src/test/resources/ClassLoaderTestA/Test.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/accumulo/src/start/src/test/resources/ClassLoaderTestB/Test.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/accumulo/src/start/src/test/resources/ClassLoaderTestC/Test.jar -low  .
