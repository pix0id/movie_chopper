# MOVIE_CHOPPER

Weekend hack script for a meme. Recruiters and potential employers, this is not the quality of my professional code.

Created using [MoviePy](https://zulko.github.io/moviepy/index.html)

## Steps:
1. Create a folder in the root directory called "movies" and the sub folder "movies/clips"
2. Create a python virtual environment `python -m venv venv`
3. Activate the virtual environment (`source venv/bin/activate` on Linux/macOS, `venv\Scripts\activate` on Windows)
3. Run `pip install moviepy`
4. Place all LEGALLY OBTAINED video files into a folder
5. Run the script and the movie magic will happen.


No longer need to add CLI arguments! Change settings in the settings.py file to augment your experience!!

## Moviepy codecs:
| Codec  | Extension | Description |
| ------------- | ------------- | ------------- |
| `libx264`  | `.mp4`  | makes well-compressed videos (quality tunable using ‘bitrate’).  |
| `mpeg4`  | `.mp4` | can be an alternative to `libx264`, and produces higher quality videos by default. | 
| `rawvideo`  | `.avi` | will produce a video of perfect quality, of possibly very huge size. |
| `png`  | `.avi` | will produce a video of perfect quality, of smaller size than with `rawvideo` |
| `libvorbis`  | `.ogv` | is a nice video format, which is completely free/ open source. |
| `libvpx`  | `.webm` | is tiny a video format well indicated for web videos (with HTML5). Open source. |

## TODO:

1. either clean out the clips folder or start clip file count at last index from clips folder (i.e. if you have 10 clips already, start at 11.).
2. add number counter/movie title to one of the corners.

