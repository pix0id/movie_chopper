import movie_chopper as chop
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", dest="length", default="1", help="Clip duration in minutes")
parser.add_argument("-n", "--num", dest="number_of_clips", default="1", help="Number of clips to create")
parser.add_argument("-p", "--path", dest="video_path", default="movies/", help="Movie Folder Path (Only have videos, no subdirectoies.")
parser.add_argument("-c", "--clips", dest="clip_path", default="movies/clips/", help="Folder for clip output")

args = parser.parse_args()

# Path variables
video_path = args.video_path
clip_path = args.clip_path

# Timing variables
length = int(args.length)
length_in_seconds = int(60*args.length)

# Logic variables
number_of_clips = int(args.number_of_clips)
movies = chop.get_movies(video_path)
touched_movies = []
count = 0

# TODO: while count is less than number_of_clips, run chop.clip_random_movie()
# TODO: After clipping is complete, merge all videos together into one file.
# TODO: Remove audio and replace it with ~*~V I B E S~*~ (vibes TBD)

print(movies)