import csv
from .clear_data import clear_list_of_list_data 
import sqlite3 
import pandas as pd 

def create_json_file(result):
    import json 
    with open("output/file.json", "w") as outfile: 
        json.dump(result, outfile, indent=4)

def create_csv_file(list_to_write:list):
    with open('output/result.csv', 'w') as csvfile:
        header = ['id','track_name', 'size_bytes', 'price','rating_count_tot', 'prime_genre']
        csv.writer(csvfile, delimiter=',').writerow(header)
        for element in list_to_write:
            csv.writer(csvfile, delimiter=',').writerow(clear_list_of_list_data(element) )

def create_sqlite3_file():
    conn = sqlite3.connect(r'output/db_results.sqlite3') 
    stud_data = pd.read_csv('output/result.csv') 
    stud_data.to_sql('results', conn, if_exists='replace', index=False) 
    conn.close() 

