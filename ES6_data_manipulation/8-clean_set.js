export default function cleanSet(set, startString) {
  if (!startString || !startString.length) {
    return '';
  }

  let result = '';

  for (const element of set) {
    if (element && element.startsWith(startString)) {
      result += result.length === 0 ? element.slice(startString.length) : `-${element.slice(startString.length)}`;
    }
  }

  return result;
}
