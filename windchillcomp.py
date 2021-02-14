#------------------------------------------------------------------------------#
# NCAR Python Tutorial 2020
#
# See tutorial https://ncar.github.io/python-tutorial/tutorials/yourfirst.html
#------------------------------------------------------------------------------#
#
from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_windchill

# Read the data file

filename = "data/wxobs20170821.txt"

# Column names and column indices to read
columns = {'date':0,'time':1,'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed':float, 'windchill':float}

data = read_data(columns, types=types)
#------------------------------------------------------------------------------#
# Initialize my data variable
#data = {}

#for column in columns:
#    data[column] = []

#with open(filename,'r') as datafile:

    # read the first three lines (header)
#    for _ in range(3):
#        print(_)
#        headerline = datafile.readline()
#        print(headerline)

    # Read and parse the rest of the file 
#    for line in datafile:
#        split_line = line.split() # (','),('/t') 
#        for column in columns:
#            i = columns[column]
#            t = types.get(column, str)
#            value = t(split_line[i])
#            data[column].append(value)
#------------------------------------------------------------------------------#

# DEBUG
#print(data['tempout'])
#for i, j in zip([1, 2], [3, 4, 5]):
#    print(i, j)

#------------------------------------------------------------------------------#
# Compute the wind chill temperature
#------------------------------------------------------------------------------#

#def compute_windchill(t,v):
#
#    a = 35.74
#    b = 0.6215
#    c = 35.75
#    d = 0.4275

#    v16 = v ** 0.16

#    wci = a + (b * t) - (c * v16) + (d * t * v16)

#    return wci

#------------------------------------------------------------------------------#
# Running the function to compute wci
#------------------------------------------------------------------------------#

#windchill = []
#for temp, windspeed in zip (data['tempout'], data['windspeed']):
#    windchill.append(compute_windchill(temp, windspeed))

windchill = [compute_windchill(t, w) for t, w in zip(data['tempout'], data['windspeed'])]

#print(windchill)

# DEBUG
#for wc_data, wc_comp in zip(data['windchill'], windchill):
#    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

print_comparison("WINDCHILL",data['date'], data['time'], data['windchill'], windchill)
#------------------------------------------------------------------------------#
# Output comparison of data
#zip_data = zip(data['date'], data['time'], data['windchill'] , windchill)

#print('                ORIGINAL  COMPUTED')
#print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
#print('------- ------ --------- --------- ----------')
#for date, time, wc_orig, wc_comp in zip_data:
#    wc_diff = wc_orig - wc_comp
#    print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')
#------------------------------------------------------------------------------#


