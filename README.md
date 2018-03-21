# split_mp3
Split Mp3 file into smaller chunks.

## Usage

```
python split.py --min 20 --file ~/The_unsolved_mysteries_of_cream_cheese.mp3
```

## Setup

Requires [pydub](https://github.com/jiaaro/pydub) to be setup correctly. Something like this works on OSX:

```
# libav
brew install libav --with-libvorbis --with-sdl --with-theora

####    OR    #####

# ffmpeg
brew install ffmpeg --with-libvorbis --with-sdl2 --with-theora
```
