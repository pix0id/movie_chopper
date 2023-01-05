from moviepy.editor import *
import os
import math
import random


try:
    from modules.settings import *
    from modules.utils import dir_check, get_video_files, file_name_text
except ModuleNotFoundError:
    from settings import *
    from utils import dir_check, get_video_files, file_name_text


class Movie_chopper():

    touched_movies = []

    def __init__(self, movies) -> None:
        self.movies = movies
        self.count = 0


    def clip_random_movie(self) -> bool:
        """
            Chooses a random file from the list of movies
            Checks if the movie has been "touched" recently
            (Meaning other movies haven't been "touched" recently.)
            Clips chosen movie and writes file
        """

        try:
            current_movie = random.choice(self.movies)

            if current_movie not in Movie_chopper.touched_movies:
                self.count += 1

                current_movie_file = VideoFileClip(current_movie)
                Movie_chopper.touched_movies.append(current_movie)
                movie_name = file_name_text(current_movie_file.filename)
                movie_LENGTH = math.floor(current_movie_file.duration)

                start_index = random.randint(0, movie_LENGTH - LENGTH)

                clip = current_movie_file.subclip(start_index, start_index + LENGTH)

                if UNIFORM_SIZE:
                    resized_clip = clip.resize(VIDEO_CLIP_SIZE)
                    resized_clip.write_videofile(f"{CLIP_PATH}{self.count}_{movie_name[0]}.mp4", codec=CODEC)
                else:
                    clip.write_videofile(f"{CLIP_PATH}{self.count}_{movie_name[0]}.mp4", codec=CODEC)

                clip.close()


                return True
            else:
                '''
                Sort lists and check if they're the same. 
                If so, empty touched_movies and start chopping again
                '''
                self.movies.sort()
                Movie_chopper.touched_movies.sort()

                if self.movies == Movie_chopper.touched_movies:
                    Movie_chopper.touched_movies = []
                

                return False

        except Exception as e:
            print("ERROR DURING CLIPPING")
            print(e)
            

            return False

    
    def select_video(self) -> str:
        videos = get_video_files(VIDEO_PATH)

        for count, video in enumerate(videos):
            print(f"{count}: {video}")

        print("="*20)

        selection = input("Enter index of video to slap-chop: ")

        return videos[int(selection)]


    def slap_chop(self, video: str) -> None:
        name = file_name_text(video)
        name = name[0]

        dir_check(f"{name}")

        video_file = VideoFileClip(video)

        video_length = video_file.duration
        start_index = 0
        count = 0
        clip_total = video_length - LENGTH / LENGTH

        
        while count < clip_total:
            if start_index + LENGTH < video_length:
                clip = video_file.subclip(start_index, start_index + LENGTH)
            else:
                clip = video_file.subclip(start_index, video_length)
            
            clip.write_videofile(f"{name}/{count}_{name}.mp4", codec=CODEC)
            
            count += 1
            start_index += LENGTH
            
        video_file.close()
    
    def custom_clip(self, video_file: str, timestamp: tuple) -> None:

        movie_name = file_name_text(video_file.filename)
        clip = video_file.subclip(timestamp[0], timestamp[1])

        
        clip.write_videofile(f"{CLIP_PATH}{movie_name[0]}/{self.count}_{movie_name[0]}.mp4", codec=CODEC)

        self.count += 1
        clip.close()


if __name__ == "__main__":

    mc = Movie_chopper(VIDEO_PATH)


    selection = mc.select_video()

    mc.slap_chop(video=selection)
