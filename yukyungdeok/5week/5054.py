# 5054번 주차의 신
for _ in range(int(input())):
	input(); l = sorted(map(int, input().split()))
	print((l[-1]-l[0])*2)