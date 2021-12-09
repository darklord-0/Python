# import csv

# # with open("data.csv" , "w") as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["name" , 'usn' , "department"])
# #     writer.writerow(["A" , 1 , "cse"])
# #     writer.writerow(["B" , 2 , "cse"])
# #     writer.writerow(["C" , 6 , "cse"])


# with open("data.csv") as file:
#     reader = csv.reader(file) 
#     # print(list(reader)) # to get all data in list form
#     for row in reader:
#         print(row)



import json
from pathlib import Path

# student = [
#     { "id": 1, "name" : "a" , "department" : "cse"},
#     { "id": 2, "name" : "b" , "department" : "ise"}
# ]
# data = json.dumps(student)
# Path('student.json').write_text(data)

data = Path('student.json').read_text()
student = json.loads(data)
print(student[1]["name"])

