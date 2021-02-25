#/usr/bin/python3
try:
    import argparse
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
        raise NameError('\n[Read error]\nUnable to retrieve the information.\n')

def display_information(tetha0, tetha1, km_mean, km_std):
    try:
        print('\n[ Info ]\n')
        print('Tetha 0 : {:.5f}'.format(tetha0).strip('0').strip('.'))
        print('Tetha 1 : {:.5f}\n'.format(tetha1).strip('0').strip('.'))
        print('Km mean : {:.5f}'.format(km_mean).strip('0').strip('.') + ' km')
        print('Km std  : {:.5f}'.format(km_std).strip('0').strip('.'))
        print()
    except:
        raise NameError('\n[Display error]\nThere has been an error while displayind the information.\n')

def main():
    try:
        tetha0, tetha1, km_mean, km_std = get_information()
        display_information(tetha0, tetha1, km_mean, km_std)
    except NameError as e:
        print(e)

if __name__ == '__main__':
    main()