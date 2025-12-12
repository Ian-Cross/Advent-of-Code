class Convex_hull:
  def __init__(self, points):
    self.points = sorted(set(points))
    self.hull_points = self.compute()
  
  def cross(self, o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
  
  def compute(self):
    if len(self.points) <= 1:
        return self.points

    lower = []
    for p in self.points:
        while len(lower) >= 2 and self.cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(self.points):
        while len(upper) >= 2 and self.cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper to get full hull (excluding duplicate endpoints)
    return lower[:-1] + upper[:-1]

  def is_contained(self, point):
    n = len(self.hull_points)
    for i in range(n):
        a, b = self.hull_points[i], self.hull_points[(i+1)%n]
        
        # Cross product to check if point is "outside" the edge
        if self.cross(a, b, point) < 0:
            return False
    return True
    
