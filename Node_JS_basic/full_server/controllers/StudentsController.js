import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const students = readDatabase('../../database.csv');
    students.CS.names.sort();
    students.CS.names.forEach((name) => {
      res.write(
        `Number of students in CS: ${students.CS.numStudents}. List: ${name}`,
      );
    });
    students.SWE.names.sort();
    students.SWE.names.forEach((name) => {
      res.write(
        `Number of students in SWE: ${students.SWE.numStudents}. List: ${name}`,
      );
    });
    res.end();
  }

  static getAllStudentsByMajor(req, res) {
    const students = readDatabase('../../database.csv');
    const { major } = req.params;
    if (major === 'CS') {
      students.CS.names.sort();
      students.CS.names.forEach((name) => {
        res.write(
          `Number of students in SWE: ${students.CS.numStudents}. List: ${name}`,
        );
      });
    }
    if (major === 'SWE') {
      students.SWE.names.sort();
      students.SWE.names.forEach((name) => {
        res.write(
          `Number of students in SWE: ${students.SWE.numStudents}. List: ${name}`,
        );
      });
    }
    res.end();
  }
}

export default StudentsController;
