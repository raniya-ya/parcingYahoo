#!/usr/bin/env python
import os
import subprocess
import sys

def check_env():
  venv_path = os.environ.get('VIRTUAL_ENV')
  if venv_path:
    print(f"venv path is {venv_path}")
  else:
    raise Exception("ошибка запустите в виртуальном окружении")
  return venv_path

def download_lib():
  needed_libs = "beautifulsoup4\npytest"
  requirements_file = "requirements_file.txt"
  with open(requirements_file, "w") as f:
    f.write(needed_libs)
  subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_file])

def list_of_libs():
  result = subprocess.run([sys.executable, "-m","pip","freeze"], capture_output = True, text = True)
  installed_libs = result.stdout
  with open("requirements.txt","w") as f:
    f.write(installed_libs)
  print(installed_libs)
  return installed_libs

if __name__ == '__main__':
  check_env()
  download_lib()
  list_of_libs()
