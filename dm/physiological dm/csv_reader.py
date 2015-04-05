import csv
import os

def read_csv(filename):
    
    dir_path = os.getcwd()
    path = dir_path +"\\"+filename
    
    csv_file = open(path,'rU')
    reader = csv.reader(csv_file,delimiter=',')

    data = []
    for i in reader:
        data.append(i)
    csv_file.close()
    return data
    
