def build_path(parent, actions, state):
    result = []
    current = state
    while parent[current] is not None:
        result.append(
            actions[current]
        )
        current = parent[current]
    result.reverse()
    return result
def dfs(state, limit, visited, parent, actions):
    if state.is_goal_state():
        return state
    if limit <= 0:
        return None
    visited.add(state)
    successors = state.get_successors()
    for action, cost, next_state in successors:
        if next_state in visited:
            continue
        try:
            collision = next_state.is_collision_state()
        except:
            try:
                collision = next_state.state_collision_is()
            except:
                collision = False
        if collision:
            continue
        parent[next_state] = state
        actions[next_state] = action
        result = dfs(
            next_state,
            limit - 1,
            visited,
            parent,
            actions
        )
        if result is not None:
            return result
    return None

def dls(initial_state):
    max_depth = 30
    depth = 0
    while depth <= max_depth:
        visited = set()
        parent = {}
        actions = {}
        parent[initial_state] = None
        result = dfs(
            initial_state,
            depth,
            visited,
            parent,
            actions
        )
        if result is not None:
            return build_path(
                parent,
                actions,
                result
            )
        depth += 1
    return []