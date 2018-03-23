import argparse
import math
import pydub
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

#segment_length_in_ms = float(pydub.utils.mediainfo(input_file)['duration']) * 1000
#print("Length of file: " + str(segment_length_in_ms / (1000 * 60)) + "min")

segment = AudioSegment.from_mp3(input_file)
#segment.export("/output/file.wav", format="wav")

# segment_length_in_ms = len(segment) # This is not accurate with MP3s
ms_per_chunk = min_per_chunk * 60 * 1000
num_chunks = math.ceil(segment_length_in_ms / float(ms_per_chunk))

if num_chunks > 1:
    print("Splitting into " + str(num_chunks) + " chunks.")
    for i in range(int(num_chunks)):
        start = i * ms_per_chunk
        if (i != 0):
            # Start 10 seconds earlier
            start = start - 10000
        end = (i + 1) * ms_per_chunk
        chunk = segment[start : end].fade_in(3000)
        output_file = output_file_prefix + "%03d" % (i + 1) + ".mp3"
        print("     ... Saving from " +
              str(start) + " to " + str(end) +
              " -> " + output_file)
        chunk.export(output_file, format = "mp3")
else:
    raise SystemExit('File is not long enough!')

print("Done!")
