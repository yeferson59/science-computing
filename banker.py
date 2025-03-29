import random

def numbers_random(desde:int, hasta: int) -> int:
  return random.randint(desde, hasta)

# matrix with the maximum resources
def matrix(processes: int, resources: int):
  i:int = 0
  matrix_max:list[list] = []
  while(i < processes):
    j:int = 0
    column:list = []
    while(j < recursos):
      column.append(numbers_random(0, 9))
      j +=1
    matrix_max.append(column)
    i += 1
  return matrix_max


# add flag to the matrix
def add_column(matrix: list[list], number: int) -> list[list]:
  for row in matrix:
    row.append(number)
  return matrix



def difference_matrix(matrix:list[list], matrix2:list[list])-> list[list]:
  nf = len(matrix2)
  nc = len(matrix2[0])
  i:int = 0
  rta_matrix:list[list] = []
  while(i < nf):
    j:int = 0
    column:list = []
    while(j < nc):
      difference = matrix[i][j] - matrix2[i][j]
      if(difference < 0):
        while(matrix2[i][j] > matrix[i][j]):
          matrix2[i][j] = numbers_random(0, 9)
        difference = matrix[i][j] - matrix2[i][j]
      column.append(difference)
      j +=1
    rta_matrix.append(column)
    i += 1
  return rta_matrix

# función imprimir matriz
def print_matrix(matrix: list[list])-> None:
  nf = len(matrix)
  nc = len(matrix[0])
  i:int = 0
  while(i < nf):
    j:int = 0
    while(j < nc):
      print(f"{matrix[i][j]} ", end=" ")
      j +=1
    print()
    i += 1

def list_resources_available(resources_max:list[list])-> list:
  list_resources_max = resources_max[0]
  i = 0
  rta = []
  while(i < len(list_resources_max)):
    difference = list_resources_max[i] - numbers_random(0,9)
    if(difference < 0):
      number_random = numbers_random(0,9)
      while(list_resources_max[i] < number_random):
        number_random = numbers_random(0,9)
      difference = list_resources_max[i] - number_random
    rta.append(difference)
    i += 1
  return rta


def banker(matrix_max:list[list], matrix_asig: list[list], list_available:list , processes:int , resources: int):
  # determine the resources needed
  matrix_need = difference_matrix(matrix_max, matrix_asig)

  resources_available = list_available

  # initialize the processes to false
  m = add_column(matrix_max, 0)

  print_matrix(matrix_need)

  safe_sequence = []

  while len(safe_sequence) < processes:
    process_found = False  # Rename and reset this variable
    for i in range(processes):
      if matrix_max[i][-1] == 0:
        if all(matrix_need[i][j] <= resources_available[j] for j in range(resources)):
          for j in range(resources):
            resources_available[j] += matrix_asig[i][j]
          matrix_max[i][-1] = 1
          safe_sequence.append(i)
          process_found = True  # Correct spelling here
          print(f"process {i} executed. Resources available now: {resources_available}")
          break
    if not process_found:  # Use the corrected variable name
      print("The system is not in a safe state. It cannot complete the sequence.")
      return False
  # Si todos los procesos pudieron ejecutarse, el sistema está en estado seguro
  print("The system is in a safe state. Safe sequence:", safe_sequence)
  return True

# amount of processes
processes = int(input("Enter the amount of processes: "))

# amount of resources
resources = int(input("Enter the amount of resources: "))

m = matrix(processes, resources)
m2 = matrix(processes, resources)

# initialize the maximum resources
max_list = matrix(1, resources)
print(max_list)

# initialize the maximum resources
available_list = list_resources_available(max_list)
print(available_list)

banker(m, m2, available_list, processes, resources)