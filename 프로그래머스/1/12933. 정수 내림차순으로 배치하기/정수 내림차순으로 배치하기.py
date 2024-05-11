def solution(n):
    ali=list(str(n))
    ali.sort(reverse=True)
    sorted_n="".join(ali)
    return int(sorted_n)