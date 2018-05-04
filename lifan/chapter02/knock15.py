import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='last lines', default=1, type=int)
args = parser.parse_args()

with open('hightemp.txt', 'r') as f:
	file_list = f.readlines()
	last_index = len(file_list) - args.n
	for line in file_list[last_index:]:
		print(line.strip())