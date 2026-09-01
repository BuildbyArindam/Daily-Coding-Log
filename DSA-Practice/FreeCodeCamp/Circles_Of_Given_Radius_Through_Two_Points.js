/**
 * Problem: Circles of Given Radius Through Two Points
 * Platform: FreeCodeCamp (Rosetta Code Challenges)
 * Link: https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/circles-of-given-radius-through-two-points
 * Date Solved: 2026-09-01
 * Difficulty: Easy-Medium
 * Topics: Geometry, Math
 *
 * Approach:
 * Given two points and a radius, find the center(s) of circle(s) of that
 * radius passing through both points. Compute the distance between the
 * points, then handle edge cases (r = 0, coincident points, points farther
 * apart than the diameter, points exactly at the diameter). Otherwise, find
 * the midpoint of the segment, then use the perpendicular bisector: the
 * offset distance h from the midpoint to each center is found via
 * Pythagoras (h = sqrt(r^2 - (d/2)^2)), applied along the unit vector
 * perpendicular to the segment joining the two points.
 *
 * Time Complexity:  O(1) — constant-time arithmetic, no loops
 * Space Complexity: O(1) — fixed number of scalar variables
 */





function getCircles(...args) {
  const [p1, p2, r] = args;
  const x1 = p1[0];
  const y1 = p1[1];
  const x2 = p2[0];
  const y2 = p2[1];
  const dx = x2 - x1;
  const dy = y2 - y1;
  const distance = Math.sqrt(dx * dx + dy * dy);
  if (r === 0) {
    if (distance === 0) {
      return "Radius Zero";
    }
    return "No intersection. Points further apart than circle diameter";
  }
  if (distance === 0) {
    return "Coincident point. Infinite solutions";
  }
  if (distance > 2 * r) {
    return "No intersection. Points further apart than circle diameter";
  }
  const midX = (x1 + x2) / 2;
  const midY = (y1 + y2) / 2;
  if (distance === 2 * r) {
    return [
      Number(midX.toFixed(4)),
      Number(midY.toFixed(4))
    ];
  }
  const h = Math.sqrt(r * r - (distance / 2) ** 2);
  const perpX = -dy / distance;
  const perpY = dx / distance;
  const center1X = midX + h * perpX;
  const center1Y = midY + h * perpY;
  const center2X = midX - h * perpX;
  const center2Y = midY - h * perpY;
  const round4 = (value) => {
    const rounded = Number(value.toFixed(4));
    return Object.is(rounded, -0) ? 0 : rounded;
  };
  return [
    [round4(center1X), round4(center1Y)],
    [round4(center2X), round4(center2Y)]
  ];
}
