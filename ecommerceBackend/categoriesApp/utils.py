from collections import defaultdict


def category_descendants(categories, start_id):
    """Given an iterable of (id, parent_id) pairs and a start_id,
    return a set of descendant ids (children, grandchildren, ...).
    """
    children = defaultdict(list)
    for cid, parent in categories:
        if parent is not None:
            children[parent].append(cid)

    visited = set()
    stack = [start_id]
    while stack:
        node = stack.pop()
        for c in children.get(node, ()): 
            if c not in visited:
                visited.add(c)
                stack.append(c)
    return visited


def has_cycle(categories):
    """Detect if the parent-child mapping contains a cycle."""
    children = defaultdict(list)
    for cid, parent in categories:
        if parent is not None:
            children[parent].append(cid)

    visited = set()
    recstack = set()

    def dfs(node):
        visited.add(node)
        recstack.add(node)
        for c in children.get(node, ()): 
            if c not in visited:
                if dfs(c):
                    return True
            elif c in recstack:
                return True
        recstack.remove(node)
        return False

    for cid, _ in categories:
        if cid not in visited:
            if dfs(cid):
                return True
    return False
