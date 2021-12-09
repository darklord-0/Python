

# people = {
#     "name" : "john",
#     "age" : 12,
#     "gender" : "male"
# }
# people["gender"] = 'female'
# print(people["gender"])
# print(people.get("Age",19)) # gives o/p even if no 'Age' key present 'None'(means absence of values) 
#                             # when default value not specified  



phone = input("enter : ")
phone_dict = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output = ""
for i in phone:
    output += phone_dict.get(i , "*" ) + " "
print(output)


msg = input(">>> ")
words = msg.split(' ')
emojis = {
    ":)" : "😃",
    ":(" : "😔"
}
output = ""
for word in words:
    output += emojis.get(word , word) + " "
print(output) 
print(words)




