from collections import deque
import heapq
from helpers import Map
from typing import Dict, List, Optional, Tuple

import numpy as np


def euclidean_distance(node_a_x: float, node_a_y: float, node_b_x: float, node_b_y: float) -> float:
    """The straight line distance between two nodes

    Args:
        node_a_x: first node x coordinate
        node_a_y: first node y coordinate
        node_a_x: second node x coordinate
        node_a_y: second node y coordinate

    Returns:
        float - Euclidean distance between the two nodes
    """
    return np.sqrt(((node_a_x - node_b_x) ** 2) + ((node_a_y - node_b_y) ** 2))


def manhattan_distance(node_a_x: float, node_a_y: float, node_b_x: float, node_b_y: float) -> float:
    """The manhattan distance between two nodes (one direction + other direction)

    Args:
        node_a_x: first node x coordinate
        node_a_y: first node y coordinate
        node_a_x: second node x coordinate
        node_a_y: second node y coordinate

    Returns:
        float - Manhattan distance between the two nodes
    """
    return np.absolute(node_a_x - node_b_x) + np.absolute(node_a_y - node_b_y)


def euclidean_distance(node_a_x: float, node_a_y: float, node_b_x: float, node_b_y: float) -> float:
    """The straight line distance between two nodes

    Args:
        node_a_x: first node x coordinate
        node_a_y: first node y coordinate
        node_a_x: second node x coordinate
        node_a_y: second node y coordinate

    Returns:
        float - Euclidean distance between the two nodes
    """
    return np.sqrt(((node_a_x - node_b_x) ** 2) + ((node_a_y - node_b_y) ** 2))


def max_axis_distance(node_a_x: float, node_a_y: float, node_b_x: float, node_b_y: float) -> float:
    """The return max(x_distance, y_distance)

    Args:
        node_a_x: first node x coordinate
        node_a_y: first node y coordinate
        node_a_x: second node x coordinate
        node_a_y: second node y coordinate

    Returns:
        float - Euclidean distance between the two nodes
    """
    return max(np.absolute(node_a_x - node_b_x), np.absolute(node_a_y - node_b_y))


DIS_TO_USE = {
    'euclidean_distance': euclidean_distance,
    'manhattan_distance': manhattan_distance,
    'max_axis_distance': max_axis_distance

}


def get_node_coordinates(M, node_id: int) -> Tuple[float, float]:
    """Get the node x and y coordinates

    Args:
        M: map
        node_id: the node id

    Returns:
        x, y: the x and y coordinates
    """
    return M.intersections[node_id][0], M.intersections[node_id][1]


def build_route(opposite_path_dict: Dict[Optional[int], int], goal_node: int) -> List[int]:
    """Build a list of the route based on the dictionary that holds the reverse routes

    Args:
        opposite_path_dict: if a -> b so it would be saved {'b': 'a'}
        goal_node: the goal node

    Returns:
        a list of the path from start to end
    """
    path = deque()
    while goal_node:
        path.appendleft(goal_node)
        goal_node = opposite_path_dict[goal_node]

    return list(path)


def shortest_path(M: Map, start_node: int, goal_node: int, distance_metric: str = 'euclidean_distance') -> Optional[
    List[int]]:
    """Build the shortest path using A*

    Args:
        M: the map with all of the road and coordinate information
        start_node: the start node
        goal_node: the goal node
        distance_metric: distance metric to use

    Returns:
        a list of the shortest path nodes. None if no path was found
    """
    assert distance_metric in DIS_TO_USE
    distance_function = DIS_TO_USE[distance_metric]
    print("shortest path called")
    q = []
    visited_set = set()
    goal_node_x, goal_node_y = get_node_coordinates(M, goal_node)
    heapq.heappush(q, (0, 0, start_node, None))
    opposite_path_dict = {}
    number_of_operations = 1
    while q:
        number_of_operations += 1
        computed_distance, actual_distance, this_node_id, last_node_id = heapq.heappop(q)
        if this_node_id in visited_set:
            continue

        node_id_x, node_id_y = get_node_coordinates(M, this_node_id)
        visited_set.add(this_node_id)
        opposite_path_dict[this_node_id] = last_node_id
        if this_node_id == goal_node:
            print(number_of_operations)
            return build_route(opposite_path_dict, goal_node)

        for next_node_id in M.roads[this_node_id]:
            number_of_operations += 1
            if next_node_id in visited_set:
                continue

            next_node_id_x, next_node_id_y = get_node_coordinates(M, next_node_id)
            next_actual_distance = actual_distance + euclidean_distance(node_id_x, node_id_y, next_node_id_x,
                                                                        next_node_id_y)
            next_computed_distance = next_actual_distance + distance_function(next_node_id_x, next_node_id_y,
                                                                              goal_node_x, goal_node_y)
            heapq.heappush(q, (next_computed_distance, next_actual_distance, next_node_id, this_node_id))

    print(f'Number of operations was: {number_of_operations}')
    return None
