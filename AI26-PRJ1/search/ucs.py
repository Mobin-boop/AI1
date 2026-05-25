import heapq
def make_path(parent, actions, state):
    result = []
    current = state
    while parent[current] is not None:
        result.append(actions[current])
        current = parent[current]
    result.reverse()
    return result
def ucs(initial_state):
    pq = []
    index = 0
    heapq.heappush(
        pq,
        (0, index, initial_state)
    )
    parent = {}
    actions = {}
    costs = {}
    parent[initial_state] = None
    costs[initial_state] = 0
    while len(pq) > 0:
        current_cost, _, state = heapq.heappop(pq)
        if state.is_goal_state():
            return make_path(parent, actions, state)
        if current_cost > costs[state]:
            continue
        successors = state.get_successors()
        for action, cost, next_state in successors:
            if next_state.is_collision_state():
                continue
            new_cost = current_cost + cost
            if next_state not in costs:
                costs[next_state] = new_cost
                parent[next_state] = state
                actions[next_state] = action
                index += 1
                heapq.heappush(
                    pq,
                    (new_cost, index, next_state)
                )
            elif new_cost < costs[next_state]:
                costs[next_state] = new_cost
                parent[next_state] = state
                actions[next_state] = action
                index += 1
                heapq.heappush(
                    pq,
                    (new_cost, index, next_state)
                )
    return []