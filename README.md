# Campus Navigation and Utility Planner   
---

## Overview

The **Campus Navigation and Utility Planner** is a data-structure–driven software system designed to model university buildings, compute optimal paths, and plan resource delivery routes across a campus.

The system uses **trees and graph algorithms** to organize buildings, find shortest paths, navigate campus spaces, and optimize utility layouts such as water, electricity, and transport routes.

This lab assignment focuses on implementing these structures and algorithms in **Python or C++**, applying them to realistic campus navigation and planning scenarios.

---

## Objectives

- Represent university buildings and campus layout using trees and graphs.  
- Implement shortest path algorithms such as **Dijkstra, BFS, DFS**.  
- Store and retrieve building information using hierarchical data structures.  
- Simulate campus navigation between buildings.  
- Model and optimize utility routes for resource delivery.  
- Understand the role of graph traversal and pathfinding in real-world systems.  
- Build a menu-driven program demonstrating these concepts.

---

## Data Structures & Algorithms Used

### **1. Graphs**
Used to represent:
- Buildings as vertices  
- Roads/walkways as edges  
- Weighted connections (distance, time, or cost)  

Graph variants:
- **Adjacency List**  
- **Adjacency Matrix**  

### **2. Trees**
Used for:
- Organizing buildings into categories: Academic, Hostels, Admin, Sports  
- Maintaining hierarchical campus structures  

### **3. Pathfinding Algorithms**
Used to compute:
- Shortest route between buildings  
- Fast resource-delivery paths  
- Navigation suggestions  

Algorithms implemented:
- Breadth-First Search (BFS)  
- Depth-First Search (DFS)  
- Dijkstra’s Algorithm  

### **4. Queues / Stacks**
Used in:
- BFS (queue)  
- DFS (stack/recursion)  
- Navigation exploration  

---

## Core Functionalities

### ✔ Add Building / Location  
- Store building name, type, code, or zone.  
- Add to tree + graph structure.

### ✔ Display Campus Map  
- Show all buildings  
- Show edges (connections)  
- Display adjacency matrix/list  

### ✔ Find Navigation Path  
- Compute shortest path  
- Show step-by-step route  
- Use BFS/DFS/Dijkstra depending on context  

### ✔ Manage Utility Layouts  
- Model water, power, or goods delivery routes  
- Optimize based on minimum distance  

### ✔ Building Hierarchy Tree  
- Insert, search, and display building hierarchy  
- Show parent and child nodes  

---

## Implementation Steps

1. **Define Building Structure**  
   - Name, code, type, department, zone.

2. **Build Graph Representation**  
   - Create adjacency list/matrix.  
   - Add weighted edges for realistic navigation.

3. **Implement Tree for Building Categories**  
   - Insert academic blocks, hostels, admin zones.  
   - Display hierarchy with traversals.

4. **Implement Pathfinding Algorithms**  
   - BFS for simple routes  
   - DFS for exploration  
   - Dijkstra for optimal weighted paths  

5. **Create Menu-Driven Program**  
   Options include:  
   - Add Building  
   - Create Road/Connection  
   - Display Campus Map  
   - Shortest Path  
   - Building Hierarchy  
   - Utility Route Planning  
   - Exit  

6. **Testing**  
   - Test with 10–20 campus buildings  
   - Random routes  
   - Edge cases (isolated nodes, multiple paths)  

---

## Technologies

This system can be implemented using:

### **Python**
- Dictionaries, lists  
- Graph algorithms  
- Recursive tree traversal  

### **C++**
- Structs, vectors, adjacency lists  
- STL priority queue for Dijkstra  
- Manual tree implementation  

---

## Learning Outcomes

By completing this lab, students will learn to:

- Apply graphs and trees to real-world navigation systems.  
- Implement BFS, DFS, and Dijkstra from scratch.  
- Build and traverse hierarchical structures.  
- Understand shortest-path optimization for utilities and navigation.  
- Design a complete system using fundamental data structures.  
- Build modular, menu-driven applications suitable for academic use.

---

## Author

**Name:** Aditya Chouhan  
**Roll No:** 2401830001  
**Course:** B.Sc. (H) Cybersecurity  

---
