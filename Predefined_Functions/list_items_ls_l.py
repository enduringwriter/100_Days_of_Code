# Long list of items

import subprocess

def list_items():
    subprocess.call(["ls", "-l"])

list_items()