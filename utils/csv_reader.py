import csv
import random
class csvreader:
    @staticmethod
    def get_row(filepath,rows=None,random_rows=False):
        with open(filepath,newline='',encoding='utf-8')as csvfile:
            data=list(csv.DictReader(csvfile))
        if random_rows:
            return random.choice(data)  
        if rows is None:
            return data
        if isinstance(rows,int):
            return data[rows]
        if isinstance(rows,list):
            return [data[i]for i in rows]
           


        