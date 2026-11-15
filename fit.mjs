export function rangeStatus(value, min, max) {
  if (value === null) return 'pending';
  return value >= min && value <= max ? 'yes' : 'no';
}

export function spaceStatus(depth, bodyDepth, clearance) {
  if (clearance === 'no' || (depth !== null && depth < bodyDepth)) return 'no';
  return depth !== null && depth > bodyDepth && clearance === 'yes' ? 'yes' : 'pending';
}
