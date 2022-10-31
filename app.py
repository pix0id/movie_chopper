import os
# import movie_chopper as mc
# import franken_movie as fm
import settings

count = 0

# get movies list
# movies = movie_chopper.get_video_files(video_path=settings.video_path)


# Create clips
# while count < settings.number_of_clips:
#     mc.clip_random_movie(movies)

# add titles to clips
# mc.title_clips()

# F R A N K E N M O V I E
# fm.concat_clips(clips_folder=settings.clip_path)

def list_files(path, filetype):
    paths=[]
    directories=[]

    for root, dirs, files in os.walk(path):
        for _dir in dirs:
            directories.append(_dir)
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root,file))

    return directories

print(list_files("testing/", ".txt"))