export default function updateStudentGradeByCity(list, city, newGrades) {
  return list.filter((student) => student.location === city)
    .map((student) => {
      const foundGrade = newGrades.find((grade) => grade.studentId === student.id);
      return {
        id: student.id,
        firstName: student.firstName,
        location: student.location,
        grade: foundGrade ? foundGrade.grade : 'N/A',
      };
    });
}
