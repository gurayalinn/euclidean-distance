import math

def euclidean_distance(point1, point2):
  """
  İki nokta arasındaki Öklid mesafesini hesaplar.

  Args:
    point1: (x1, y1) şeklinde bir demet olan ilk nokta.
    point2: (x2, y2) şeklinde bir demet olan ikinci nokta.

  Returns:
    İki nokta arasındaki Öklid mesafesi.
  """
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
  # Noktaları tanımlayın
  points = [
    (1, 2),
    (3, 4),
    (5, 6),
  ]

  # Mesafeleri hesaplayın
  distances = []
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      distance = euclidean_distance(points[i], points[j])
      distances.append((points[i], points[j], distance))

  # Minimum mesafeyi bulun
  min_distance = min(distances, key=lambda x: x[2])
  print(f"Minimum mesafe: {min_distance[2]} ({min_distance[0]}, {min_distance[1]})")

if __name__ == "__main__":
  main()
