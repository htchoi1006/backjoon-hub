def solution(video_len, pos, op_start, op_end, commands):
    
    now = int(pos[:2])*60 + int(pos[3:])
    start = int(op_start[:2])*60 + int(op_start[3:])
    end = int(op_end[:2])*60 + int(op_end[3:])
    length = int(video_len[:2])*60 + int(video_len[3:])
    
    
    if start <= now <= end:
        now = end
    
    for i in commands:
        if i == 'prev':
            now -= 10
            if now < 0:
                now = 0
            if start <= now <= end:
                now = end

        if i == 'next':
            now += 10
            if now > length:
                now = length
            if start <= now <= end:
                now = end
        
            
    minute = now//60
    second = now%60
    
    return f"{minute:02d}:{second:02d}"

    