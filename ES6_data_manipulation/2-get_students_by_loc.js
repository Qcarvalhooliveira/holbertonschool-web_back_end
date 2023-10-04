export default function getStudentsByLocation(list, city) {
  const locationStudents = list.filter((student) => student.location === city);
  return locationStudents;
}
