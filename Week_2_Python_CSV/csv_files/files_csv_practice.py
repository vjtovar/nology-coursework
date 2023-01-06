import os
import os.path
import csv
import pandas as pd

example_dictionary = {'name': ["Rich", "Ash", "Ben", "Steph"], 'age':[35,26,37,26], }

df = pd.DataFrame(example_dictionary)
print(df)

df.to_csv("csv_example.csv", index = False)

new_df = pd.read_csv("csv_example")
print(new_df)

data = {
    'col1': [10,20, 30],
    'col2': ['A', 'B', 'c']
}

df = pd.DataFrame(data)
print(df.to_json())
df.to_json("example_json")



with open("myfile.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some text\nMore text\nEven more\nMOAR\n")

with open("myfile.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True: 
        line = my_file.readline()
        if not line:
            break
        print("Line # : ", line_num, " | ", line, end="")
        line_num += 1 
        print(len(line.split())) 


rows = []
with open('unitedStates.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    total = 0
    for row in csvreader:
        rows.append(row)   
        total += int(row[1])        
print(f"The headers are: {header}")
print(rows)
print(total)


header = ['State', 'Population', 'Capital']
data = [['California', '9600500', 'Sacramento'], ['Texas', '29700300', 'Austin'], ['Florida', '21900500', 'Tallahassee'], ['New York', '19900500', 'Albany'], ['Pennsylvania', '12800100', 'Harrisburg'], ['Illinois', '12500300', 'Sringfield'], ['Ohio', '11700600', 'Columbus'], ['Georgia', '10800000', 'Atlanta'], ['North Carolina', '10700000', 'Raleigh'], ['Michigan', '9900400', 'Lansing']]
with open('unitedStates.csv', mode = 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(header) 
    csvwriter.writerows(data)

