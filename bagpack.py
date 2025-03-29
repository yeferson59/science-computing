import heapq
from itertools import combinations
from random import randint, choices

def list_random(number_elements, start, end):
  rta = []
  for _ in range(number_elements):
    rta.append(randint(start, end))
  return rta



class Problem_bagpack:
  def __init__(self, matrix_bagpack, capacity, num_ant, num_iteracion, alpha=1.1, beta=2, radio_evaporacion=0.5):
    self.weights =  matrix_bagpack[0]
    self.values =  matrix_bagpack[1]
    self.capacity = capacity
    self.num_ant = num_ant
    self.num_iteracion = num_iteracion
    self.alpha = alpha
    self.beta = beta
    self.radio_evaporacion = radio_evaporacion

  def bagpack_a(self):
    items = [(self.values[i] / self.weights[i] , self.weights[i], self.values[i]) for i in range(len(self.weights))]
    items.sort(reverse=True, key=lambda x: x[0])
    
    priority = []
    heapq.heappush(priority, (0, 0, 0, 0))
    heapq.heappush(priority, (0, 0, 0, 0))

    max_value = 0
    better_combination = []

    while priority:
      _, weight_actual, value_accumulated, i = heapq.heappop(priority)
      if i >= len(items):
        if value_accumulated > max_value:
            max_value = value_accumulated
        continue

      _, weight, value = items[i]

      h = value_accumulated
      weight_available = self.capacity - weight_actual

      for j in range(i, len(items)):
        _, p, v = items[j]

        if(weight_available >= p):
          h += v
          weight_available -= p
        else:
          h += (weight_available / p) * v
          break

      cota_superior = value_accumulated + sum(item[2] for item in items[i:])
      fn = -1 * (value_accumulated + 0.5 * cota_superior)


      if(weight_actual + weight <= self.capacity):
        heapq.heappush(priority, (fn, weight_actual + weight, value_accumulated + value, i + 1))
      heapq.heappush(priority, (fn, weight_actual, value_accumulated, i + 1))

    better_combination = priority

    return max_value, better_combination

  def ba(self):
    n = len(self.weights)
    max_value = 0
    better_combination = []

    for r in range(n):
      for combination in combinations(range(n), r):
        weight_total = sum(self.weights[i] for i in combination)
        value_total = sum(self.values[i] for i in combination)

        if(weight_total <= self.capacity and value_total > max_value):
          max_value = value_total
          better_combination = combination

    return max_value, better_combination

  def bagpack_aco(self):
    n = len(self.weights)
    fermonas = [1] * n # Initialize the fermonas array with 1s
    max_value = 0
    better_combination = []

    for i in range(self.num_iteracion):
      solucions = []
      for _ in range(self.num_ant):
        actual_weight = 0
        actual_value = 0
        solucion = []

        copy_objects = list(range(n))
        while (copy_objects):
          probabilities = []
          for j in copy_objects:
            if(actual_weight + self.weights[j] <= self.capacity):
              heuristic = self.values[j] / self.weights[j]
              probabilities.append((fermonas[j] ** self.alpha) * (heuristic ** self.beta))
            else:
              probabilities.append(0)


          probability_total = sum(probabilities)
          if(probability_total == 0):
            break

          probabilities = [p / probability_total for p in probabilities]
          indice_selected = choices(copy_objects, probabilities)[0]

          solucion.append(indice_selected)
          actual_weight += self.weights[indice_selected]
          actual_value += self.values[indice_selected]

          copy_objects.remove(indice_selected)

        solucions.append((actual_value, solucion))

        if(actual_value > max_value):
          max_value = actual_value
          better_combination = solucion

      fermonas = [p * (1 - self.radio_evaporacion) for p in fermonas]
      for value, solucion in solucions:
        for obj in solucion:
          fermonas[obj] += value # Update the fermonas array

    return max_value, better_combination


# Example usage
matrix_bagpack = [
  [1, 3, 4, 5, 3], # Weights
  [3, 4, 5, 6, 4], # Values
]

problema_bagpack = Problem_bagpack(matrix_bagpack, capacidad, 50, 10)

result, better_combination = problema_bagpack.bagpack_a()
print(result, better_combination)


force_bruta, better_combination = problema_bagpack.ba()
print(force_bruta, better_combination)

aco_result, better_combination = problema_bagpack.bagpack_aco()
print(aco_result, better_combination)

matrix_bagpack = [
  [1, 3, 4, 5, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # Weights
  [3, 4, 5, 6, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], # Values
]

problema_bagpack = Problem_bagpack(matrix_bagpack, capacidad, 80, 12)

result, better_combination = problema_bagpack.bagpack_a()
print(result, better_combination)


force_bruta, better_combination = problema_bagpack.ba()
print(force_bruta, better_combination)

aco_result, better_combination = problema_bagpack.bagpack_aco()
print(aco_result, better_combination)

