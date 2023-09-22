#-------------------------------------------------------
#  Title: davidson_usersp2.py
#  Author: John Davidson
#  Date: 22 September 2023
#  Description: Exercise 7.3 for WEB 335 - Intro to NoSQL.
#-------------------------------------------------------

# Import the MongoClient.
from pymongo import MongoClient
import datetime

# Build a connection string to connect to web335DB.
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.feyswh3.mongodb.net/web335DBretryWrites=true&w=majority")

# Configure a variable to access web335DB database.
db = client['web335DB']

# Display all documents in the users' collection to the console.
for user in db.users.find():
    print(user)

# Make a blank line to make console more readable.
print('')

# Store the new user document in a variable to be added to the users collection.
spartan = {
    'firstName': 'Master',
    'lastName': 'Chief',
    'employeeId': '1014',
    'email': 'haloEnjoyer@me.com',
    'dateCreated': datetime.datetime.utcnow()
}

# Add the spartan object to the users collection.
db.users.insert_one(spartan)

# Prove that the new document was successfully added to the collection.
print(db.users.find_one({ 'employeeId': '1014'}))

# Make a blank line to make console more readable.
print('')

# Update the newly created user document's email value.
db.users.update_one(
    { 'employeeId': '1014',}, {'$set': { 'email': 'spartan117@me.com' }})

# Prove that the new document's email was successfully updated.
print(db.users.find_one({ 'employeeId': '1014' }))

# Make a blank space to make console more readable.
print('')

# Delete the recently created user document from the collection.
db.users.delete_one({ 'employeeId': '1014'})

# Prove that the recently added user was  successfully deleted from the collection.
print(db.users.find_one({ 'employeeId': '1014' }))





