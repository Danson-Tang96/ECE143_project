import os
import csv

def read_data(fname, ENCODE="utf8"):
    '''
    read data from csv file
    input: file name in path, encoding of string
    output: a dictionary of data, keys are categories and values are data
    '''
    
    assert os.path.isfile(fname), "file doesn't exit in given path"
    
    with open(fname, 'r', encoding=ENCODE) as temp_file:
        csvreader = csv.DictReader(temp_file)
        out = dict()
        f_row = next(csvreader)
        
        for key in f_row.keys():
            out[key] = []
            out[key].append(f_row[key])
            
        for row in csvreader:
            for key in row.keys():
                out[key].append(row[key])
                
        return out


if __name__ == '__main__':
    pass

