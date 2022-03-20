import subprocess


def test_sum() -> None:
    cmd = ["poetry", "run", "python", "../src/calculator.py", "-sum", "3", "1"]
    process = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    result, err = process.communicate()
    assert float(result.strip()) == 4


def test_substract() -> None:
    cmd = ["poetry", "run", "python", "../src/calculator.py", "-substract", "3", "1"]
    process = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    result, err = process.communicate()
    assert float(result.strip()) == 2
