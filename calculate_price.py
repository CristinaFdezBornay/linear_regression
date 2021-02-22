#/usr/bin/python3
try:
    import argparse
    import pandas as pd
except:
    print('[Import error] Please run <pip3 install -r requirements.txt>')
    exit()

def parse_arg():
    parser = argparse.ArgumentParser(prog='calculate_price', usage='%(prog)s [-h] tetha.csv', description='Program to calculate the price of a car for a given milage.')
    parser.add_argument('tethas', help='the .csv file containing the tethas')
    args = parser.parse_args()
    return args

def read_csv(datafile):
    try:
        f = pd.read_csv(datafile)
        tetha0 = f['tetha0'].unique()
        tetha1 = f['tetha1'].unique()
        if len(tetha0) != 1:
            tetha0 = 0
        if len(tetha1) != 1:
            tetha1 = 0
        return tetha0, tetha1
    except:
        raise NameError('\n[Read error]\nWrong file format. Make sure you give an existing .csv file as argument.\n')

def get_mileage():
    try:
        mileage = input('\nPlease introduce the mileage(km): ')
        return float(mileage)
    except:
        raise NameError('\n[Input error]\nPlease introduce a valid number.\n')

def calculate_price(mileage, tetha0, tetha1):
    try:
        estimated_price = tetha0 + (tetha1 * mileage)
        return estimated_price
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def display_price(price, mileage, tetha0, tetha1):
    print('\n=====================================================================\n')
    print('\tThe estimated price for your vehicle is:  {:.2f}€'.format(price))
    print('\n=====================================================================\n')
    print()
    print('[ Info ]')
    print('Tetha 0 : {:.5f}'.format(tetha0).strip('0').strip('.'))
    print('Tetha 1 : {:.5f}'.format(tetha1).strip('0').strip('.'))
    print('Mileage : {:.5f}'.format(mileage).strip('0').strip('.'))

def main():
    try:
        args = parse_arg()
        tetha0, tetha1 = read_csv(args.tethas)
        mileage = get_mileage()
        price = calculate_price(mileage, tetha0, tetha1)
        display_price(price, mileage, tetha0, tetha1)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()