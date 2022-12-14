import os
import pathlib
try:
    from modules.settings import CLIP_PATH, FILE_TYPES
except ModuleNotFoundError:
    from settings import CLIP_PATH, FILE_TYPES


def dir_check(path: str) -> None:
    '''
        If the directory does not exist, create it.
    '''
    try:
        if not os.path.isdir(path):
            os.mkdir(path)
    except OSError as e:
        print(f"ERROR WHILE CREATING {path}: {e}")



def get_video_files(path: str) -> list:
    """
        Generates list of videos from specified video path.
        Does not work with nested directories.
        Make sure the videos are the ONLY thing in the directory. ALL FILES are added to the list currently.
    """
    paths = []
    directories = []

    for root, dirs, files in os.walk(path):
        for _dir in dirs:
            directories.append(_dir)

        for _file in files:
            filetype = get_file_extension(_file)
            if filetype:
                paths.append(os.path.join(root, _file))

    return paths


def get_file_extension(file: str) -> str | bool:
    split_name = file.split('.')
    ext = split_name[-1]

    if ext in FILE_TYPES:
        return ext

    return False


def clip_cleanup() -> None:
    try:
        clips = get_video_files(CLIP_PATH)

        for clip in clips:
            os.remove(clip)
    except OSError as e:
        print(f"ERROR DURING CLIP CLEANUP: {e}")


def audio_cleanup() -> None:
    try:
        for mp3 in pathlib.Path("").glob('.mp3'):
            os.remove(mp3)
    except OSError as e:
        print(f"ERROR DELETING ROGUE AUDIO FILES: {e}")

def get_seconds(timestamp: str) -> int:
    """
        Get seconds from time.
    """
    h,m,s=timestamp.split(":")
    return int(h)*3600+int(m)*60+int(s)
