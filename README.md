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


## Command line arguments:
| Short Arg  | Long Arg | Default | Description |
| ------------- | ------------- | ------------- | ------------- |
| -l  | --length  | 1 (int only) | Clip duration in whole minutes |
| -n  | --num | 1 (int) | Number of clips to create |
| -p  | --path | "movies/" | Movie Folder Path |
| -c  | --clips | "movies/clips" | Folder for clip output |

_cli arguments will be made invalid in future update!_

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
1. Add support for choosing codec
2. Add support for files in sub-directories
4. either clean out the clips folder or start clip file count at last index from clips folder (i.e. if you have 10 clips already, start at 11.).
5. add number counter/movie title to one of the corners.

