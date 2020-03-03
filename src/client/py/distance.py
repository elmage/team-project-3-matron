"""
Find the distance between any two nodes in a given graph, with a list of node id pairs.
"""

from .utility import *


def dijkstra(graph: Graph, s_id: str, e_id: str, adjacency_map: AdjacencyMap = None) -> Path:
    """
    Return a 2-tuple, where the first element is the weight along
    the shortest path from start to end, as given by s_id and e_id,
    respectively. The second element is the list of id's of the
    nodes along this shortest path. Return (-1, []) if no path
    exists between start and end.
    """
    if adjacency_map is None:
        adjacency_map = graph.get_adjacency_map()
    open_paths = [(0, [s_id])]

    def get_succs(path: Path) -> List[Path]:
        succs = []
        cur_weight = path[0]
        path_nodes = path[1]
        adj_nodes = adjacency_map[path_nodes[-1]]
        for weight, node in adj_nodes:
            succ = (cur_weight + weight, path_nodes + [node])
            succs.append(succ)
        return succs

    while len(open_paths) > 0:
        cur_path = open_paths.pop(0)
        if cur_path[1][-1] == e_id:
            return cur_path
        else:
            cur_succs = get_succs(cur_path)
            for s in cur_succs:
                heapq.heappush(open_paths, s)
    return -1, []


def find_dist_from_start(graph: Graph, start_id: str) -> Dict[List[Tuple[float, str]]]:
    """
    Given graph and the id of a start node, return a json object containing distances
    from the start to all non-hallway nodes in graph. Format of output:
    Key:
        Room type (for example, "supply room")
    Value:
        A list of tuples (d, id) where id is the id of a room with the specified room type,
        and d is the distance (sum of edge weights) between it and the start room.
    """
    pass
