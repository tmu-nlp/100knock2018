def spearman(n, sum_diff):
  return 1 - (6 * sum_diff) / float(n ** 3 - n)

def sim_diff(sim1, sim2):
  return (sim1 - sim2) ** 2
  
def main():
  sum_diff = 0
  line_count = 0
  with open("knock94.txt", "r") as fin:
    for line in fin:
      line = line.strip().split(",")
      sum_diff += sim_diff(float(line[2]), float(line[3]))
      line_count += 1
    print(spearman(line_count, sum_diff))

if __name__ == '__main__':
  main()