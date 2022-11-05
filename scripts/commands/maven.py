import subprocess


def clean_install():
    p = subprocess.Popen('mvn clean install -DskipTests=true -Dmaven.wagon.http.retryHandler.count=10'.split(), universal_newlines=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    try:
        (cmd_out, _) = p.communicate(timeout=10*60)
    except subprocess.TimeoutExpired:
        print("Timeout clean install")
        return

    if "BUILD SUCCESS" not in cmd_out:
        print("BUILD FAILED")
        # print(cmd_out)
    else:
        print("BUILD SUCCESS")

    # with subprocess.Popen('mvn clean install -DskipTests=true'.split(), stdout=subprocess.PIPE,
    #                       stderr=subprocess.STDOUT) as proc:
    #     a = "asd"
    #     print(a)
    #     pass
