export default function cleanSet(set, startString) {
  const result = [];

  set.forEach(value => {
    if (value.startsWith(startString)) {
      const restOfString = value.slice(startString.length);
      result.push(restOfString);
    }
  });

  return result.join('-');
}
