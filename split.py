import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--min',
                    type = int,
                    required = True,
                    help = 'minutes per chunk.')

args = parser.parse_args()
min_per_chunk = args.min

print("Splitting into " + str(min_per_chunk) + " min chunks")
