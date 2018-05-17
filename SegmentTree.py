class SegmentTreeNode:
	"""This is to implement segment tree node.
	
	Attributes:
	"""
    def __init__(self, start, end, max):
    	"""This is to initiate tree node.

    	Args:
    		self.start: int, start of the segment
    		self.end: int, end of the segment
    		self.max: int or float (depending on the input) 
    				  max value of the segment
    	"""
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
    
class SegmentTree:
	"""This is to implement the segment tree and its three
	basic operations: build, query and modify.

	"""
    def build(self, A):
    	"""This is to build the segment tree.

    	Args:
    		A: list of numbers

    	Returns:
    		SegmentTreeNode of the root of SegmentTree

    	Example:
    		for generating A and use build method:
    	
    		>>> import random
    		>>> A = random.sample(xrange(0, 10), 10)
    		>>> test = SegmentTree()
    		>>> treeA = test.build(A)

    	Return
    	"""
        def buildHelper(A, start, end):
            if start > end:
                return
            if start == end:
                return SegmentTreeNode(start, end, A[start])
            mid = (start + end) / 2
            node = SegmentTreeNode(start, end, None)
            node.left = buildHelper(A, start, mid)
            node.right = buildHelper(A, mid + 1, end)
            if node.left is not None:
                node.max = max(node.max, node.left.max)
            if node.right is not None:
                node.max = max(node.max, node.right.max)
            return node
        return buildHelper(A, 0, len(A) - 1)
    
    def query(self, root, start, end):
        if start <= root.start and end >= root.end:
            return root.max
        mid = (root.start + root.end) / 2
        ans = None
        if mid >= start:
            ans = max(ans, self.query(root.left, start, end))
        if mid + 1 <= end:
            ans = max(ans, self.query(root.right, start, end))
        return ans
import random
