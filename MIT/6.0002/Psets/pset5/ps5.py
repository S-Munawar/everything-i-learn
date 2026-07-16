# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match(r'(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    models = []
    for d in degs:
        model = pylab.polyfit(x, y, d)
        models.append(model)
        
    return models

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    # TODO
    sse = ((y - estimated)**2).sum()
    sst = ((y - y.mean())**2).sum()
    return 1 - sse / sst

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    # TODO
    for model in models:
        estYVals = pylab.polyval(model, x)
        rSquare = r_squared(y, estYVals)
        pylab.figure()
        pylab.plot(x, y, 'b:')
        pylab.plot(x, estYVals, 'r-')
        pylab.xlabel("Years")
        pylab.ylabel("Temperature (°C)")
        degree = len(model) - 1
        title = f"Degree = {degree}, R² = {rSquare:.4f}"
        if degree == 1:
            se = se_over_slope(x, y, estYVals, model)
            title = f"Degree = {degree}, R² = {rSquare:.4f} SE/Slope = {se:.4f}"
        pylab.title(title)
    
    pylab.show()

def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    # TODO
    national_yearly_avgs = []
    for year in years:
        cities_sum = 0
        for city in multi_cities:
            daily_temps = (climate.get_yearly_temp(city, year))
            city_avg = daily_temps.mean()
            cities_sum += city_avg
        national_yearly_avgs.append(cities_sum / len(multi_cities))
        
    national_yearly_avgs = pylab.array(national_yearly_avgs)
    return national_yearly_avgs

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    # TODO
    moving_avgs = []
    for i in range(len(y)):
        start = max(0, i - window_length + 1)
        curr = pylab.array(y[start:i+1])
        moving_avgs.append(curr.mean())
    
    moving_avgs = pylab.array(moving_avgs)
    return moving_avgs

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    # TODO
    return pylab.sqrt(((y - estimated)**2).mean())

def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    # TODO
    std_devs = []
    for year in years:
        city_daily_temps = [climate.get_yearly_temp(city, year) for city in multi_cities]

        # Compute each day's average across all cities, then std dev over days.
        daily_avgs = []
        for i in range(len(city_daily_temps[0])):
            daily_avgs.append(sum(city[i] for city in city_daily_temps) / len(multi_cities))
            
        std_devs.append(pylab.std(daily_avgs))
        
    std_devs = pylab.array(std_devs)
    return std_devs

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    # TODO
    for model in models:
        estYVals = pylab.polyval(model, x)
        rMSE = rmse(y, estYVals)
        pylab.figure()
        pylab.plot(x, y, 'b:')
        pylab.plot(x, estYVals, 'r-')
        pylab.xlabel("Years")
        pylab.ylabel("Temperature (°C)")
        degree = len(model) - 1
        title = f"Degree = {degree}, RMSE = {rMSE:.4f}"
        pylab.title(title)
    
    pylab.show()

if __name__ == '__main__':

    xVals = pylab.array(TRAINING_INTERVAL) 
    climate1 = Climate("data.csv")
    
    # Part A.4
    # TODO: replace this line with your code
    yVals = []
    for year in xVals:
        # yVals.append(climate1.get_daily_temp("NEW YORK", 1, 10, year))
        daily_temps = (climate1.get_yearly_temp("NEW YORK", year))
        yVals.append(daily_temps.mean())
    yVals = pylab.array(yVals)
    models = generate_models(xVals, yVals, [1, 2])
    evaluate_models_on_training(xVals, yVals, models)
    
    # Part B
    # TODO: replace this line with your code
    yVals = gen_cities_avg(climate1, CITIES, xVals)
    models = generate_models(xVals, yVals, [1, 2, 20])
    evaluate_models_on_training(xVals, yVals, models)
    
    # Part C
    # TODO: replace this line with your code
    yVals = moving_average(yVals, 5)
    models = generate_models(xVals, yVals, [1, 2, 20])
    evaluate_models_on_training(xVals, yVals, models)
    
    # Part D.2
    # TODO: replace this line with your code
    xVals = TESTING_INTERVAL
    test_yVals = gen_cities_avg(climate1, CITIES, xVals)
    test_yVals = moving_average(test_yVals, 5)
    evaluate_models_on_testing(xVals, test_yVals, models)
    
    # Part E
    # TODO: replace this line with your code
    stds = gen_std_devs(climate1, CITIES, TRAINING_INTERVAL)
    yVals = moving_average(stds, 5)
    models = generate_models(TRAINING_INTERVAL, yVals, [1, 2, 20])
    evaluate_models_on_training(TRAINING_INTERVAL, yVals, models)
