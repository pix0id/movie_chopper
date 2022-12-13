from moviepy.editor import *
import os
import math
import random
try:
    from modules.settings import *
    from modules.utils import dir_check, get_video_files
except ImportError:
    from settings import *
    from utils import dir_check, get_video_files


class Movie_chopper():

    touched_movies = []
    count = 0

    def __init__(self, movies) -> None:
        self.movies = movies

    def get_name_text(self, file) -> str:
        file_name = os.path.basename(file).split('.')
        video_name = file_name[0].split('_')
        return video_name


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
                Movie_chopper.count += 1

                current_movie_file = VideoFileClip(current_movie)
                Movie_chopper.touched_movies.append(current_movie)
                movie_name = self.get_name_text(current_movie_file.filename)
                movie_length = math.floor(current_movie_file.duration)

                start_index = random.randint(0, movie_length - LENGTH)

                clip = current_movie_file.subclip(start_index, start_index + LENGTH)

                if UNIFORM_SIZE:
                    resized_clip = clip.resize(VIDEO_CLIP_SIZE)
                    resized_clip.write_videofile(f"{CLIP_PATH}{Movie_chopper.count}_{movie_name[0]}.mp4", codec=CODEC)
                else:
                    clip.write_videofile(f"{CLIP_PATH}{Movie_chopper.count}_{movie_name[0]}.mp4", codec=CODEC)

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


    def slap_chop(self, video) -> None:
        name = self.get_name_text(video)
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


if __name__ == "__main__":

    mc = Movie_chopper(VIDEO_PATH)


    selection = mc.select_video()

    mc.slap_chop(video=selection)
