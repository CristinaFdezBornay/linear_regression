#/usr/bin/python3
try:
    import argparse
    import pandas as pd
    import pickle
except:
    print('[Import error] Please run <pip3 install -r requirements.txt>')
    exit()

def get_tethas():
    try:
        infile = open('tethas', 'rb')
        tethas_dict = pickle.load(infile)
        infile.close()
        tetha0 = float(tethas_dict['tetha0'])
        tetha1 = float(tethas_dict['tetha1'])
        return tetha0, tetha1
    except:
        raise NameError('\n[Read error]\nUnable to retrieve the tetha values.\n')

def get_mileage():
    try:
        mileage = input('\nPlease introduce the mileage(km): ')
        return float(mileage)
    except:
        raise NameError('\n[Input error]\nPlease introduce a valid number.\n')

def calculate_price(mileage, tetha0, tetha1):
    try:
        price = tetha0 + (tetha1 * mileage)
        return price
    except:
        raise NameError('\n[Process error]\nThere has been an error while processing the information.\n')

def display_price(price, mileage, tetha0, tetha1):
    try:
        print('\n=====================================================================\n')
        print('\tThe estimated price for your vehicle is:  {:.2f}€'.format(price))
        print('\n=====================================================================\n')
        print()
        print('[ Info ]')
        print('Tetha 0 : {:.5f}'.format(tetha0).strip('0').strip('.'))
        print('Tetha 1 : {:.5f}'.format(tetha1).strip('0').strip('.'))
        print('Mileage : {:.5f}'.format(mileage).strip('0').strip('.') + ' km')
    except:
        raise NameError('\n[Display error]\nThere has been an error while displayind the information.\n')

def main():
    try:
        tetha0, tetha1 = get_tethas()
        mileage = get_mileage()
        price = calculate_price(mileage, tetha0, tetha1)
        display_price(price, mileage, tetha0, tetha1)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()