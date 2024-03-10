def solution(nums):
    poket = int(len(nums) / 2) 
    nums = set(nums) 
    
    answer = min(len(nums), poket)
    
    return answer