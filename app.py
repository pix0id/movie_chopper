import modules.movie_chopper as movie_chopper
import modules.franken_movie as franken_movie
from modules.settings import clip_path, concat_path, video_path, number_of_clips
from modules.utils import dir_check, get_video_files

count = 0
movies = get_video_files(path=video_path)

fm = franken_movie.Franken_movie()
mc = movie_chopper.Movie_chopper(movies)


if __name__ == "__main__":
    print("Checking for required directories....")
    dir_check(clip_path)
    dir_check(concat_path)
    
    fm.set_concat_name()

    while count < number_of_clips:
        if mc.clip_random_movie():
            count += 1

    fm.concat_clips(video_folder=clip_path)
