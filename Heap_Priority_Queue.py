import math


class HeapPriorityQueue:
    def __init__(self, nodes):
        # initializing the distance to infinity
        self.dist = [math.inf] * len(nodes)
        self.queue = []
        # initializing the pointer of the tree to infinity
        self.q_pointer = [math.inf] * len(nodes)

    # add a node into the heap
    def insert(self, node_index):
        self.queue.append(node_index)
        self.q_pointer[node_index] = len(self.queue) - 1
        self.bubble_up(len(self.queue) - 1)

    # adjust the distance update of nodes
    def decrease_key(self, dist, node_index):
        self.dist[node_index] = dist
        self.bubble_up(self.q_pointer[node_index])

    # bubble_up maintains the property of heap after insertion or decrease key operation
    def bubble_up(self, child_index):
        while child_index > 0:
            parent_index = (child_index - 1) // 2
            if (
                self.dist[self.queue[child_index]]
                >= self.dist[self.queue[parent_index]]
            ):
                break
            self.swap_nodes(child_index, parent_index)
            child_index = parent_index

    # return the minimum element from the heap and removes it
    def delete_min(self):
        if not self.queue:
            return None

        min_index = self.queue[0]
        if len(self.queue) == 1:
            self.queue.pop()
            return min_index

        last_index = len(self.queue) - 1
        self.swap_nodes(0, last_index)
        self.queue.pop()  # swaps the item at the end with root and return the root node
        self.bubble_down(0)

        return min_index

    # restores the heap property starting from the given parent_index
    def bubble_down(self, parent_index):
        while True:
            left_child_index = 2 * parent_index + 1
            if left_child_index >= len(self.queue):
                break

            child_index_left = left_child_index
            child_index_right = left_child_index + 1
            if (
                child_index_right < len(self.queue)
                and self.dist[self.queue[child_index_right]]
                < self.dist[self.queue[left_child_index]]
            ):
                child_index_left = child_index_right

            # checking the distance of parent node and the smallest child node
            if (
                self.dist[self.queue[parent_index]]
                <= self.dist[self.queue[child_index_left]]
            ):
                break

            self.swap_nodes(parent_index, child_index_left)
            parent_index = child_index_left

    # perform the swap between nodes
    def swap_nodes(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
        self.q_pointer[self.queue[i]] = i
        self.q_pointer[self.queue[j]] = j
