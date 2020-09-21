from math import ceil, log2


class SegmentTree:
    def __init__(self, array):
        self.arr = array
        self.len_arr = len(array)

        # Height of segment tree
        height = int(ceil(log2(self.len_arr)))
        # Maximum size of segment tree
        self.seg_tree = [0] * (2 * int(2 ** height) - 1)
        self.build(
            index_current_vertex=0,
            seg_tree_left_limit=0,
            seg_tree_right_limit=self.len_arr - 1,
        )

    def build(self, index_current_vertex, seg_tree_left_limit, seg_tree_right_limit):
        if seg_tree_left_limit == seg_tree_right_limit:
            self.seg_tree[index_current_vertex] = self.arr[seg_tree_left_limit]
        else:
            middle = self._mid(seg_tree_left_limit, seg_tree_right_limit)
            # If there are more than one elements,
            # then recur for left and right subtrees
            # and store the sum of values in this node
            # that the left child of a vertex at index i is stored at index 2i+1,
            # and the right one at index 2i+2
            left_child_vertex = 2 * index_current_vertex + 1
            right_child_vertex = 2 * index_current_vertex + 2
            self.build(left_child_vertex, seg_tree_left_limit, middle)
            self.build(right_child_vertex, middle + 1, seg_tree_right_limit)
            self.seg_tree[index_current_vertex] = (
                self.seg_tree[left_child_vertex] + self.seg_tree[right_child_vertex]
            )

    def querySum(self, query_start, query_end):
        return self._querySum(0, 0, self.len_arr - 1, query_start, query_end)

    def _querySum(
        self, index_current_node, seg_tree_left, seg_tree_right, query_left, query_right
    ):
        if query_left > query_right:
            return 0

        if query_left == seg_tree_left and query_right == seg_tree_right:
            return self.seg_tree[index_current_node]

        middle = self._mid(seg_tree_left, seg_tree_right)
        left = 2 * index_current_node + 1
        right = 2 * index_current_node + 2
        return self._querySum(
            left, seg_tree_left, middle, query_left, min(query_right, middle)
        ) + self._querySum(
            right, middle + 1, seg_tree_right, max(query_left, middle + 1), query_right
        )

    def updateValueOfIndex(self, index, new_val):
        self._updateValueOfIndex(0, 0, self.len_arr - 1, index, new_val)

    def _updateValueOfIndex(
        self, index_current_node, seg_tree_left, seg_tree_right, index_val, new_val
    ):
        if seg_tree_left == seg_tree_right:  # [2..2]
            self.seg_tree[index_current_node] = new_val
        else:
            middle = self._mid(seg_tree_left, seg_tree_right)
            left = 2 * index_current_node + 1
            right = 2 * index_current_node + 2
            if index_val <= middle:
                self._updateValueOfIndex(
                    left, seg_tree_left, middle, index_val, new_val
                )
            else:
                self._updateValueOfIndex(
                    right, middle + 1, seg_tree_right, index_val, new_val
                )
            self.seg_tree[index_current_node] = (
                self.seg_tree[left] + self.seg_tree[right]
            )

    def _mid(self, low, high):
        return low + ((high - low) // 2)


arr = [1, 3, 5, 7, 9, 11]
segment = SegmentTree(arr)
print(segment.querySum(1, 3))  # 15

# Update: set arr[1] = 10 and update
# corresponding segment tree nodes
segment.updateValueOfIndex(1, 10)

# Find sum after the value is updated
print(segment.querySum(1, 3))  # 22
