/**
============================================
; Title: davidson-assignment6-2.js
; Author: John Davidson
; Date: 09/13/2023
; Description: The MongoDB queries used for WEB 335 - Assignment 6.2.
============================================
*/

// Query used to show a list of documents in the houses collection.
db.houses.find()

// Query used to show a list od documents in the student's collection.
db.students.find()

// Query used to add a document to the student's collection.
db.students.insertOne({ firstName: 'John', lastName: 'Davidson', studentId: 's1019', houseId: 'h1007' })

// Query used to prove the document was successfully added to the collection.
db.students.findOne({ studentId: 's1019' })

// Query used to delete the previously added document.
db.students.deleteOne({ studentId: 's1019' })

// Query used to prove that the document was successfully deleted.
db.students.findOne({ studentId: 's1019' })

// Query used to show a list of students by house name:
// - Utilizes $lookup stage to combine data from the "houses" and "students" collections.
// - The results include an array of students associated with each house.
db.houses.aggregate([{ $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students' }}])

// Query used to show a list of students for house Gryffindor:
// - Utilizes $lookup stage to combine data from the "houses" and "students" collections.
// - Matches documents by houseId: 'h1009' to select Gryffindor.
// - The results include an array of students associated with house Gryffindor.
db.houses.aggregate([{ $match: { houseId: 'h1009' }}, { $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students' }}])

// Query used to show a list of students for the Eagle mascot:
// - Utilizes $lookup stage to combine data from the "houses" and "students" collections.
// - Matches documents by mascot: 'Eagle' to select the Eagle mascot.
// - The results include an array of students associated with the Eagle mascot.
db.houses.aggregate([{ $match: { mascot: 'Eagle' }}, { $lookup: { from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'students' }}])
