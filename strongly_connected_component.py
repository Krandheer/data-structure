"""
uses kosaraju's algorithm to find strongly connected components in a graph.
basically store all nodes in stack to get some order for traversal.
then reverse the edges and do dfs on each node.
number of times we call dfs is number of SCCs.
"""
