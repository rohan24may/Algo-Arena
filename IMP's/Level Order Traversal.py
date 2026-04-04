from collections import deque

def level_order(root):
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        node = q.popleft()
        res.append(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return res