export default function getListStudentIds(list) {
  if (!Array.isArray(list)) {
    return [];
  }
  const listId = list.map((student) => student.id);
  return listId;
}
