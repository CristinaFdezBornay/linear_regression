# WELCOME TO LINEAR REGRESSION

## SUMMARY
42 project where a moldel to predict a vehicle's price is trained using a given dataset.

The model is a linear regression trained following the descendent gradient algorithm.

### Used formulas

The formula used to estimate the price of the vehicle is: `estimated_price = tetha0 + tetha1 * km`.

Tetha0 is calculated as `tetha0 = learning_rate * (1/m) * sum(estimated_price - price)`.

Tetha1 is `tetha1 = learning_rate * (1/m) * sum((estimated_price - price) * km)`.

The cost is calculated as `cost = (1/m) * sum((estimated_price - price) ^ 2)`.

Tetha0 and tetha1 are updated on each iteration.

## HOW TO

### Set Up
```
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
source venv/bin/activate
```

### Calculate price
Run `python calculate_price.py`.

### Train model
Run `python train.py <dataset.csv>`.

**Arguments:**
Dataset mandatory to train the model. The other arguments are optional.
* datafile   -> csv file containing the dataset
* -h         -> display help information
* -v {1, 2}  -> verbosity level
* -lr        -> indicate the learning rate (default 0.01)
* -it        -> number of iterations to train the model (default 1000)
* -plt       -> plot the dataset and the model
* -cst       -> calculate and plot the cost function per iteration

### Read parameters
Run `python read_parameters.py`.

### Generate dataset
Run `python generate_datasets.py`.

**Arguments:**
All of them are optional.
* -h      -> display help information
* -dl     -> number of points in the dataset (default 100)
* -min    -> min mileage (default 0 km)
* -max    -> max mileage (default 200000 km)
* -err    -> desired error in the price output (default 15%)
* -t0     -> price of a new vehicle 0km (default 15000€)
* -t1     -> price lost per km (default 100€/km)
* -file   -> file name to save the generated dataset (default dataset)
* -plt    -> plot dataset and linear regression
* -v      -> increase output verbosity

## PROCESS

### Calculate price

1.  Retrieve the parameters calculated by the model saved on the file `linear_regression_parameters`
2.  If the parameters are not available will ask the user to train the model
3.  Otherwise, asks for the mileage of the vehicle
4.  Displays the estimated price of the vehicle and additional information (tetha0 and tetha1)

### Train model

1.  Parse the arguments
2.  Read the csv file to get the datapoints (km, price).
3.  Normalize the data
4.  Train the model to obtain the tetha0 and tetha1 (if `--cost` is passed as an argument)
5.  Save the parameters (tetha0, tetha1, km mean and std) using pickle
6.  Plot the dataset and the model (if `--plot` is passed as an argument)
7.  Plot the cost per iteration (if `--cost` is passed as an argument)

### Read parameters

1.  Retrieve the parameters calculated by the model saved on the file `linear_regression_parameters`
2.  Display the information (tetha0, tetha1, km mean and std)

### Generate dataset

1.  Parse the arguments
2.  Generate the km data by `(random(dataset_len) * (max_km - min_km)) + min_km`
3.  Normalize the KM
4.  Calculate the price for the generated km dataset for the given tetha0 and tetha1
5.  Generate the price data adding noise `noise = random(dataset_len) * error * price_range`
6.  Save the generated dataset into as the csv file
7.  Print the information (if `-v` is passed as an argument)
8.  Plot the dataset (if `--plot` is passed as an argument)

