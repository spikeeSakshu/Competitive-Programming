class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.dfs(node, {})

    def dfs(self, node, dic):
        if not node: return None
        if dic.get(node.val, None) != None: return dic[node.val]
        cur = Node(node.val)
        dic[cur.val] = cur
        cur.neighbors = [*map(lambda x: self.dfs(x, dic), node.neighbors)]
        return cur