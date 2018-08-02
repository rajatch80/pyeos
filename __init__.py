from sys import path as sys_path
from os import environ as os_environ

sys_path.append(os_environ.get('BASE_DIR'))