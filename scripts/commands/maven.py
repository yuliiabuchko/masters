import subprocess


def clean_install():
    with subprocess.Popen('mvn clean install -DskipTests=true'.split(), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT) as _:
        pass