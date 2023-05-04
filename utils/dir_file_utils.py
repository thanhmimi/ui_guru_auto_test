import os
from config.base_config import wins_local_path, osx_linux_local_path


def default_file_path_to_upload():
    if os.path.exists(wins_local_path):
        return wins_local_path
    else:
        return osx_linux_local_path
