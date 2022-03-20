import subprocess


def testadd() -> None:
    cmd = ["poetry", "run", "python", "src/main.py", "--sum", "2", "2"]
    process = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    result, err = process.communicate()
    assert float(result.strip()) == 4
