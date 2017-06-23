const mongoose = require('mongoose')
const conn = require('../db/db')
const Schema = mongoose.Schema

const docSchema = new Schema({
  url: String,
  title: String,
  content: String
})

const docModel = conn.model('Doc', docSchema)


module.exports = docModel
