import bisect

def search(array, n):
    start_pos = 0
    end_pos = len(array) - 1
    found = False
    
    while not found:
        pos = 0
        
        mid_pos = (start_pos + end_pos)//2
        q = array[mid_pos]
        if start_pos > end_pos: break

        if q == n:
            i = 1
            while True:
                try:
                    prev_mid = mid_pos - i
                    q_prev_neighbour = array[prev_mid]
                    if q == q_prev_neighbour:
                        i += 1
                    else:
                        pos = prev_mid + 1
                        found = True
                        break
                except IndexError:
                    pos = mid_pos
                    found = True
                    break
        else:
            if n < q:
                end_pos = mid_pos - 1
            else:
                start_pos = mid_pos + 1
        
    return n, found, pos + 1
    
if __name__ == '__main__':
    case_num = 1
    while True or case_num <= 65:
        
        N, Q = input().split(" ")
        N, Q = int(N), int(Q)
        if not(N and Q): break
        
        print(f"CASE# {case_num}:")
        marbles = []
        for i in range(N):
            n = int(input())
            bisect.insort(marbles, n)
        
        for i in range(Q):
            q, found, idx = search(marbles, int(input()))
            if not found: print(f"{q} not found"); continue;
            print(f"{q} found at {idx}")
        
        case_num += 1
