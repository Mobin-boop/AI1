from collections import deque

def make_path(parent, actions, state):
    result = []
    current = state
    while parent[current] is not None:
        result.append(actions[current])
        current = parent[current]
    result.reverse()
    return result

def bfs(initial_state):
    queue = deque()
    queue.append(initial_state)
    visited = set()
    visited.add(initial_state)
    parent = {}
    actions = {}
    parent[initial_state] = None
    while len(queue) > 0:
        state = queue.popleft()
        if state.is_goal_state():
            return make_path(parent, actions, state)
        successors = state.get_successors()
        for action, cost, next_state in successors:
            if next_state in visited:
                continue
            if next_state.is_collision_state():
                continue
            visited.add(next_state)
            parent[next_state] = state
            actions[next_state] = action
            queue.append(next_state)
    return []