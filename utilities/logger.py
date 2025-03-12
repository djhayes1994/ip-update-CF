import logging
import datetime

class Logger:
    def __init__(self):
        pass

    def info(self, msg):
        print(f"[INFO] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: {msg}")

    def warn(self, msg):
        print(f"[WARN] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: {msg}")

    def failure(self, msg):
        print(f"[FAIL] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: {msg}")