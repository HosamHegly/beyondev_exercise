from collections import deque


# We use BFS but add a restriction of k moves
def kReachable(grid, start, target, k):
    n = len(grid)
    m = len(grid[0])
    visited = set()
    row_start = start[0]
    col_start = start[1]
    row_targer = target[0]
    col_target = target[1]
    visited.add((row_start, col_start, 0))  # add start pos to visited with 0 moves
    q = deque([(row_start, col_start, 0)])  # add start pos to queue

    while q:
        row, col, moves = q.popleft()  # get left most position in the queue
        if target[0] == row and target[1] == col:
            return True
        if moves < k:
            # check all moves positions if visited and legal and contains no rock then add to visisted set and queue with moves +1
            if row - 1 >= 0 == grid[row - 1][col] and (row - 1, col, moves + 1) not in visited:
                visited.add((row - 1, col, moves + 1))
                q.append([row - 1, col, moves + 1])

            if row + 1 < n and (row + 1, col, moves + 1) not in visited and grid[row + 1][col] == 0:
                visited.add((row + 1, col, moves + 1))
                q.append([row + 1, col, moves + 1])

            if 0 <= col - 1 and (row, col - 1, moves + 1) not in visited and grid[row][col - 1] == 0:
                visited.add((row, col - 1, moves + 1))
                q.append([row, col - 1, moves + 1])

            if col + 1 < m and (row, col + 1, moves + 1) not in visited and grid[row][col + 1] == 0:
                visited.add((row, col + 1, moves + 1))
                q.append([row, col + 1, moves + 1])
    return False


if __name__ == "__main__":

    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]

    start_pos = (0, 0)
    target_pos = (3, 3)
    max_moves = 6

    reachable = kReachable(grid, start_pos, target_pos, max_moves)
    if reachable:
        print("Target position is reachable within the given moves.")
    else:
        print("Target position is not reachable within the given moves.")

    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]

    start_pos = (0, 0)
    target_pos = (3, 3)
    max_moves = 3

    reachable = kReachable(grid, start_pos, target_pos, max_moves)
    if reachable:
        print("Target position is reachable within the given moves.")
    else:
        print("Target position is not reachable within the given moves.")
