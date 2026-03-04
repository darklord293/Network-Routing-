import math


class ArrayPriorityQueue:
    def __init__(self, nodes):
        # initializing the dist array to inifinite
        self.dist = [math.inf] * len(nodes)
        self.queue = []

    # inserting node in the queue
    def insert(self, node_index):
        self.queue.append(node_index)

    # update the distance value of node
    def decrease_key(self, dist, node_index):
        self.dist[node_index] = dist

    # return the node with minimum distance and remove it from queue
    def delete_min(self):
        if not self.queue:
            return None

        min_node = None
        min_distance = math.inf

        for node in self.queue:
            if self.dist[node] < min_distance:
                min_node = node
                min_distance = self.dist[node]

        self.queue.remove(min_node)
        return min_node
