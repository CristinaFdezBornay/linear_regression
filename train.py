#/usr/bin/python3
try:
    import argparse
    import pandas as pd
    import numpy as np
    import pickle
    import matplotlib.pyplot as plt
except:
    print('[Import error] Please run <pip3 install -r requirements.txt>')
    exit()

def parse_arg():
    parser = argparse.ArgumentParser(prog='train', usage='%(prog)s [-h] datafile.csv', description='Program to train a model to calculate the price of a car for a given milage.')
    parser.add_argument('datafile', help='the .csv file containing the data to train the model')
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

def train_model(KM, PRICE):

        N = KM.shape[0]
        tetha0 = 0
        tetha1 = 0
        learning_rate = 0.1
        number_iterations = 100

        for i in range(number_iterations):
            estimated_price = tetha0 + (KM * tetha1)
            print(estimated_price)
            print(PRICE)
            loss = estimated_price - PRICE
            print(loss)
            print('loss      : {}'.format(np.sum(loss)))
            print('loss * KM : {}'.format(np.sum(loss * KM)))
            tetha0_gradient = (2/N) * np.sum(loss)
            tetha1_gradient = (2/N) * np.sum(loss * KM)
            print('tetha0_g : {}'.format(tetha0_gradient))
            print('tetha1_g : {}'.format(tetha1_gradient))
            tetha0 = tetha0 - (learning_rate * tetha0_gradient)
            tetha1 = tetha1 - (learning_rate * tetha1_gradient)
            print('tetha0 : {}'.format(tetha0))
            print('tetha1 : {}'.format(tetha1))
            print('tetha0: {:.5f} || tetha1: {:.5f}'.format(tetha0, tetha1))        
            i += 1

        tethas = { 'tetha0': str(tetha0), 'tetha1': str(tetha1) }
        return tethas

def save_tethas(tethas):
    try:
        outfile = open('tethas', 'wb')
        pickle.dump(tethas, outfile)
        outfile.close()
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def main():
    try:
        args = parse_arg()
        km, price = read_csv(args.datafile)
        KM = normalize(km)
        PRICE = normalize(price)
        tethas = train_model(KM, PRICE)
        save_tethas(tethas)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()