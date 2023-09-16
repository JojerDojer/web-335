#-------------------------------------------------------
#  Title: davidson_usersp1.py
#  Author: John Davidson
#  Date: 16 September 2023
#  Description: Exercise 6.3 for WEB 335 - Intro to NoSQL.
#-------------------------------------------------------

# Import the MongoClient.
from pymongo import MongoClient

# Build a connection string to connect to web335DB.
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.feyswh3.mongodb.net/web335DBretryWrites=true&w=majority")

# Configure a variable to access web335DB database.
db = client['web335DB']

print('Here is a list of every document in the users collection:')
# Display all documents in the users' collection to the console.
for user in db.users.find():
    print(user)

print('Here is the document with employeeId 1011:')
# Display the document from the users' collection with the employeeId of 1011 to the console.
print(db.users.find_one({ 'employeeId': '1011'}))

print('Here is the document with the lastName Mozart:')
# Display the document from the users' collection with the lastName Mozart to the console.
print(db.users.find_one({ 'lastName': 'Mozart' }))





