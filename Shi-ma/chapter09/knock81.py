if __name__ == '__main__':
    with open('result/knock81_result.txt', 'w') as data_out:
        countries = list(open('../data/countries.txt', 'r'))
        for line in open('result/knock80_result.txt', 'r'):
            for country in countries:
                line = line.strip().replace(country.strip(), country.strip().replace(' ', '_'))
            print(line, file=data_out)
