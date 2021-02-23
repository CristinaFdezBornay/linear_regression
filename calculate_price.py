#/usr/bin/python3
try:
    import argparse
    import pandas as pd
    import pickle
except:
    raise NameError('[Import error] Please run <pip3 install -r requirements.txt>')

def get_information():
    try:
        infile = open('linear_regression_parameters', 'rb')
        information = pickle.load(infile)
        infile.close()
        tetha0 = float(information['tetha0'])
        tetha1 = float(information['tetha1'])
        km_mean = float(information['km_mean'])
        km_std = float(information['km_std'])
        infile.close()
        return tetha0, tetha1, km_mean, km_std
    except:
        raise NameError('\n[Read error]\nUnable to retrieve the tetha values.\n')

def get_km():
    try:
        km = input('\nPlease introduce the mileage(km): ')
        return float(km)
    except:
        raise NameError('\n[Input error]\nPlease introduce a valid number.\n')

def calculate_price(km, tetha0, tetha1, km_mean, km_std):
    try:
        KM = (km - km_mean) / km_std
        price = tetha0 + (tetha1 * KM)
        return price
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def display_price(price, km, tetha0, tetha1):
    try:
        print('\n=======================================================================\n')
        if price > 0:
            print('\t🚗 The estimated price for your vehicle is:  {:.2f}€ 🚗'.format(price))
        else:
            print('\t😿 I am very sorry but your vehicle is worthless 😿')
        print('\n=======================================================================\n')
        print()
        print('[ Info ]')
        print('Tetha 0 : {:.5f}'.format(tetha0).strip('0').strip('.'))
        print('Tetha 1 : {:.5f}'.format(tetha1).strip('0').strip('.'))
        print('Mileage : {:.5f}'.format(km).strip('0').strip('.') + ' km\n')
    except:
        raise NameError('\n[Display error]\nThere has been an error while displayind the information.\n')

def main():
    try:
        tetha0, tetha1, km_mean, km_std = get_information()
        km = get_km()
        price = calculate_price(km, tetha0, tetha1, km_mean, km_std)
        display_price(price, km, tetha0, tetha1)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()