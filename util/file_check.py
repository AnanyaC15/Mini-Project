from pathlib import Path

def file_exist(model_path):
    file_path = model_path
    path = Path(file_path)
    if path.exists():
        print('The file exists')
    else:
        print('The file does not exist')