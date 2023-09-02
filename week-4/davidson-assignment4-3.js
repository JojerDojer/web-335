/**
============================================
; Title: davidson-mongodb-shell.js
; Author: John Davidson
; Date: 09/1/2023
; Description: The MongoDB queries used for WEB 335 - Assignment 4.3.
============================================
*/

// Query to retrieve all documents in the "users" collection.
db.users.find()

// Query to retrieve the document matching the email jbach@me.com.
db.users.find({ email: "jbach@me.com" })

// Query to retrieve the document matching the last name Mozart.
db.users.find({ lastName: "Mozart" })

// Query to retrieve the document matching the first name Richard.
db.users.find({ firstName: "Richard" })

// Query to retrieve the document matching the specified employeeId number 1010.
db.users.find({ employeeId: "1010"  })
