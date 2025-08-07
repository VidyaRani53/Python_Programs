import copy

# Function to print the distance table
def print_table(table):
    for row in table:
        print(row)
    print()

# Function to perform Distance Vector Routing
def distance_vector_routing(distance_table):
    num_nodes = len(distance_table)
    updated_table = copy.deepcopy(distance_table)

    for i in range(num_nodes):
        for j in range(num_nodes):
            for k in range(num_nodes):
                if updated_table[i][k] + updated_table[k][j] < updated_table[i][j]:
                    updated_table[i][j] = updated_table[i][k] + updated_table[k][j]

    return updated_table

# Initial Distance Table (inf means no direct connection)
inf = float('inf')
distance_table = [
    [0, 1, inf, 1],
    [1, 0, 1, inf],
    [inf, 1, 0, 1],
    [1, inf, 1, 0]
]

# Output before update
print("Initial Distance Table:")
print_table(distance_table)

# Apply Distance Vector Routing
updated_table = distance_vector_routing(distance_table)

# Output after update
print("Updated Distance Table After Distance Vector Routing:")
print_table(updated_table)
