import argparse
import math
from pydub import AudioSegment
import re

parser = argparse.ArgumentParser()
parser.add_argument('--min',
                    type = int,
                    required = True,
                    help = 'minutes per chunk.')
parser.add_argument('--file',
                    required = True,
                    help = 'mp3 file to split.')

args = parser.parse_args()
min_per_chunk = args.min
input_file = args.file
output_file_prefix = re.sub('\.mp3$', '', input_file) + "_"

print("Splitting into " + str(min_per_chunk) + " min chunks")
print("Reading: " + input_file)

segment = AudioSegment.from_mp3(input_file)
segment_length_in_sec = len(segment) / 1000

print("Length of file: " + str(segment_length_in_sec) + "sec")

sec_per_chunk = min_per_chunk #* 60
num_chunks = math.ceil(segment_length_in_sec / float(sec_per_chunk))

if num_chunks > 1:
    print("Splitting into " + str(num_chunks) + " chunks.")
    for i in range(int(num_chunks)):
        start = i * sec_per_chunk
        end = (i + 1) * sec_per_chunk
        chunk = segment[start * 1000 : end * 1000]
        output_file = output_file_prefix + "%03d" % (i + 1) + ".mp3"
        print("     ... Saving from " +
              str(start) + " to " + str(end) +
              " -> " + output_file)
        chunk.export(output_file, format = "mp3")
else:
    raise SystemExit('File is not long enough!')

print("Done!")
