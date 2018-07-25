if __name__ == '__main__':
    with open('result/knock92_85.txt', 'r') as data_in_85, open('result/knock92_90.txt') as data_in_90:
        count_85, count_90 = 0, 0
        for i, (line_85, line_90) in enumerate(zip(data_in_85, data_in_90)):
            if line_85.strip().split()[3] == line_85.strip().split()[4]:
                count_85 += 1
            if line_90.strip().split()[3] == line_90.strip().split()[4]:
                count_90 += 1
        print('knock85_result : {0:3d}/{1} ({2} %)'.format(count_85, i+1, count_85/(i+1) * 100))
        print('knock90_result : {0:3d}/{1} ({2} %)'.format(count_90, i+1, count_90/(i+1) * 100))
