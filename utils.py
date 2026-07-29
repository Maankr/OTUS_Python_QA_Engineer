import os

def get_log_files(path):

    if os.path.isfile(path):
        return [path]

    if os.path.isdir(path):
        files = []

        for filename in os.listdir(path):
            full_path = os.path.join(path, filename)

            if os.path.isfile(full_path):
                files.append(full_path)

        return files

    raise FileNotFoundError(path)