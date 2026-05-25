import heapq
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def mst_cost(points):
    if len(points) <= 1:
        return 0
    used = set()
    used.add(0)
    total = 0
    while len(used) < len(points):
        best = None
        best_index = None
        for i in used:
            for j in range(len(points)):
                if j in used:
                    continue
                cost = manhattan(
                    points[i],
                    points[j]
                )
                if best is None:
                    best = cost
                    best_index = j
                elif cost < best:
                    best = cost
                    best_index = j
        total += best
        used.add(best_index)
    return total

def heuristic(state):
    agent = state.get_agent_position()
    targets = list(
        state.get_targets_positions()
    )
    if len(targets) == 0:
        return 0
    nearest = None
    for target in targets:
        distance = manhattan(
            agent,
            target
        )

        if nearest is None:
            nearest = distance

        elif distance < nearest:
            nearest = distance

    h = nearest * 7
    mst = mst_cost(targets)
    h += mst * 4
    enemy = state.get_enemy_position()
    if enemy is not None:
        distance = manhattan(
            agent,
            enemy
        )
        if distance <= 1:
            h += 100000
        elif distance <= 2:
            h += 5000

        elif distance <= 3:
            h += 1200
    return h

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

def a_star(initial_state):
    pq = []
    counter = 0
    heapq.heappush(
        pq,
        (
            heuristic(initial_state),
            counter,
            initial_state
        )
    )
    parent = {}
    actions = {}
    costs = {}
    parent[initial_state] = None
    costs[initial_state] = 0
    while len(pq) > 0:
        f, _, state = heapq.heappop(pq)
        if state.is_goal_state():
            return build_path(
                parent,
                actions,
                state
            )
        successors = state.get_successors()
        for action, cost, next_state in successors:
            try:
                collision = next_state.is_collision_state()
            except:
                try:
                    collision = next_state.state_collision_is()
                except:
                    collision = False
            if collision:
                continue
            next_agent = next_state.get_agent_position()
            enemy = next_state.get_enemy_position()
            if enemy is not None:
                distance = manhattan(
                    next_agent,
                    enemy
                )
                if distance <= 1:
                    continue
            new_cost = costs[state] + cost
            if next_state not in costs:
                costs[next_state] = new_cost
                parent[next_state] = state
                actions[next_state] = action
                h = heuristic(next_state)
                total = new_cost + h
                counter += 1
                heapq.heappush(
                    pq,
                    (
                        total,
                        counter,
                        next_state
                    )
                )
            elif new_cost < costs[next_state]:
                costs[next_state] = new_cost
                parent[next_state] = state
                actions[next_state] = action
                h = heuristic(next_state)
                total = new_cost + h
                counter += 1
                heapq.heappush(
                    pq,
                    (
                        total,
                        counter,
                        next_state
                    )
                )
    return []