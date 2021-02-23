#/usr/bin/python3
try:
    import argparse
    import pandas as pd
    import numpy as np
    import pickle
    import matplotlib.pyplot as plt
except:
    raise NameError('[Import error] Please run <pip3 install -r requirements.txt>')

def parse_arg():
    parser = argparse.ArgumentParser(prog='train', usage='%(prog)s [-h] [-v] [-lr] [-it] datafile.csv', description='Program to train a model to calculate the price of a car for a given milage.')
    parser.add_argument('datafile', help='.csv file containing the data to train the model')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
    parser.add_argument('-lr', '--learning_rate', help='[default = 0.01]', type=float, default=0.01)
    parser.add_argument('-it', '--iterations', help='[default = 1000]', type=int, default=1000)
    args = parser.parse_args()
    return args

def read_csv(datafile):
    try:
        f = pd.read_csv(datafile)
        km = np.array(f.get('km'))
        price = np.array(f.get('price'))
        return km, price
    except:
        raise NameError('\n[Read error]\nWrong file format. Make sure you give an existing .csv file as argument.\n')

def normalize(X):
    try:
        Xnorm = (X - X.mean()) / X.std()
        return Xnorm
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def train_model(KM, price, verbose, learning_rate, number_iterations):
    try:
        m = KM.shape[0]
        tetha0 = 0
        tetha1 = 0
        # cost = []  NOT DONE
        if verbose:
            print('\n[ Trainig starting ]')
            print('Learning rate        : {:.4f}'.format(learning_rate).strip('0').strip('.'))
            print('Number of iterations : {}'.format(number_iterations))
            print('\n[ Tethas per iteration ]')
        for i in range(number_iterations):
            estimated_price = tetha0 + (KM * tetha1)
            loss = estimated_price - price
            tetha0_gradient = (1/m) * np.sum(loss)
            tetha1_gradient = (1/m) * np.sum(loss * KM)
            tetha0 -= learning_rate * tetha0_gradient
            tetha1 -= learning_rate * tetha1_gradient
            if verbose and i % 10 == 0:
                print('it: {}\t-> t0: {:.4f} || t1: {:.4f}'.format(i, tetha0, tetha1))
            i += 1
        return tetha0, tetha1
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def save_information(tetha0, tetha1, km, verbose):
    try:
        km_mean = km.mean()
        km_std = km.std()
        information = {
            'tetha0': str(tetha0),
            'tetha1': str(tetha1),
            'km_mean': str(km_mean),
            'km_std': str(km_std)
        }
        outfile = open('linear_regression_parameters', 'wb')
        pickle.dump(information, outfile)
        outfile.close()
        if verbose:
            print('\n[ Trainig finished ]')
            print('The model has been trained and the parameters has been saved correctly.')
            print('\n[ Next step ]')
            print('\t<python calculate_price.py> to calculate the price of your vehicle according to the model.')
            print('\t<python read_parameters.py> to see the parameters calculated after training the model.')
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def main():
    try:
        verbose = False
        args = parse_arg()
        if args.verbose:
            verbose = True
        km, price = read_csv(args.datafile)
        KM = normalize(km)
        tetha0, tetha1 = train_model(KM, price, verbose, args.learning_rate, args.iterations)
        save_information(tetha0, tetha1, km, verbose)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()