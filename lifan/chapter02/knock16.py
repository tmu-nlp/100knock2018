import argparse
from itertools import zip_longest

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='split lines', default=12, type=int)
args = parser.parse_args()

split_num = args.n
with open('hightemp.txt', 'r') as f:
	for file_no,string_turple in enumerate(zip_longest(*[iter(f.readlines())]*split_num)):
		with open("split_{}.txt".format(file_no), "w") as wf:
			for w_line in string_turple:
				if w_line is not None:
					wf.write(w_line)