from pathlib import Path
"""
    SETTINGS -
    LENGTH                      -- Length of clips in seconds.
    MAX_VIDEOS                  -- Maximum number of videos to get from the folder. 0 = unlimited (default)
    NUMBER_OF_CLIPS             -- Number of clips to create.
    VIDEO_PATH                  -- Path to start searching through
    CLIP_PATH                   -- Path clips get output to. Will be created if it doesn't exist.
    CONCAT_PATH                 -- Directory for final exports to save out in.
    MANUAL_CONCAT_PATH          -- clips folder that will be processed when running franken_movie.py directly. Default is CLIP_PATH.
    ENABLE_TRANSITIONS          -- "True" or "False", enables adding transitions between clips. MUST BE TRUE IF YOU WANT OPENING/ENDING TRANSITIONS!!
    ENABLE_OPENING_TRANSITION   -- "True" or "False", enables adding a "Transition clip" at the start of the video.
    ENABLE_ENDING_TRANSITION    -- "True" or "False", enables adding a "Transition clip" at the end of the video.
    TRANSITION_PATH             -- The folder path where all opening/mid-roll/closing transitions are stored.
                                   Include all transitions in this one folder.
    OPENING_TRANSITION          -- Clip that will be played at beginning of concatenated video.
    TRANSITION                  -- Clip that will be played between two videos.
    ENDING_TRANSITION           -- Clip that will be played at the end of the concatenated video.
    CLEANUP_CLIPS               -- Boolean. True = deletes all clip files once concat finishes, will delete even if there's an error. False = leaves clips alone in the clips folder.
    CODEC                       -- Video codec clips will save out as. List of available codecs in README.md
    METHOD                      -- Concatenation method. (default) "compose" Other value:
    FILE_TYPES                  -- File types movie_chopper will accept for chopping.

"""

ROOT_DIR = Path(__file__).resolve().parents[1]
LENGTH = 60
UNIFORM_SIZE = True
VIDEO_CLIP_SIZE = (1920,1080)
NUMBER_OF_CLIPS = 5
VIDEO_PATH = "movies/"
CLIP_PATH = "clips/"
CONCAT_PATH = "final_videos/"
MANUAL_CONCAT_PATH = "clips/"
ENABLE_TRANSITIONS = False
ENABLE_OPENING_TRANSITION = False
ENABLE_ENDING_TRANSITION = False
TRANSITION_PATH = "transitions/"
OPENING_TRANSITION = f"{TRANSITION_PATH}Shatner_door_open.mp4"
TRANSITION = f"{TRANSITION_PATH}Shatner_door_transition.mp4"
ENDING_TRANSITION = f"{TRANSITION_PATH}Shatner_door_close.mp4"
CLEANUP_CLIPS = False
CODEC = "libx264"
METHOD = "compose"
FILE_TYPES = [
    'avi',
    'mkv',
    'mp4'
]


SCALPEL = True

