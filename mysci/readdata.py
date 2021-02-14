def read_data(columns, types={}, filename="data/wxobs20170821.txt"):
    """
    Read data from CU Boulder Weather Station data file
    Parameters:
        columns: A dictionary of column names mapping the column indices
        types: A dictionnary of column names mappinf the type to which to convert each column 
        filename: A string pointing to CU Boulder Weather Station data file

    """
    # Initialize my data variable
    data = {}
    
    for column in columns:
        data[column] = []
    
    with open(filename,'r') as datafile:
    
        # read the first three lines (header)
        for _ in range(3):
            print(_)
            headerline = datafile.readline()
            print(headerline)
    
        # Read and parse the rest of the file 
        for line in datafile:
            split_line = line.split() # (','),('/t') 
            for column in columns:
                i = columns[column]
                t = types.get(column, str)
                value = t(split_line[i])
                data[column].append(value)
    return(data) 
