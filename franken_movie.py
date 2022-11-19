from moviepy.editor import *
from settings import *
import movie_chopper as mc


# TODO: Count up concat file name so multiple can exist in directory
# TODO: Create folder for final concats.
# TODO: Clip folder cleanup

def concat_clips(video_folder):
    clips = mc.get_video_files(video_folder)
    clips_list = []

    for clip in clips:
        clips_list.append(VideoFileClip(clip))

    print(
    '''
    ================================
    ==     MAKING THE MONSTER     ==
    ================================
    '''
    )
    final_clip = concatenate_videoclips(
        clips_list,
        transition=VideoFileClip(TRANSITION) if ENABLE_TRANSITIONS else None,
        method="compose"
        )



    if (ENABLE_OPENING_TRANSITION or ENABLE_ENDING_TRANSITION) and ENABLE_TRANSITIONS:
        bookends = []
        if ENABLE_OPENING_TRANSITION:
            bookends.append(VideoFileClip(OPENING_TRANSITION))

        bookends.append(final_clip)

        if ENABLE_ENDING_TRANSITION:
            bookends.append(VideoFileClip(ENDING_TRANSITION))

        new_final = concatenate_videoclips(bookends,method="compose")

        new_final.write_videofile("concat.mp4")
    else:
        final_clip.write_videofile("concat.mp4")


if __name__ == "__main__":
    print("Run the app.py script.")
    print("Change preferences in settings.py")
    print("Leave me alone.")