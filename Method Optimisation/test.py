import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Eulerian Circuit")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define the graph as a dictionary of edges
graph = {
    0: [1, 3],
    1: [2, 4],
    2: [3],
    3: [1],
    4: [0, 2]
}

# Initialize the circuit
circuit = []

# Choose a random starting node
start_node = random.choice(list(graph.keys()))

# Initialize the stack with the starting node
stack = [start_node]

# Loop until the stack is empty
while stack:
    # Get the top node from the stack
    node = stack[-1]
    
    # Check if the node has any unexplored edges
    if graph[node]:
        # Choose a random edge from the node
        neighbor = graph[node].pop(random.randint(0, len(graph[node]) - 1))
        
        # Add the edge to the circuit
        circuit.append((node, neighbor))
        
        # Push the neighbor onto the stack
        stack.append(neighbor)
    else:
        # Remove the node from the stack
        stack.pop()

# Draw the circuit
for edge in circuit:
    pygame.draw.line(window, WHITE, (50 + 100 * edge[0], 50 + 100 * edge[1]), (50 + 100 * edge[1], 50 + 100 * edge[0]), 5)

# Draw the nodes
for node in graph:
    color = GREEN if node == start_node else RED
    pygame.draw.circle(window, color, (50 + 100 * node, 50), 25)

# Update the display
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
