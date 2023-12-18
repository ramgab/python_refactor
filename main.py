class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calculate_distance(point1, point2):
    x_distance = point1.x - point2.x
    y_distance = point1.y - point2.y
    distance = (x_distance ** 2 + y_distance ** 2) ** 0.5
    return distance

def find_closest_point(points, target_point):
    closest_point = None
    min_distance = float('inf')

    for point in points:
        distance = calculate_distance(point, target_point)
        if distance < min_distance:
            closest_point = point
            min_distance = distance

    return closest_point

# Пример использования:
point1 = Point(1, 2)
point2 = Point(4, 5)
point3 = Point(3, 1)

points_list = [point1, point2, point3]
target = Point(0, 0)

closest = find_closest_point(points_list, target)
print(f"Ближайшая точка: ({closest.x}, {closest.y})")

#Этот код создает класс `Point` для представления точек с координатами x и y. Затем определены функции для вычисления расстояния между двумя точками и поиска ближайшей точки к заданной. В примере использования создаются три точки, формируется список точек, и затем находится ближайшая точка к заданной целевой точке.
