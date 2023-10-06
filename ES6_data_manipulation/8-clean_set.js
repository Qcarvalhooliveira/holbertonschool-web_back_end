export default function cleanSet(set, startString) {
  const result = [];

  if (typeof startString !== 'string' || typeof set !== 'object' || startString.length === 0) {
    return '';
  }
  
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      const restOfString = value.slice(startString.length);
      result.push(restOfString);
    }
  });

  return result.join('-');
}
