import os
import sys
import subprocess

modules = ["requests", "psutil", "netifaces", "urllib3", "threading", "concurrent.futures"]

for module in modules:
    subprocess.check_call([sys.executable, "-m", "pip", "install", module, "--quiet"])

print("Modules ok")
