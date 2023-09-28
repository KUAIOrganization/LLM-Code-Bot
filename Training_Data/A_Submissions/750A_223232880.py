n, k = map(int, input().split())
contest_time = 240 - k
problems_solved = 0
for i in range(1, n + 1):
    problem_time = 5 * i
    if contest_time >= problem_time:
        problems_solved += 1
        contest_time -= problem_time
    else:
        break
print(problems_solved)
