from collections import deque

def lru(pages, capacity):
    mem = deque(); hits = faults = 0
    for p in pages:
        if p in mem:
            hits += 1; mem.remove(p); mem.append(p)
        else:
            faults += 1
            if len(mem) >= capacity: mem.popleft()
            mem.append(p)
        print("메모리:", list(mem))
    print("히트:", hits, "폴트:", faults)

if __name__ == "__main__":
    lru([1,2,3,1,4,5,2,1,2,3,4,5], 3)