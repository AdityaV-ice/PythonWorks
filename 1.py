def can_defeat_villains(start_index, villains, H, M):
    hero_health = H
    hero_count = M
    
    for i in range(start_index, len(villains)):
        villain_health = villains[i]
        if hero_health > villain_health:
            hero_health -= villain_health
        elif hero_health == villain_health:
            hero_health = H
        else:
            hero_count -= 1
            if hero_count <= 0:
                return False
            hero_health = H - villain_health
    return True

def min_villains_to_remove(N, M, H, villains):
    left = 0
    right = N
    result = N
    
    while left <= right:
        mid = (left + right) // 2
        if can_defeat_villains(mid, villains, H, M):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return result

# Reading input
N = int(input())
M = int(input())
H = int(input())
villains = [int(input()) for _ in range(N)]

# Calculating result
print(min_villains_to_remove(N, M, H, villains))
