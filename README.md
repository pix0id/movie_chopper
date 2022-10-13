# MOVIE_CHOPPER

Script built very quickly for a meme.

## Steps:
1. Create a folder in the root directory called "movies" and the sub folder "movies/clips"
2. Create a python virtual environment `python -m venv venv`
3. Activate the virtual environment (`source venv/bin/activate` on Linux/macOS, `venv\\Scripts\\activate` on Windows)
3. Run `pip install moviepy`
4. Place all LEGALLY OBTAINED video files in the folder "movies"
5. Run the script and the movie magic will happen.


## TODO:
1. Add ability to specify length of clips (HIGH PRIORITY)
2. Automatically get proper file format and use proper codec (HIGH PRIORITY)
3. Add video file name to clip file name. (LOW PRIORITY)
4. Create clips shorter than specified time if final clip is shorter than provided time. (LOW PRIORITY)
