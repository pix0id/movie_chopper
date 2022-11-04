'''
    SETTINGS -
    LENGTH              -- Length of clips in seconds.
    NUMBER_OF_CLIPS     -- Number of clips to create.
    VIDEO_PATH          -- Path to start searching through
    CLIP_PATH           -- Path clips get output to. Will be created if it doesn't exist.
    FILE_TYPES          -- File types movie_chopper will accept for chopping.
'''
LENGTH = 60
NUMBER_OF_CLIPS = 1
VIDEO_PATH = "movies/"
CLIP_PATH = "clips/"
FILE_TYPES = [
    'avi',
    'mkv',
    'mp4'
]