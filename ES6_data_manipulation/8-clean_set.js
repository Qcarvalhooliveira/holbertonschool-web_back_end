export default function cleanSet(set, startString) {
  const result = [];

  if (typeof startString !== 'string' || typeof set !== 'object' || startString.length === 0) {
    return '';
  }

  for (const item of set) {
    result.push(item.slice(startString.length));
  }
  return result.join('-');
}
