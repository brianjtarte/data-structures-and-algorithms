
# Graph - Code Challenge 35

## Collaborator(s):
1. JJ E.
2. Jacob A.
3. Brian T.

## Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

 - add node
   - Arguments: value
   - Returns: The added node
   - Add a node to the graph
 - add edge
   - Arguments: 2 nodes to be connected by the edge, weight (optional)
   - Returns: nothing
   - Adds a new edge between two nodes in the graph
   - If specified, assign a weight to the edge
   - Both nodes should already be in the Graph
 - get nodes
   - Arguments: none
   - Returns all of the nodes in the graph as a collection (set, list, or similar)
 - get neighbors
   - Arguments: node
   - Returns a collection of edges connected to the given node
   - Include the weight of the connection in the returned collection
 - size
   - Arguments: none
   - Returns the total number of nodes in the graph


## Whiteboard Process

N/A

## Approach & Efficiency
- add_node:
T: O(1)
S: O(1)

- add_edge:
T: O(1)
S: O(1)

- get_nodes:
T: O(1)
S: O(1)
- get_neighbors:
T: O(n^2)
S: O(n)

- size:
T: O(1)
S: O(1)


