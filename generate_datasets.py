#/usr/bin/python3
try:
    import argparse
    import pandas as pd
    from numpy import random
    import csv
    import matplotlib.pyplot as plt
except:
    raise NameError('[Import error] Please run <pip3 install -r requirements.txt>')

def parse_arg():
    try:
        parser = argparse.ArgumentParser(prog='train', usage='%(prog)s [-h][-nb][-min][-max][-t0][-t1][-plt]', description='Program to train a model to calculate the price of a car for a given milage.')
        parser.add_argument('-dslen', '--dataset_lenght', help='[default = 100]', type=int, default=100)
        parser.add_argument('-min', help='min mileage [default = 0 km]', type=int, default=0)
        parser.add_argument('-max', help='max mileage [default = 200000 km]', type=float, default=200000)
        parser.add_argument('-err', help='desired error in the price output [default = 15%]', type=float, default=0.15)
        parser.add_argument('-t0', '--tetha0', help='price of a new vehicle (0km) [default = 15000 €]', type=float, default=15000)
        parser.add_argument('-t1', '--tetha1', help='price lost per km [default = 100 €/km]', type=float, default=100)
        parser.add_argument('-fl', '--file', help='file name to save the generated dataset', type=str, default='dataset')
        parser.add_argument('-plt', '--plot', help='dataset and linear regression', action='store_true')
        args = parser.parse_args()
        return args
    except:
        raise NameError('\n[Input error]\nThere has been an error while parsing the arguments.\n')

def get_km_for_dataset(dslen, max, min):
    try:
        km = (random.rand(dslen) * (max - min)) + min
        KM = (km - km.mean()) / km.std()
        return KM, km
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def get_price_for_dataset(dslen, KM, err, tetha0, tetha1):
    try:
        price = tetha0 + (KM * tetha1)
        price_range = price.max() - price.min()
        noise = random.rand(dslen)
        price_noise = (noise - noise.mean()) * (err * price_range)
        price += price_noise
        return price
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def generate_dataset(dslen, KM, price, filename):
    try:
        with open(filename, 'w') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(['km', 'price'])
            for i in range(dslen):
                spamwriter.writerow([KM[i], price[i]])
                i += 1
    except:
        raise NameError('\n[Process error]\nThere has been an error while saving the dataset.\n')

def plot_dataset(km, price):
    try:
        plt.scatter(km, price, color='blue')
        plt.xlabel('Mileage (km)')
        plt.ylabel('Price (€)')
        plt.title('Generated dataset')
        plt.show()
    except:
        raise NameError('\n[Plot error]\nThere has been an error while plotting.\n')

def main():
    try:
        args = parse_arg()
        KM, km = get_km_for_dataset(args.dataset_lenght, args.min, args.max)
        price = get_price_for_dataset(args.dataset_lenght, KM, args.err, args.tetha0, args.tetha1)
        filename = 'Dataset/{}.csv'.format(args.file)
        generate_dataset(args.dataset_lenght, km, price, filename)
        if args.plot:
            plot_dataset(km, price)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()