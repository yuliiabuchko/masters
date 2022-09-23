import git

from main import *
from ExtractAndSerializeDiffs import compute_proj_diff
from errorprone.Util import CustomEncoder

PATH_TO_B_F_BUGS_DOT_JAR = "/home/yuliia/PycharmProjects/bugs-dot-jar-like-defects4j"

if __name__ == '__main__':
    proj = "wicket"  # maven accumulo camel commons-math flink jackrabbit-oak logging-log4j2 wicket
    proj_path = os.path.join(PATH_TO_DATABASE, proj)
    proj_bug_path = os.path.join(PATH_TO_B_F_BUGS_DOT_JAR, proj)

    class_paths = get_class_paths_from_dependencies(proj)

    parsed_projects_diffs = []

    os.chdir(proj_path)

    git.revert_changes()
    all_branches = git.get_all_branches()

    for i, branch in enumerate(all_branches):
        print(i + 1, branch)

        os.chdir(proj_path)
        git.revert_changes()

        git.checkout_branch(branch)
        buggy_files = get_changed_file(proj_path)

        git.apply_developer_patch()
        # shutil.rmtree(".bugs-dot-jar")

        os.chdir(proj_bug_path)
        git.revert_changes()
        git.checkout_branch(branch)

        parsed_projects_diffs.extend(compute_proj_diff(proj_bug_path, proj_path, buggy_files))

        git.revert_changes()


    parsed_output_file_name = os.path.join(PATH_TO_RESULTS, "diffs_parsed_" + proj + ".json")
    with open(parsed_output_file_name, "w") as file:
        json.dump(parsed_projects_diffs, file, cls=CustomEncoder, indent=4)