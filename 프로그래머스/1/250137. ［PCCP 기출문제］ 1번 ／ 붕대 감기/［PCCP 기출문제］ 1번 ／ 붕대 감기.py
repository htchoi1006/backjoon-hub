def solution(bandage, health, attacks):
    attack_time = []
    for time, damage in attacks:
        attack_time.append(time)
    
    max_health = health
    idx = 0
    cnt = 0
    
    for i in range(attacks[0][0], attacks[-1][0]+1):
        if i in attack_time:
            health -= attacks[idx][1]
            if health <= 0:
                return -1
            idx += 1
            cnt = 0
            # print(health)
        else:
            if health < max_health:
                health = min(health + bandage[1], max_health)
                cnt += 1
                if cnt == bandage[0]:
                    health = min(health + bandage[2], max_health)
                    cnt = 0
            # print(health)
            
    if health > 0:
        return health
    else: 
        return -1 