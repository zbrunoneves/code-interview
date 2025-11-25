import heapq

def top_k_elements(nums: list[int], k: int) -> list[int]:
    h={}
    for n in nums:
        h[n] = h.get(n, 0)
        h[n] += 1

    heap = []
    for n, count in h.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, n))
        else:
            heapq.heappushpop(heap, (count, n))

    return [x[1] for x in heap]