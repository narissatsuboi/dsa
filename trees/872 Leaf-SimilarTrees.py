# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar_first(root1, root2):
    """dfs inorder traversal with carry along sequence list

    inorder finds the leaf nodes faster (left, visit, right)
    
    passed list with each recursive call to store leaf values
    which adds extra memory
    
    tc O(n) worst case, skewed tree of length n, all nodes
    sc O(n) recursive stack the length of n in the worst case 
    described above
    """
    def dfs_inorder(node, seq) :
        if node:
            dfs_inorder(node.left, seq)
            if not node.left and not node.right:
                seq.append(node.val)
            dfs_inorder(node.right, seq)
        return seq
    return dfs_inorder(root1, []) == dfs_inorder(root2, [])

def leafSimilar_second(root1, root2): 
    """dfs inorder as generator, sequence list outside of 
    recursive calls
    
    same complexity of big o but cleaner
    """
    def dfs_inorder_generator(node):
        if node:
            yield from dfs_inorder_generator(node.left)
            if not node.left and not node.right:
                yield node.val
            yield from dfs_inorder_generator(node.right)
    return list(dfs_inorder_generator(root1)) == list(dfs_inorder_generator(root2))
    
    