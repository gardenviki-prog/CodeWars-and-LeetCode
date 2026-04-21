# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    result = []
    result += [node.data]
    result += pre_order(node.left)
    result += pre_order(node.right)
    return result

# In-order traversal
def in_order(node):
    if node is None:
        return []
    result = []
    result += in_order(node.left)
    result += [node.data]
    result += in_order(node.right)
    return result

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    result = []
    result += in_order(node.left)
    result += in_order(node.right)
    result += [node.data]
    return result
