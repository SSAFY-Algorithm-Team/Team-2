class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.is_wolf=None
        
answer = 0

def solution(info, edges):
    
    def dfs(sheep, wolf, candidates):

        global answer
        answer = max(answer, sheep)

        for node in candidates:

            ns, nw = sheep, wolf                      #현재까지 양의 수, 늑대의 수
            if nodes[node].is_wolf == 0: ns += 1
            else: nw += 1

            if nw >= ns:
                continue

            next_nodes = candidates.copy()
            next_nodes.remove(node)
            if(nodes[node].left):
                next_nodes.append(nodes[node].left.val)
            if(nodes[node].right):
                next_nodes.append(nodes[node].right.val)

            dfs(ns, nw, next_nodes)
        
    nodes=[]
    
    for i in range(len(info)):
        
        nodes.append(Node(i))
        nodes[i].is_wolf=info[i]
    
    for parent, child in edges:
        if(nodes[parent].left is None):
            nodes[parent].left=nodes[child]
        else:nodes[parent].right=nodes[child]
            
    dfs(0,0,[0])
    
    return answer