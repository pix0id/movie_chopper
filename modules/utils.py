import os
import pathlib
try:
    from modules.settings import clip_path, file_types
except ModuleNotFoundError:
    from settings import clip_path, file_types


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
    """
        Get file extention and verify that it is in the
        file_types constant. If not, return false.
    """
    split_name = file.split('.')
    ext = split_name[-1]

    if ext in file_types:
        return ext

    return False


def clip_cleanup() -> None:
    """
        Removes all clips from the clips directory.
        Used for cleanup after concatenation.
    """
    try:
        clips = get_video_files(clip_path)

        for clip in clips:
            os.remove(clip)
    except OSError as e:
        print(f"ERROR DURING CLIP CLEANUP: {e}")


def audio_cleanup() -> None:
    """
        Clean up audio files left behind in root directory
        if an error occurs.
    """
    try:
        for mp3 in pathlib.Path("").glob('.mp3'):
            os.remove(mp3)
    except OSError as e:
        print(f"ERROR DELETING ROGUE AUDIO FILES: {e}")

def get_seconds(timestamp: str) -> int:
    """
        Convert timestamp to seconds.
    """
    h,m,s=timestamp.split(":")
    return int(h)*3600+int(m)*60+int(s)

def file_name_text(file) -> str:
        file_name = os.path.basename(file).split('.')
        video_name = file_name[0].split('_')
        return video_name