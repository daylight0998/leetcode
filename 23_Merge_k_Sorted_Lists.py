#!/usr/bin/python3
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        min_heap = []
        dummy_head = ListNode(-1)
        runner_node = dummy_head
        runners = {}

        for i, l in enumerate(lists):
            # print(i)
            # print(l)
            # print("=====")
            if l:
                heapq.heappush(min_heap, (l.val, i))
                runners[i] = l

        while min_heap:
            curr_node_val, curr_node_index = heapq.heappop(min_heap)
            runner_node.next = runners[curr_node_index]
            runner_node = runner_node.next
            runners[curr_node_index] = runners[curr_node_index].next
            if runners[curr_node_index]:
                heapq.heappush(min_heap, (runners[curr_node_index].val, curr_node_index))
        return dummy_head.next


s = Solution()
print(s.mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]]))
