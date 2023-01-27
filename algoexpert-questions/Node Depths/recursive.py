def nodeDepths(root,depth = 0):
    if root is None: return 0

    return depth + nodeDepths(root.right,depth+1) + nodeDepths(root.left,depth + 1)