const fs = require('fs').promises;

async function countStudents(database) {
  try {
    const data = await fs.readFile(database, 'utf8');
    let students = data.trim().split('\n');
    const header = students.shift().split(',');

    const studentObjects = [];
    const StudentGroup = {};

    students.forEach((row) => {
      if (row) {
        const studentInfo = row.split(',');
        const studentObj = header.reduce((acc, curr, index) => {
          acc[curr] = studentInfo[index];
          return acc;
        }, {});

        if (!StudentGroup[studentObj.field]) {
          StudentGroup[studentObj.field] = [];
        }
        StudentGroup[studentObj.field].push(studentObj.firstname);
        studentObjects.push(studentObj);
      }
    });

    console.log(`Number of students: ${studentObjects.length}`);
    for (const field in StudentGroup) {
      console.log(`Number of students in ${field}: ${StudentGroup[field].length}. List: ${StudentGroup[field].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;