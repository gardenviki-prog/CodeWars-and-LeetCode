def tree_by_levels(node):
    if node is None:
        return []
    result = []
    queue = [node]
    while queue:
        result += [queue[0].value]
        if queue[0].left:
            queue += [queue[0].left]
        if queue[0].right:
            queue += [queue[0].right]
        queue.pop(0)
    return result
