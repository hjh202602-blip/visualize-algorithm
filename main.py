import random


def generate_maze(width=30, height=30, seed=None):

    # seed가 같으면 항상 같은 랜덤 결과
    rng = random.Random(seed)

    # 홀수 크기로 맞추기
    if width % 2 == 0:
        width -= 1
    if height % 2 == 0:
        height -= 1

    # 0 = 벽
    # 1 = 길
    # 2 = 시작/도착
    maze = [[0 for _ in range(width)] for _ in range(height)]

    directions = [
        (-2, 0),
        (2, 0),
        (0, -2),
        (0, 2)
    ]

    def is_valid(r, c):
        return 0 < r < height - 1 and 0 < c < width - 1

    def carve_path(r, c):
        maze[r][c] = 1

        dirs = directions.copy()
        rng.shuffle(dirs)

        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if is_valid(nr, nc) and maze[nr][nc] == 0:
                maze[r + dr // 2][c + dc // 2] = 1
                carve_path(nr, nc)

    carve_path(1, 1)

    extra_paths = int(width * height * 0.08)

    for _ in range(extra_paths):

        r = rng.randrange(1, height - 1)
        c = rng.randrange(1, width - 1)

        if maze[r][c] != 0:
            continue

        neighbors = 0

        if maze[r - 1][c] == 1:
            neighbors += 1

        if maze[r + 1][c] == 1:
            neighbors += 1

        if maze[r][c - 1] == 1:
            neighbors += 1

        if maze[r][c + 1] == 1:
            neighbors += 1

        if neighbors >= 2:
            maze[r][c] = 1

    for _ in range(int(width * 0.8)):

        r = rng.randrange(1, height - 1)
        c = rng.randrange(1, width - 1)

        if rng.random() < 0.5:

            length = rng.randint(2, 5)

            for i in range(length):
                nc = c + i

                if nc < width - 1:
                    maze[r][nc] = 1

        else:

            length = rng.randint(2, 5)

            for i in range(length):
                nr = r + i

                if nr < height - 1:
                    maze[nr][c] = 1

    maze[1][1] = 2
    maze[height - 2][width - 2] = 2

    return maze

maze = generate_maze(
    width=45,
    height=45,
    seed=int(input("press the any seed : "))
)

for row in maze:
    for cell in row:

        if cell == 2:
            print("🚩", end=" ")

        elif cell == 1:
            print("⬛", end=" ")

        else:
            print("⬜", end=" ")

    print()