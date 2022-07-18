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


def apply_developer_patch():
    apply_patch('.bugs-dot-jar/developer-patch.diff')


def apply_patch(path: str):
    with subprocess.Popen(f'git apply {path}'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as _:
        pass


def apply_proj_specific_patches(proj: str):
    if proj == "flink":
        apply_flink_patch()
    if proj == "accumulo":
        apply_accumulo_patch()


def apply_accumulo_patch():
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-wagon.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-integration-tests.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-integration.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-mini.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-rat.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-compile.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-rat-2.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-rat-manual.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-invoker.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/accumulo-findbugs.patch')


def apply_flink_patch():
    apply_patch('/home/yuliia/PycharmProjects/masters/flink.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/flink-rat.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/flink-rat-2.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/flink-unlink.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/flink-javadoc.patch')
    apply_patch('/home/yuliia/PycharmProjects/masters/flink-revision.patch')


def revert_changes():
    with subprocess.Popen('git clean  -d  -fx .'.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as _:
        pass
    with subprocess.Popen('git checkout . -f'.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as _:
        pass
