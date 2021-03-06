import os
import logging

from src.train import svm
from src.train import lstm

def config_log():
    """Config logging."""
    s_handler= logging.StreamHandler()
    s_handler.setLevel(logging.INFO)
    info_handler = logging.FileHandler(filename=os.path.join("output", "log", "info.log"), mode="w", encoding="utf-8")
    info_handler.setLevel(level=logging.INFO)
    err_handler = logging.FileHandler(filename=os.path.join("output", "log", "error.log"), mode="w", encoding="utf-8")
    err_handler.setLevel(logging.ERROR)

    logging.basicConfig(level=logging.INFO,
                        datefmt="%H:%M:%M",
                        format="{asctime} [{levelname}]>> {message}",
                        style="{",
                        handlers=[s_handler, info_handler, err_handler])


def main():
    config_log()
    lstm()
    # svm()


if __name__ == "__main__":
    main()

