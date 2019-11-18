const express = require('express')
const app = express()
require("./db") // database connection

/**
 * Import routes files
 */
const index_routes = require("./routes/index")
const book_routes = require("./routes/books")

// for parsing application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true }))

app.get('/', (req, res) => {
    return res.send(`Welcome to Ihsandroid`)
})

/**
 * Set routes imported
 */
app.use("/index", index_routes)
app.use("/book", book_routes)

app.listen(3300, () => {
    console.log(`Example app listening on port 3300`)
})