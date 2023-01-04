import random
from moviepy.editor import concatenate_videoclips, VideoFileClip
import os

try:
    from modules.settings import *
    from modules.utils import clip_cleanup, audio_cleanup, get_video_files
except ModuleNotFoundError:
    from settings import *
    from utils import clip_cleanup, audio_cleanup, get_video_files

class Franken_movie():

    concat_name = ""
    count = 0

    def __init__(self) -> None:
        pass
        
    def set_concat_name(self) -> None:
        name = input("Enter name for Concat (Leave blank for default): ")

        if len(name) > 0:
            Franken_movie.concat_name = name
        else:
            for path in os.listdir(concat_path):
                if os.path.isfile(os.path.join(concat_path, path)):
                    Franken_movie.count += 1
            
            Franken_movie.concat_name = f"concat_{Franken_movie.count}"

    def concat_clips(self, video_folder: str) -> None:
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
                transition=VideoFileClip(transition) if enable_transitions else None,
                method="compose"
            )

            if (enable_opening_transition or enable_ending_transition) and enable_transitions:
                bookends = []
                if enable_opening_transition:
                    bookends.append(VideoFileClip(opening_transition))

                bookends.append(final_clip)

                if enable_ending_transition:
                    bookends.append(VideoFileClip(ending_transition))

                new_final = concatenate_videoclips(bookends, method="compose")

                new_final.write_videofile(f"{concat_path}{Franken_movie.concat_name}.mp4",codec=codec)
            else:
                final_clip.write_videofile(f"{concat_path}{Franken_movie.concat_name}.mp4",codec=codec)
        except OSError as ose:
            print(f"OSERROR CONCATENATING FILES: {ose}")
        finally:
            if cleanup_clips:
                print("Cleaning up files....")
                clip_cleanup()
                audio_cleanup()


if __name__ == "__main__":
    fm = Franken_movie()
    fm.set_concat_name()
    fm.concat_clips(video_folder=manual_concat_path)