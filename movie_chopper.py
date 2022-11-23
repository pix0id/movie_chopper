from moviepy.editor import CompositeVideoClip, TextClip, VideoFileClip
import os
import math
import random
from settings import *
from utils import get_video_files


class Movie_chopper():
    # Logic variables
    touched_movies = []
    count = 0


    def __init__(self) -> None:
        pass


    def get_name_text(file):
        file_name = os.path.basename(file).split('.')
        video_name = file_name[0].split('_')
        return video_name


    def clip_random_movie(movies):
        """
            Chooses a random file from the list of movies
            Checks if the movie has been "touched" recently
            (Meaning other movies haven't been "touched" recently.)
            Clips chosen movie and writes file
        """

        global touched_movies
        global count
        try:
            current_movie = random.choice(movies)

            if current_movie not in touched_movies:
                count += 1

                current_movie_file = VideoFileClip(current_movie)
                touched_movies.append(current_movie)
                movie_name = get_name_text(current_movie_file.filename)
                movie_length = math.floor(current_movie_file.duration)

                start_index = random.randint(0, movie_length - LENGTH)

                clip = current_movie_file.subclip(start_index, start_index + LENGTH)
                clip.write_videofile(f"{CLIP_PATH}{count}_{movie_name[0]}.mp4", codec=CODEC)

                clip.close()
            else:
                '''
                Sort lists and check if they're the same. 
                If so, empty touched_movies and start chopping again
                '''
                movies.sort()
                touched_movies.sort()

                if movies == touched_movies:
                    touched_movies = []
        except Exception as e:
            print("ERROR DURING CLIPPING")
            print(e)


if __name__ == "__main__":
    print("Run the app.py script.")
    print("Change preferences in settings.py")
    print("Leave me alone.")
