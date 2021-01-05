
def solution(s):
    # Type your solution here
    if len(s) < 1:
        return 0
    
    max_l = 1
    length = 1
    visited = {}
    visited[s[0]] = 1
    window = [0,1]
    
    while (window[0] < len(s) and window[1] < len(s)):
        if visited.get(s[window[1]]) != None and visited.get(s[window[1]]) > 0:
            window[0] += 1
            visited[s[window[1]]] = 0
        else:
            visited[s[window[1]]] = 1
            window[1] += 1
            length = window[1] - window[0]
        
        max_l = max(length,max_l)
        
    return max_l