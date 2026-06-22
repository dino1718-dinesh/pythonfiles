def average(lst):
    avg = sum(lst) / len(lst)
    return f"{avg:.2f}"

numbers = list(map(int,input().split()))
print(average(numbers))