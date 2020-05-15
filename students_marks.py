n=int(input())
students=[[input(),float(input())] for _ in range(n) ]
smallest=list(sorted([marks for name,marks in students]))[1]
print("\n".join(sorted([name for name,marks in students if marks == smallest])))