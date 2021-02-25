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
    try:
        parser = argparse.ArgumentParser(prog='train.py', usage='%(prog)s [-h][-v {1,2}][-lr][-it][-plt][-cst] datafile.csv', description='Program to train a model to calculate the price of a car for a given milage.')
        parser.add_argument('datafile', help='.csv file containing the data to train the model')
        parser.add_argument('-v', '--verbose', help='increase output verbosity', type=int, default=0)
        parser.add_argument('-lr', '--learning_rate', help='[default = 0.01]', type=float, default=0.01)
        parser.add_argument('-it', '--iterations', help='[default = 1000]', type=int, default=1000)
        parser.add_argument('-plt', '--plot', help='dataset and linear regression', action='store_true')
        parser.add_argument('-cst', '--cost', help='cost function', action='store_true')
        args = parser.parse_args()
        return args
    except:
        raise NameError('\n[Input error]\nThere has been an error while parsing the arguments.\n')

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

def train_model(KM, price, verbose, learning_rate, number_iterations, cost):
    try:
        m = KM.shape[0]
        tetha0 = 0
        tetha1 = 0
        costs = []
        if verbose > 0:
            print('\n[ Trainig starting ]')
            print('Learning rate        : {:.4f}'.format(learning_rate).strip('0').strip('.'))
            print('Number of iterations : {}'.format(number_iterations))
        if verbose > 1:
            print('\n[ Tethas per iteration ]')
        for i in range(number_iterations):
            estimated_price = tetha0 + (KM * tetha1)
            loss = estimated_price - price
            tetha0 -= learning_rate * (1/m) * np.sum(loss)
            tetha1 -= learning_rate * (1/m) * np.sum(loss * KM)
            if verbose > 1 and i % 10 == 0:
                print('it: {}\t-> t0: {:.4f} || t1: {:.4f}'.format(i, tetha0, tetha1))
            if cost:
                costs.append(sum(loss ** 2) / m)
            i += 1
        return tetha0, tetha1, costs
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def save_parameters(tetha0, tetha1, km, verbose):
    try:
        km_mean = km.mean()
        km_std = km.std()
        parameters = {
            'tetha0': str(tetha0),
            'tetha1': str(tetha1),
            'km_mean': str(km_mean),
            'km_std': str(km_std)
        }
        outfile = open('linear_regression_parameters', 'wb')
        pickle.dump(parameters, outfile)
        outfile.close()
        if verbose > 0:
            print('\n[ Trainig finished ]')
            print('The model has been trained and the parameters have been saved correctly.')
            print('Tetha 0 : {:.5f}'.format(tetha0).strip('0').strip('.'))
            print('Tetha 1 : {:.5f}'.format(tetha1).strip('0').strip('.'))
            print('Km mean : {:.5f}'.format(km_mean).strip('0').strip('.') + ' km')
            print('Km std  : {:.5f}'.format(km_std).strip('0').strip('.'))
            print('\n[ Next step ]')
            print('\t<python calculate_price.py> to calculate the price of your vehicle according to the model.')
            print('\t<python read_parameters.py> to see the parameters calculated after training the model.\n')
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def plot_model(km, KM, price, tetha0, tetha1, learning_rate, number_iterations):
    try:
        plt.scatter(km, price, color='blue')
        estimated_price = tetha0 + (KM * tetha1)
        plt.plot(km, estimated_price, color='red')
        plt.xlabel('Mileage (km)')
        plt.ylabel('Price (€)')
        plt.legend(['LR model', 'Dataset'])
        plt.suptitle('Linear regression model')
        plt.title('Learning rate : {:.3f} || Number of iterations : {}'.format(learning_rate, number_iterations))
        plt.show()
    except:
        raise NameError('\n[Plot error]\nThere has been an error while plotting.\n')

def plot_cost(costs, number_iterations):
    try:
        plt.plot(range(number_iterations), costs)
        plt.xlabel('Number of iterations')
        plt.ylabel('Cost')
        plt.suptitle('Cost per iteration')
        plt.title('Final cost: {:.2f}'.format(costs[len(costs) - 1]))
        plt.show()
    except:
        raise NameError('\n[Plot error]\nThere has been an error while plotting.\n')

def main():
    try:
        args = parse_arg()
        km, price = read_csv(args.datafile)
        KM = normalize(km)
        tetha0, tetha1, costs = train_model(KM, price, args.verbose, args.learning_rate, args.iterations, args.cost)
        save_parameters(tetha0, tetha1, km, args.verbose)
        if args.plot:
            plot_model(km, KM, price, tetha0, tetha1, args.learning_rate, args.iterations)
        if args.cost:
            plot_cost(costs, args.iterations)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()