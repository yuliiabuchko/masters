import os
from diffparser import get_changed_file

PATH_TO_STATIC_BUG_CHECKERS = "~/PycharmProjects/StaticBugCheckers/static-checkers"
EP_BIN = os.path.join(PATH_TO_STATIC_BUG_CHECKERS, "error_prone_ant-2.1.1.jar")

# TODO: what is prop-compile-path in Defects4J?

if __name__ == '__main__':
    print(EP_BIN)
    proj_path = "/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2"

    buggy_files = get_changed_file(proj_path)

    for buggy_f in buggy_files:
        cmd = ['java', '-Xbootclasspath/p:' + EP_BIN,
           'com.google.errorprone.ErrorProneCompiler',
           '-implicit:none'] + ['-cp', "TODO", buggy_f]

