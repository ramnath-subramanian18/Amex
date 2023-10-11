import csv
def csv_write(file_name,data,operation):
    with open(file_name, mode=operation, newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
# csv_write("statement.csv",data,'a')