const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const path = process.argv[2];
    await countStudents(path)
      .then((data) => {
        res.send(`This is the list of our students\n${data}`);
      });
  } catch (error) {
    res.status(500).send('Cannot load the database');
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

module.exports = app;
