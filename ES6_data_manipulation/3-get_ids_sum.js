export default function getStudentIdsSum(list) {
  const sumStudents = list.reduce((result, student) => result + student.id, 0);
  return sumStudents;
}
