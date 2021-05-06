from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]
n = 3
a = [list(map(int,input().split())) for _ in range(n)]
dist = dict()
start = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            a[i][j] = 9
        start = start*10 + a[i][j]
dist[start] = 0
q = deque()
q.append(start)

while q:
    cur = q.popleft()
    cur_str = str(cur)
    z = cur_str.find('9')
    x = z//n
    y = z%n
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            temp = list(cur_str)
            temp[x*3+y], temp[nx*3+ny] = temp[nx*3+ny], temp[x*3+y]
            next_num = int(''.join(temp))
            if next_num not in dist:
                dist[next_num] = dist[cur] +1
                q.append(next_num)

if 123456789 in dist:
    print(dist[123456789])
else:
    print(-1)


