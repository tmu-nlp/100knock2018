import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='head lines', default=1, type=int)
args = parser.parse_args()

with open('hightemp.txt', 'r') as f:
	for line in f.readlines()[:args.n]:
		print(line.strip())