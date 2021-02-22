#/usr/bin/python3
try:
    import argparse
    import pandas as pd
except:
    print('[Import error] Please run <pip3 install -r requirements.txt>')
    exit()

def parse_arg():
    parser = argparse.ArgumentParser(prog='calculate_price', usage='%(prog)s [-h] datafile.csv', description='Program to train a model to calculate the price of a car for a given milage.')
    parser.add_argument('datafile', help='the .csv file containing the data to train the model')
    args = parser.parse_args()
    return args

def read_csv(datafile):
    try:
        f = pd.read_csv(datafile)
        km = f['km']
        price = f['price']
        if len(km) == 0:
            km = []
        if len(price) == 0:
            price = []
        if len(km) != len(price):
            return [], []
        return km, price
    except:
        raise NameError('\n[Read error]\nWrong file format. Make sure you give an existing .csv file as argument.\n')

def calculate_price(mileage, tetha0, tetha1):
    try:
        estimated_price = tetha0 + (tetha1 * mileage)
        return estimated_price
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def calculate_loss(km, price, tetha0, tetha1):
    try:
        loss = 0
        for i in range(len(km)):
            predicted_price_i = calculate_price(km[i], tetha0, tetha1)
            diff_price = price[i] - predicted_price_i
            loss += diff_price ** 2
            i += 1
        loss /= len(km)
        return loss
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def main():
    try:
        args = parse_arg()
        km, price = read_csv(args.datafile)
        tetha0 = 0
        tetha1 = 0
        mean_km = sum(km) / len(km)
        mean_price = sum(price) / len(price)

        # accuracy = float('inf')
        # while accuracy > 1:

        #     tmp_tetha0 =
        # print(km)
        # print(price)
        print(calculate_loss(km, price, tetha0, tetha1))
        # mileage = get_mileage()
        # price = calculate_price(mileage, tetha0, tetha1)
        # display_price(price, mileage, tetha0, tetha1)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()