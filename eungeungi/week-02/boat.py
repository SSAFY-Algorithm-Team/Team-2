def solution(people, limit):
    boats = 0
    people.sort()
    l = 0
    r = len(people)-1
    while l <= r:
        if l==r:
            boats+=1
            break
            
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        boats +=1
        
    return boats