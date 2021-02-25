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
        parser = argparse.ArgumentParser(prog='generate_datasets.py', usage='%(prog)s [-h][-dl][-min][-max][-err][-t0][-t1][-file][-plt][-v]', description='Program to generate a dataset to train the linear regression model.')
        parser.add_argument('-dl', '--dataset_len',help='number of points in the dataset [default = 100]', type=int, default=100)
        parser.add_argument('-min', help='min mileage [default = 0 km]', type=int, default=0)
        parser.add_argument('-max', help='max mileage [default = 200000 km]', type=float, default=200000)
        parser.add_argument('-err', help='desired error in the price output [default = 15%]', type=float, default=15)
        parser.add_argument('-t0', '--tetha0', help='price of a new vehicle (0km) [default = 15000 €]', type=float, default=15000)
        parser.add_argument('-t1', '--tetha1', help='price lost per km [default = 100 €/km]', type=float, default=100)
        parser.add_argument('-file', help='file name to save the generated dataset', type=str, default='dataset')
        parser.add_argument('-plt', '--plot', help='dataset and linear regression', action='store_true')
        parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
        args = parser.parse_args()
        return args
    except:
        raise NameError('\n[Input error]\nThere has been an error while parsing the arguments.\n')

def generate_km_for_dataset(dataset_len, max, min):
    try:
        km = (random.rand(dataset_len) * (max - min)) + min
        KM = (km - km.mean()) / km.std()
        return KM, km
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def generate_price_for_dataset(dataset_len, KM, err, tetha0, tetha1):
    try:
        err /= 100
        price = tetha0 + (KM * tetha1)
        price_range = price.max() - price.min()
        noise = random.rand(dataset_len)
        price_noise = (noise - noise.mean()) * (err * price_range)
        price += price_noise
        return price
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def generate_dataset(dataset_len, KM, price, filename):
    try:
        with open(filename, 'w') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(['km', 'price'])
            for i in range(dataset_len):
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

def display_information(dataset_len, max, min, err, tetha0, tetha1, km, filename):
    try:
        print('\n[ Dataset generated ]\nSaved into {}\n'.format(filename))
        print('Number of data   : {}'.format(dataset_len))
        print('Min mileage      : {}'.format(min))
        print('Max mileage      : {}'.format(max))
        print('Price variation  : {}%'.format(err))
        print('Tetha 0          : {:.5f}'.format(tetha0).strip('0').strip('.'))
        print('Tetha 1          : {:.5f}'.format(tetha1).strip('0').strip('.'))
        print('KM mean          : {:.5f}'.format(km.mean()).strip('0').strip('.'))
        print('KM std           : {:.5f}'.format(km.std()).strip('0').strip('.'))
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def main():
    try:
        args = parse_arg()
        KM, km = generate_km_for_dataset(args.dataset_len, args.min, args.max)
        price = generate_price_for_dataset(args.dataset_len, KM, args.err, args.tetha0, args.tetha1)
        filename = 'Dataset/{}.csv'.format(args.file)
        generate_dataset(args.dataset_len, km, price, filename)
        if args.verbose:
            display_information(args.dataset_len, args.min, args.max, args.err, args.tetha0, args.tetha1, km, filename)
        if args.plot:
            plot_dataset(km, price)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()