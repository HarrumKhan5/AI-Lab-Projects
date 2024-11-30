class Graph:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def get_neighbors(self,neighbour):
        return self.adj_list.get(neighbour, [])
    def heuristic(self, new):
        Heu = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return Heu.get(new, float('inf'))  

    def astar_algo(self, start_node, stop_node):

        open_list = {start_node}
        closed_list = set()
        goal_node = {start_node: 0}
        parents = {start_node: start_node}

        while open_list:
            new = None
            for neighbour in open_list:
                if new is None or goal_node[neighbour] + self.heuristic(neighbour) < goal_node[new] + self.heuristic(new):
                    new = neighbour

            if new is None:
                print('Path does not exist!')
                return None
            if new == stop_node:
                rec_path = []
                while parents[new] != new:
                    rec_path.append(new)
                    new = parents[new]
                rec_path.append(start_node)
                rec_path.reverse()
                print('Path found: {}'.format(rec_path))
                return rec_path
            for (curr, weight) in self.get_neighbors(new):
                if curr not in open_list and curr not in closed_list:
                    open_list.add(curr)
                    parents[curr] = new
                    goal_node[curr] = goal_node[new] + weight
                else:
                    if goal_node[curr] > goal_node[new] + weight:
                        goal_node[curr] = goal_node[new] + weight
                        parents[curr] = new
                        if curr in closed_list:
                            closed_list.remove(curr)
                            open_list.add(curr)
            open_list.remove(new)
            closed_list.add(new)

        print('Path does not exist!')
        return None
adj_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
graph1 = Graph(adj_list)
graph1.astar_algo('A', 'D')
