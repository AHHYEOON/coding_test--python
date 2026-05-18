def solution(brown, yellow):
    
    for yh in range(1,yellow+1):
        if yellow % yh == 0:
            yw = yellow // yh
            if yh > yw:
                break;
            if (yw+2) * 2 + 2 * yh == brown:
                return [yw+2,yh+2]
        
            
        
            