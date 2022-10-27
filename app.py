import movie_chopper
import franken_movie

with open("settings.json") as settings:
    settings = json.load(settings)

count = 0

# get movies list
movies = movie_chopper.get_video_files(video_path=settings["video_path"])


# Create clips
while count < settings["number_of_clips"]:
    movie_chopper.clip_random_movie(movies)

# add titles to clips
# movie_chopper.title_clips()

# F R A N K E N M O V I E
franken_movie.concat_clips(clips_folder=clip_path)