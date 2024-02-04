# Graph

Following is note from https://algo.monster/problems/graph_intro

- A Tree: 
    - a connected acyclical graph
	- contain n nodes and n-1 edges
	- there's only 1 path between 2 nodes
	- an undirected graph
- A Graph: 
  - may contains cycle
  - nodes could be disconnected
  - can be directed or undirected

## Terminology
- **vertices** (nodes in tree) are connected by **edges** 
- 2 vertices connected by an edge are called **neighbors** and are **adjacent**
- edges can be **directed** or **undirected**
- **a path** is sequence of vertices
- **a cycle** is a path that starts and ends at the same vertex
- **a connected graph** - graph where every vertex is joined by a path to another vertex
- graph is commonly stored as a **map of adjacency lists**


```
Graph:
	1
   / \
  2 - 3
 /
4

Map of Adjacency List:
{
	1: [2,3]
	2: [1,2,3]
	3: [1,2]
	4: [2]
}
```



