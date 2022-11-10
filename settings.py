'''
    SETTINGS -
    LENGTH              -- Length of clips in seconds.
    MAX_VIDEOS          -- Maximum number of videos to get from the folder. 0 = unlimited (default)
    NUMBER_OF_CLIPS     -- Number of clips to create.
    VIDEO_PATH          -- Path to start searching through
    CLIP_PATH           -- Path clips get output to. Will be created if it doesn't exist.
    FILE_TYPES          -- File types movie_chopper will accept for chopping.
    CODEC               -- Video codec clips will save out as. List of available codecs in README.md
'''
LENGTH = 60
MAX_VIDEOS = 0 # WIP doesn't do anything for now.
NUMBER_OF_CLIPS = 1
VIDEO_PATH = "movies/"
CLIP_PATH = "clips/"
FILE_TYPES = [
    'avi',
    'mkv',
    'mp4'
]
CODEC = "libx264"