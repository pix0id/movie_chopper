from pathlib import Path
import json
"""
    SETTINGS -
    LENGTH                      -- Length of clips in seconds.
    max_videos                  -- Maximum number of videos to get from the folder. 0 = unlimited (default)
    NUMBER_OF_CLIPS             -- Number of clips to create.
    VIDEO_PATH                  -- Path to start searching through
    CLIP_PATH                   -- Path clips get output to. Will be created if it doesn't exist.
    CONCAT_PATH                 -- Directory for final exports to save out in.
    MANUAL_CONCAT_PATH          -- clips folder that will be processed when running franken_movie.py directly. Default is CLIP_PATH.
    ENABLE_TRANSITIONS          -- "True" or "False", enables adding TRANSITIONs between clips. MUST BE TRUE IF YOU WANT OPENING/ENDING TRANSITIONS!!
    ENABLE_OPENING_TRANSITIONS   -- "True" or "False", enables adding a "Transition clip" at the start of the video.
    ENABLE_ENDING_TRANSITIONS    -- "True" or "False", enables adding a "Transition clip" at the end of the video.
    TRANSITION_PATH             -- The folder path where all opening/mid-roll/closing TRANSITIONs are stored.
                                   Include all TRANSITIONs in this one folder.
    OPENING_TRANSITION          -- Clip that will be played at beginning of concatenated video.
    TRANSITION                  -- Clip that will be played between two videos.
    ENDING_TRANSITION           -- Clip that will be played at the end of the concatenated video.
    CLEANUP_CLIPS               -- Boolean. True = deletes all clip files once concat finishes, will delete even if there's an error. False = leaves clips alone in the clips folder.
    CODEC                       -- Video CODEC clips will save out as. List of available CODECs in README.md
    METHOD                      -- Concatenation METHOD. (default) "compose" Other value:
    FILE_TYPES                  -- File types movie_chopper will accept for chopping.

"""
ROOT_DIR = Path(__file__).resolve().parents[1]
with open(f'{ROOT_DIR}/settings.json', 'r') as f:
    json_data = json.load(f)
    data = json_data[0]
    #TODO: Figure out if settings update after saving changes.
    LENGTH = data["LENGTH"]
    UNIFORM_SIZE = data["UNIFORM_SIZE"]
    VIDEO_CLIP_SIZE = (data["VIDEO_CLIP_SIZE_H"],data["VIDEO_CLIP_SIZE_W"])
    NUMBER_OF_CLIPS = data["NUMBER_OF_CLIPS"]
    VIDEO_PATH = data["VIDEO_PATH"]
    CLIP_PATH = data["CLIP_PATH"]
    CONCAT_PATH = data["CONCAT_PATH"]
    MANUAL_CONCAT_PATH = data["MANUAL_CONCAT_PATH"]
    ENABLE_TRANSITIONS = data["ENABLE_TRANSITIONS"]
    ENABLE_OPENING_TRANSITIONS = data["ENABLE_OPENING_TRANSITIONS"]
    ENABLE_ENDING_TRANSITIONS = data["ENABLE_ENDING_TRANSITIONS"]
    TRANSITION_PATH = data["TRANSITION_PATH"]
    OPENING_TRANSITION = f"{TRANSITION_PATH}{data['OPENING_TRANSITION']}"
    TRANSITION = f"{TRANSITION_PATH}{data['TRANSITION']}"
    ENDING_TRANSITION = f"{TRANSITION_PATH}{data['ENDING_TRANSITION']}"
    CLEANUP_CLIPS = data['CLEANUP_CLIPS']
    CODEC = data['CODEC']
    METHOD = data['METHOD']
    FILE_TYPES = data['FILE_TYPES']


    SCALPEL =  data['SCALPEL']




