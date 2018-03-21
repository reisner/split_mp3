import argparse
import math
from pydub import AudioSegment

parser = argparse.ArgumentParser()
parser.add_argument('--min',
                    type = int,
                    required = True,
                    help = 'minutes per chunk.')
parser.add_argument('--file',
                    type = argparse.FileType('r'),
                    required = True,
                    help = 'mp3 file to split.')

args = parser.parse_args()
min_per_chunk = args.min
input_file = args.file

print("Splitting into " + str(min_per_chunk) + " min chunks")

segment = AudioSegment.from_mp3(input_file)
segment_length_in_sec = len(segment)

print("Length of file: " + len(segment_length_in_sec))

sec_per_chunk = min_per_chunk * 60

num_chunks = math.ceil(segment_length_in_sec / float(sec_per_chunk))
#     return [audio_segment[i * chunk_length:(i + 1) * chunk_length]
#             for i in range(int(number_of_chunks))]

if num_chunks > 1:
    print("Splitting into " + num_chunks + " chunks.")
else:
    raise SystemExit('File is not long enough!')

#:45

# halfway_point = len(sound) // 2
# first_half = sound[:halfway_point]
#
# # create a new file "first_half.mp3":
# first_half.export("/path/to/first_half.mp3", format="mp3")
