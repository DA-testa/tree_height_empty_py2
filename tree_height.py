# python3

import sys

def build_tree(n, parents):
    nodes = [None] * n
    for i in range(n):
        nodes[i]= {'value': i, 'children': []}
    root = None
    for i in range(n):
        parent= parents[i]
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent]['children'].append(nodes[i])
    return root



def compute_height(root):
    if root is None:
        return 0
    max_height = 0
    for child in root['children']:
        height= compute_height(child)
        max_height = max(max_height, height)
    return max_height + 1


def main():
    n= int(input())
    parents = list(map(int, input().split()))
    root = build_tree(n,parents)
    height = compute_height(root)
    print(height)


if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
main()
