import modules.movie_chopper as movie_chopper
import modules.franken_movie as franken_movie
import modules.movie_scalpel as movie_scalpel
from modules.settings import *
from modules.utils import dir_check, get_video_files


count = 0
movies = get_video_files(path=VIDEO_PATH)

fm = franken_movie.Franken_movie()
mc = movie_chopper.Movie_chopper(movies)


if __name__ == "__main__":
    print("Checking for required directories....")
    dir_check(CLIP_PATH)
    dir_check(CONCAT_PATH)
    
    fm.set_concat_name()

    while count < NUMBER_OF_CLIPS:
        if mc.clip_random_movie():
            count += 1

    fm.concat_clips(video_folder=CLIP_PATH)
