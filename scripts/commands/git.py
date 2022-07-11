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


def revert_changes():
    with subprocess.Popen('git checkout .'.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as _:
        pass
