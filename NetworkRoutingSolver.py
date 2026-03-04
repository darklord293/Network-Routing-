#!/usr/bin/python3
import math
import time

from CS4412Graph import *
from Heap_Priority_Queue import HeapPriorityQueue
from Array_Priority_Queue import ArrayPriorityQueue


class NetworkRoutingSolver:
    def __init__(self):
        self.prev_array = None
        self.cost = None

    def initializeNetwork(self, network):
        assert type(network) == CS4412Graph
        self.network = network

    def getShortestPath(self, destIndex):
        self.dest = destIndex
        path_edges = []
        total_length = 0
        curr_node_index = destIndex

        while True:
            prev_index = self.prev_array[curr_node_index]
            if prev_index is None:
                print("--------------------------------")
                print("Destination not reachable")
                print("--------------------------------")
                return exit(0)
            prev_node = self.network.nodes[self.prev_array[curr_node_index]]
            edge = self.find_edge(prev_node, curr_node_index)

            path_edges.append(
                (edge.src.loc, edge.dest.loc, "{:.0f}".format(edge.length))
            )
            total_length += edge.length
            curr_node_index = prev_node.node_id

            if edge.src.node_id == self.source:
                break

        return {"cost": total_length, "path": path_edges}

    def find_edge(self, node, dest_index):
        for neighbor in node.neighbors:
            if neighbor.dest.node_id == dest_index:
                return neighbor

    def computeShortestPaths(self, srcIndex, use_heap=False):
        self.source = srcIndex
        t1 = time.time()

        if use_heap:
            pq = HeapPriorityQueue(self.network.nodes)
        else:
            pq = ArrayPriorityQueue(self.network.nodes)

        # initializing the prev array to nil
        self.prev_array = [None] * len(self.network.nodes)

        # Start with the source node and updating the dist value to 0
        pq.insert(srcIndex)
        pq.decrease_key(0, srcIndex)

        while pq.queue:
            curr_min_node_index = pq.delete_min()
            curr_node = self.network.nodes[curr_min_node_index]

            # Check each edge from the lowest distance node
            for edge in curr_node.neighbors:
                node_index = edge.dest.node_id
                new_distance = pq.dist[curr_min_node_index] + edge.length
                if new_distance < pq.dist[node_index]:
                    pq.insert(node_index)
                    self.prev_array[node_index] = curr_min_node_index
                    pq.decrease_key(new_distance, node_index)

        t2 = time.time()
        return t2 - t1
