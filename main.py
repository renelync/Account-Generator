# student_names = ["Jesse Katsopolis", "Danny Tanner", "Joey Gladstone", "Stephanie Tanner", "Kimberlina Gibbler"]

student_names = []

def create_names():
  count = 1
  while count <= 5:
    name = input("Enter student name, please. ")
    student_names.append(name)
    count += 1 
create_names()

import random

student_ids = []

# #fx to generate random Student IDs
def create_ids():
  student_id = random.randint(111111,999999)
  return student_id

# def create_ids():
#   list = []
#   for i in range(5):
#     student_id = random.randint(111111,999999)
#     if student_id not in list:
#       return student_id  
# #fx to place randomized student IDs into my student IDs list

def create_id_list():
  for name in student_names:
    student_ids.append(create_ids())
# #calling the fx to get student IDs.    
create_id_list()

# print(student_ids)

student_emails = []

def create_emails():
  for name in student_names:
    # splitting the student names
    first_last = name.split(" ")
    #first, middle, last = name.split()
    # converting student IDs to a string while also indexing each name in student names - in other words, finding it's position w/in the list.
    sid = str(student_ids[student_names.index(name)])
    len_sid = len(sid)
    # len_sid-3;len_sid = drops the first 3 characters, and print from that point to the end
    last_three_sid = sid[len_sid-3:len_sid]
    #adding the first letter of the first name + the last name + the last 3 SID digits to the student emails list.
    student_emails.append(first_last[0][0] + first_last[1] + last_three_sid + "@gmail.com") #ignores last index if one is provided.


create_emails()
# print(student_emails)

def student_info():
  for name in student_names:
    name_pos = student_names.index(name)
    print("\n" + "name: " + name)
    print("id: " + str(student_ids[name_pos]))
    print("email: " + student_emails[name_pos])
student_info()
