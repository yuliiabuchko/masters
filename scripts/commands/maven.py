import subprocess


def clean_install():
    p = subprocess.Popen('mvn clean install -DskipTests=true'.split(), universal_newlines=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    (cmd_out, _) = p.communicate()

    if "BUILD SUCCESS" not in cmd_out:
        print("BUILD FAILED")
        print(cmd_out)
    else:
        print("BUILD SUCCESS")

    # with subprocess.Popen('mvn clean install -DskipTests=true'.split(), stdout=subprocess.PIPE,
    #                       stderr=subprocess.STDOUT) as proc:
    #     a = "asd"
    #     print(a)
    #     pass
