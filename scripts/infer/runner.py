import shutil
import tempfile
from typing import List
import subprocess
import os


def run_infer(buggy_files: List[str], class_paths: List[str], path_out_txt: str, path_out_json: str, branch_name: str, path_logs: str) -> None:
    os.makedirs(path_out_txt, exist_ok=True)
    os.makedirs(path_out_json, exist_ok=True)
    os.makedirs(path_logs, exist_ok=True)

    infer_txt_results = []
    infer_json_results = []

    log = open(os.path.join(path_logs, 'inf_logs'), 'a+')
    tmp_out_dir = tempfile.mkdtemp(prefix='infer-out.', dir=os.getcwd())

    for buggy_f in buggy_files:
        cmd = f"/home/yuliia/PycharmProjects/masters/infer-linux64-v1.1.0/bin/infer run -o {tmp_out_dir} -- javac".split() \
              + ['-cp' if class_paths else '', ':'.join(class_paths), buggy_f]

        log.write(" ".join(cmd) + "\n\n")

        p = subprocess.Popen(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (cmd_out, _) = p.communicate()

        # for line in cmd_out.split("\n"):
        #     print(line)

        log.write(cmd_out + "\n")
        log.write("*" * 24 + "\n\n")

        try:
            with open(os.path.join(os.getcwd(), tmp_out_dir + '/report.txt'), 'r') as file:
                infer_txt_results.append(file.read())
        except IOError:
            print("error txt")
            pass

        try:
            with open(os.path.join(os.getcwd(), tmp_out_dir + '/report.json'), 'r') as file:
                infer_json_results.append(file.read().strip("\n"))
        except IOError:
            print("error json")
            pass

    shutil.rmtree(tmp_out_dir)

    with open(os.path.join(path_out_txt, branch_name), 'w') as file:
        file.write("\n".join(res for res in infer_txt_results))

    with open(os.path.join(path_out_json, branch_name), 'w') as file:
        file.write(manual_merge_json(infer_json_results))

    log.write("#" * 212 + "\n\n")
    log.close()


def manual_merge_json(json_strings):
    json_strings = [x for x in json_strings if x != "" and x != '[]']
    length = len(json_strings)

    if length == 1:
        return json_strings[0]

    if length > 1:
        for i in range(1, length):
            json_strings[i] = json_strings[i][1:-1]
        json_strings[0] = json_strings[0][:-1]
        json_strings[length - 1] = json_strings[length - 1] + ']'
        return ",".join(s for s in json_strings)

    return ""
