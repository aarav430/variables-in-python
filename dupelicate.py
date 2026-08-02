students = {

101: {"name": "Alice", "class": 9, "subject": "Math"},

102: {"name": "Bob", "class": 9, "subject": "Science"},

103: {"name": "Charlie", "class": 9, "subject": "English"},

102: {"name": "Bob", "class": 9, "subject": "Science"}

}
print("unique student records")
for key, value in students.items():
    print(key, ":" , value )