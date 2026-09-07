#!/usr/bin/env python
import os

def get_name_of_venv():
  return os.environ.get('VIRTUAL_ENV')

if __name__ == '__main__':
  venv_path = get_name_of_venv()
  if venv_path:
    print(f'Your current virtual env is {venv_path}')
  else:
    print('No venv active')