from collections import deque

def solve(tar_a, tar_b, final_target):
    if final_target == 0:
        return

    q = deque([((0, 0), [(0, 0)], "")])
    vis = [[False] * (tar_b + 1) for _ in range(tar_a + 1)]
    vis[0][0] = True

    while q:
        (x_jug, y_jug), path, path_by_st = q.popleft()

        if x_jug == final_target or y_jug == final_target:
            print("Path:", path)
            print("Steps to reach:", path_by_st)
            print("FOUND")
            continue

        # option1: Completely fill A
        if x_jug < tar_a and not vis[tar_a][y_jug]:
            n_path = path + [(tar_a, y_jug)]
            n_path_by_st = path_by_st + " Fill A, "
            q.append(((tar_a, y_jug), n_path, n_path_by_st))
            vis[tar_a][y_jug] = True

        # option2: Completely fill B
        if y_jug < tar_b and not vis[x_jug][tar_b]:
            n_path = path + [(x_jug, tar_b)]
            n_path_by_st = path_by_st + " Fill B, "
            q.append(((x_jug, tar_b), n_path, n_path_by_st))
            vis[x_jug][tar_b] = True

        # option3: Completely Empty A
        if x_jug > 0 and not vis[0][y_jug]:
            n_path = path + [(0, y_jug)]
            n_path_by_st = path_by_st + " Empty A, "
            q.append(((0, y_jug), n_path, n_path_by_st))
            vis[0][y_jug] = True

        # option4: Completely Empty B
        if y_jug > 0 and not vis[x_jug][0]:
            n_path = path + [(x_jug, 0)]
            n_path_by_st = path_by_st + " Empty B, "
            q.append(((x_jug, 0), n_path, n_path_by_st))
            vis[x_jug][0] = True

        # option 5: Pour from A to B
        if x_jug > 0 and y_jug < tar_b:
            pour_amount = min(x_jug, tar_b - y_jug)
            n_path = path + [(x_jug - pour_amount, y_jug + pour_amount)]
            n_path_by_st = path_by_st + " Move A to B, "
            if not vis[x_jug - pour_amount][y_jug + pour_amount]:
                q.append(((x_jug - pour_amount, y_jug + pour_amount), n_path, n_path_by_st))
                vis[x_jug - pour_amount][y_jug + pour_amount] = True

        # option 6: Pour from B to A
        if y_jug > 0 and x_jug < tar_a:
            pour_amount = min(y_jug, tar_a - x_jug)
            n_path = path + [(x_jug + pour_amount, y_jug - pour_amount)]
            n_path_by_st = path_by_st + " Move B to A, "
            if not vis[x_jug + pour_amount][y_jug - pour_amount]:
                q.append(((x_jug + pour_amount, y_jug - pour_amount), n_path, n_path_by_st))
                vis[x_jug + pour_amount][y_jug - pour_amount] = True

if __name__ == "__main__":
    solve(4, 3, 2)
