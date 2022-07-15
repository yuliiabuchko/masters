import subprocess


def clean_install():
    p = subprocess.Popen('mvn clean install -DskipTests=true'.split(), universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (cmd_out, _) = p.communicate()

    if not "BUILD SUCCESS" in cmd_out:
        print(cmd_out)

    # with subprocess.Popen('mvn clean install -DskipTests=true'.split(), stdout=subprocess.PIPE,
    #                       stderr=subprocess.STDOUT) as proc:
    #     a = "asd"
    #     print(a)
    #     pass