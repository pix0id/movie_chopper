from moviepy.editor import concatenate_videoclips, VideoFileClip
from settings import *
from utils import clip_cleanup, audio_cleanup
from utils import get_video_files


def concat_clips(video_folder):
    clips = get_video_files(video_folder)
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
    try:
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

            new_final = concatenate_videoclips(bookends, method="compose")

            new_final.write_videofile(f"{CONCAT_PATH}concat.mp4")
        else:
            final_clip.write_videofile(f"{CONCAT_PATH}concat.mp4")
    except OSError as ose:
        print(f"OSERROR CONCATENATING FILES: {ose}")
    finally:
        if CLEANUP_CLIPS:
            print("Cleaning up files....")
            clip_cleanup()
            audio_cleanup()


if __name__ == "__main__":
    print("Run the app.py script.")
    print("Change preferences in settings.py")
    print("Leave me alone.")
