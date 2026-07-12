import time


def follow(file):
    file.seek(0)

    while True:
        line = file.readline()
        if line:
            yield line
        else:
            time.sleep(0.5)
            continue