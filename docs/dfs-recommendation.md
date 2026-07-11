# DFS Recommendation

## Overview

The project includes a category descendants helper function in `categoriesApp/utils.py`.

## Implementation

The function `category_descendants(categories, start_id)` accepts:
- `categories`: iterable of `(id, parent_id)` pairs
- `start_id`: category id to traverse from

It builds a graph of child relationships and performs depth-first search.

## Algorithm

1. Build `children` map from parent ID to list of child IDs.
2. Initialize `stack` with `start_id`.
3. Pop a node, add children to `stack`, and visit recursively.
4. Return all discovered descendant IDs.

## Why DFS?

- DFS efficiently enumerates descendants in a tree or graph.
- It uses stack-based traversal with O(N) complexity.

## Complexity

- Time: O(N) where N is number of category pairs
- Space: O(N) for the child map and visited set

## Notes

- The function is currently defined, but `Category` model does not have a `parent` field.
- Therefore the DFS helper is not actually used with a parent-child model in the current schema.
