from typing import List
import subprocess


def get_all_branches() -> List[str]:
    with subprocess.Popen('git branch -a'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as proc:
        branches = []
        for branch in proc.stdout.readlines():
            if "bugs-dot-jar_" in branch.decode("UTF-8") and not "HEAD" in branch.decode("UTF-8"):
                branches.append(branch.decode("UTF-8").strip())
        return sorted(branches)


def checkout_branch(branch):
    subprocess.call(f'git checkout {branch}'.split())


def apply_patch():
    with subprocess.Popen('git apply .bugs-dot-jar/developer-patch.diff'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as _:
        pass


def apply_flink_patch():
    with subprocess.Popen('git apply /home/yuliia/PycharmProjects/masters/flink.patch'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as _:
        pass

    with subprocess.Popen('git apply /home/yuliia/PycharmProjects/masters/flink-rat.patch'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as _:
        pass

    with subprocess.Popen('git apply /home/yuliia/PycharmProjects/masters/flink-rat-2.patch'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as _:
        pass

    with subprocess.Popen('git apply /home/yuliia/PycharmProjects/masters/flink-unlink.patch'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as _:
        pass

    with subprocess.Popen('git apply /home/yuliia/PycharmProjects/masters/flink-javadoc.patch'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as _:
        pass

    with subprocess.Popen('git apply /home/yuliia/PycharmProjects/masters/flink-revision.patch'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as _:
        pass


def revert_changes():
    with subprocess.Popen('git clean  -d  -fx .'.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as _:
        pass
    with subprocess.Popen('git checkout . -f'.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as _:
        pass
