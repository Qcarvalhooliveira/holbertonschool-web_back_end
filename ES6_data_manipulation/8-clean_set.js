export default function cleanSet(set, startString) {
  if (startString.length === 0) {
    return '';
  }
  
  const result = [];
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      const restOfString = value.slice(startString.length);
      result.push(restOfString);
    }
  });

  return result.join('-');
}
