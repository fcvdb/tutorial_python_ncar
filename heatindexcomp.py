#------------------------------------------------------------------------------#
# NCAR Python Tutorial 2020
#
# See tutorial https://ncar.github.io/python-tutorial/tutorials/yourfirst.html
#------------------------------------------------------------------------------#
#
from mysci.printing import print_comparison
from mysci.readdata import read_data
from mysci.computation import compute_heatindex

# Read the data file

filename = "data/wxobs20170821.txt"

# Column names and column indices to read
#columns = {'date':0,'time':1,'tempout':2, 'windspeed':7, 'windchill':12}
columns = {'date':0,'time':1,'tempout':2, 'humout':5, 'heatindex':13}

# Data types for each column (only if non-string)
types = {'tempout': float, 'humout':float, 'heatindex':float}

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

# DEBUG
#print(data['tempout'])
#for i, j in zip([1, 2], [3, 4, 5]):
#    print(i, j)

#------------------------------------------------------------------------------#
# Compute the heart index
#------------------------------------------------------------------------------#

#def compute_heatindex(t,hum):

#    a = -42.379
#    b = 2.04901523
#    c = 10.14333127
#    d = 0.22475541
#    e = 0.00683783
#    f = 0.05481717
#    g = 0.00122874
#    h = 0.00085282
#    i = 0.00000199

#    rh = hum / 100

#    hi = a + (b * t) + (c * rh) + (d * t * rh) + (e * t**2) + (f * rh**2) + (g * t**2 * rh) + (h * t * rh**2) + (i * t**2 * rh**2)

#    return hi

# windchill
#   a = 35.74
#   b = 0.6215
#   c = 35.75
#   d = 0.4275
#   v16 = v ** 0.16
#   wci = a + (b * t) - (c * v16) + (d * t * v16)
#   return wci

#------------------------------------------------------------------------------#
# Running the function to compute hi
#------------------------------------------------------------------------------#

#heatindex = []
#for temp, humout in zip (data['tempout'], data['humout']):
#    heatindex.append(compute_heatindex(temp, humout))

heatindex = [compute_heatindex(t, w) for t, w in zip(data['tempout'], data['humout'])]

#print(heatindex)

# DEBUG
#for hi_data, hi_comp in zip(data['heatindex'], heatindex):
#    print(f'{hi_data:.5f} {hi_comp:.5f} {hi_data - hi_comp:.5f}')

print_comparison("HEATINDEX",data['date'], data['time'], data['heatindex'] , heatindex)
#------------------------------------------------------------------------------#
# Output comparison of data
#zip_data = zip(data['date'], data['time'], data['heatindex'] , heatindex)

#print('                ORIGINAL  COMPUTED')
#print(' DATE    TIME  HEATINDEX HEATINDEX DIFFERENCE')
#print('------- ------ --------- --------- ----------')
#for date, time, hi_orig, hi_comp in zip_data:
#    hi_diff = hi_orig - hi_comp
#    print(f'{date} {time:>6} {hi_orig:9.6f} {hi_comp:9.6f} {hi_diff:10.6f}')
#------------------------------------------------------------------------------#


