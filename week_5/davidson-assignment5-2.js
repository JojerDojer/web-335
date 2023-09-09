/**
============================================
; Title: davidson-assignment5-2.js
; Author: John Davidson
; Date: 09/6/2023
; Description: The MongoDB queries used for WEB 335 - Assignment 5.2.
============================================
*/

// Query to add a new user to the user's collection.
db.users.insertOne({ firstName: 'John', lastName: 'Davidson', employeeId: '1013', email: 'ilovemongd@db.org', dateCreated: new Date()})

// Query to update Mozart's email address to 'mozart@me.com'.
db.users.updateOne({ email: 'wmozart@me.com' }, {'$set': {email: 'mozart@me.com'}})

// Query to prove the email address was updated.
db.users.find({email:'mozart@me.com'})

// Query to list all documents in the user's collection, using projections to only display firstName, lastName, and email fields.
db.users.find({}, {firstName: 1, lastName: 1, email: 1})
