import csv
import json

def get_csv_data(csv_file_path):
    data = []
    with open (csv_file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({"id":row["id"],"request_payload":row["request_payload"],"expected_response":row["expected_response"]})
    
    return data



    

