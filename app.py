from utils import get_video_files
import movie_chopper
import franken_movie
from settings import *
from utils import dir_check


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
