# Science Computing

## Bagpack Problem

The bagpack problem is a classic optimization problem in operations research. It is a combinatorial optimization problem that involves selecting a subset of items from a set of items, where each item has a weight and a value, and the goal is to maximize the total value of the selected items while keeping the total weight below a given capacity.

### Bagpack Algorithms

There are several algorithms for solving the bagpack problem, including:

- Brute Force: This algorithm simply tries all possible combinations of items until it finds one that satisfies the capacity constraint. It is not efficient for large sets of items or when the capacity is large.

- Branch and Bound: This algorithm uses a branch-and-bound approach to solve the bagpack problem. It starts with an empty subset and gradually adds items to it, checking if the total weight and value of the items in the subset satisfy the capacity constraint. If not, it backtracks and removes the last item from the subset. This process continues until a valid subset is found that satisfies the capacity constraint.

- Ant Colony Optimization (ACO): This algorithm is inspired by the behavior of ants searching for food in a forest. It uses a population of ants to explore the search space and find the best solution. Each ant has a certain number of ants that it can communicate with, and it uses these communications to share information and explore different parts of the search space. The ACO algorithm is particularly effective for solving large-scale optimization problems, as it can handle a large number of variables and constraints.

### Bagpack Implementation

In this implementation, we will use the Bagpack algorithm to solve the bagpack problem. We will start by defining the problem class and its methods. Then, we will implement the Bagpack algorithm and compare its performance with the Brute Force and Branch and Bound algorithms.

#### Problem Class

First, we will define the problem class, which will contain the necessary data and methods for solving the bagpack problem. We will define the following attributes:

- `weights`: A list of weights for each item.
- `values`: A list of values for each item.
- `capacity`: The maximum capacity of the bag.
- `num_ant`: The number of ants in the ACO algorithm.
- `num_iteracion`: The number of iterations in the ACO algorithm.
- `alpha`: The alpha parameter in the ACO algorithm.
- `beta`: The beta parameter in the ACO algorithm.
- `radio_evaporacion`: The radio_evaporacion parameter in the ACO algorithm.

We will also define the following methods:

- `bagpack_a()`: This method implements the Bagpack algorithm using a simple brute force approach.
- `ba()`: This method implements the Bagpack algorithm using a brute force approach.
- `bagpack_aco()`: This method implements the Bagpack algorithm using the ACO approach.

#### Bagpack Algorithm

Next, we will implement the Bagpack algorithm using the `bagpack_a()` method. This method will use a simple brute force approach to find the best combination of items that satisfies the capacity constraint.

The algorithm works as follows:

1. Sort the items by their values in descending order.
2. Initialize an empty priority queue.
3. For each item, calculate its value and weight, and add it to the priority queue.
4. While the priority queue is not empty, pop the item with the highest value from the priority queue.
5. If the item's weight plus the current weight of the bag does not exceed the capacity, add the item to the bag and update the priority queue with the updated values.
6. If the item's weight plus the current weight of the bag exceeds the capacity, calculate the value of the item by subtracting the weight of the bag from the item's weight and multiplying it by the item's value.
7. If the item's weight plus the current weight of the bag does not exceed the capacity, add the item to the priority queue with the updated values.
8. Repeat steps 4-7 until the priority queue is empty.

#### Brute Force Algorithm

Next, we will implement the Brute Force algorithm using the `ba()` method. This method will use a brute force approach to find the best combination of items that satisfies the capacity constraint.

The algorithm works as follows:

1. Initialize an empty list to store the best combination.
2. For each possible combination of items, calculate the total weight and value of the items in the combination.
3. If the total weight plus the current weight of the bag does not exceed the capacity, add the combination to the list of best combinations.
4. Repeat steps 2-3 until all possible combinations have been checked.
5. Return the maximum value of the best combination and the list of best combinations.

#### Ant Colony Optimization Algorithm

Next, we will implement the Ant Colony Optimization algorithm using the `bagpack_aco()` method. This method will use the ACO approach to find the best combination of items that satisfies the capacity constraint.

The algorithm works as follows:

1. Initialize an empty list to store the best combination.
2. For each possible combination of items, calculate the total weight and value of the items in the combination.

# Banker's Problem

### Banker's Problem

The banker's problem is a classic optimization problem in operations research. It is a combinatorial optimization problem that involves selecting a subset of items from a set of items, where each item has a weight and a value, and the goal is to maximize the total value of the selected items while keeping the total weight below a given capacity.

### Banker's Algorithms

There are several algorithms for solving the banker's problem, including:

- Brute Force: This algorithm simply tries all possible combinations of items until it finds one that satisfies the capacity constraint. It is not efficient for large sets of items or when the capacity is large.

- Branch and Bound: This algorithm uses a branch-and-bound approach to solve the banker's problem. It starts with an empty subset and gradually adds items to it, checking if the total weight and value of the items in the subset satisfy the capacity constraint. If not, it backtracks and removes the last item from the subset. This process continues until a valid subset is found that satisfies the capacity constraint.
