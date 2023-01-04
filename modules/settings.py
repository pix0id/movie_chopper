from pathlib import Path
"""
    SETTINGS -
    length                      -- Length of clips in seconds.
    max_videos                  -- Maximum number of videos to get from the folder. 0 = unlimited (default)
    number_of_clips             -- Number of clips to create.
    video_path                  -- Path to start searching through
    clip_path                   -- Path clips get output to. Will be created if it doesn't exist.
    concat_path                 -- Directory for final exports to save out in.
    manual_concat_path          -- clips folder that will be processed when running franken_movie.py directly. Default is clip_path.
    enable_transitions          -- "True" or "False", enables adding transitions between clips. MUST BE TRUE IF YOU WANT OPENING/ENDING transitionS!!
    enable_opening_transition   -- "True" or "False", enables adding a "Transition clip" at the start of the video.
    enable_ending_transition    -- "True" or "False", enables adding a "Transition clip" at the end of the video.
    transition_path             -- The folder path where all opening/mid-roll/closing transitions are stored.
                                   Include all transitions in this one folder.
    opening_transition          -- Clip that will be played at beginning of concatenated video.
    transition                  -- Clip that will be played between two videos.
    ending_transition           -- Clip that will be played at the end of the concatenated video.
    cleanup_clips               -- Boolean. True = deletes all clip files once concat finishes, will delete even if there's an error. False = leaves clips alone in the clips folder.
    codec                       -- Video codec clips will save out as. List of available codecs in README.md
    method                      -- Concatenation method. (default) "compose" Other value:
    file_types                  -- File types movie_chopper will accept for chopping.

"""

root_dir = Path(__file__).resolve().parents[1]
length = 60
uniform_size = True
video_clip_size = (1920,1080)
number_of_clips = 5
video_path = "movies/"
clip_path = "clips/"
concat_path = "final_videos/"
manual_concat_path = "clips/"
enable_transitions = False
enable_opening_transition = False
enable_ending_transition = False
transition_path = "transitions/"
opening_transition = f"{transition_path}Shatner_door_open.mp4"
transition = f"{transition_path}Shatner_door_transition.mp4"
ending_transition = f"{transition_path}Shatner_door_close.mp4"
cleanup_clips = False
codec = "libx264"
method = "compose"
file_types = [
    'avi',
    'mkv',
    'mp4'
]


scalpel = True

