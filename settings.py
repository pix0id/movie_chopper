'''
    SETTINGS -
    LENGTH              -- Length of clips in seconds.
    MAX_VIDEOS          -- Maximum number of videos to get from the folder. 0 = unlimited (default)
    NUMBER_OF_CLIPS     -- Number of clips to create.
    VIDEO_PATH          -- Path to start searching through
    CLIP_PATH           -- Path clips get output to. Will be created if it doesn't exist.
    OPENING_TRANSITION  -- Clip that will be played at beginning of concatenated video.
    TRANSITION          -- Clip that will be played between two videos.
    CLOSING_TRANSITION  -- Clip that will be played at the end of the concatenated video.
    CODEC               -- Video codec clips will save out as. List of available codecs in README.md
    METHOD              -- concatenation method. (default) "compose" Other value: 
    FILE_TYPES          -- File types movie_chopper will accept for chopping.

'''
LENGTH = 60
MAX_VIDEOS = 0 # WIP doesn't do anything for now.
NUMBER_OF_CLIPS = 1
VIDEO_PATH = "movies/"
CLIP_PATH = "clips/"
OPENING_TRANSITION = ""
TRANSITION = ""
CLOSING_TRANSITION = ""
CODEC = "libx264"
METHOD = "compose"
FILE_TYPES = [
    'avi',
    'mkv',
    'mp4'
]
