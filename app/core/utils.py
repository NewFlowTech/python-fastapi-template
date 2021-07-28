import os

def check_exists_folder(folder_path: str, create_if_not: bool = False) -> bool:
    return True

def check_exists_file(filename: str, create_if_not: bool = False) -> bool:
    if os.path.isfile(filename):
        return True
    elif create_if_not:
        open(filename,"w")
        return True
    else:
        return False

def check_env_by_name(envname: str) -> bool:
    return (lambda x: True if x != None else False)(os.getenv(envname))

