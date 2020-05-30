from heapq import heappush, heappop, heapify

def sort_k_lists(lists):
    result, heap = [], []
    # # Create a heap for first element of every list
    # for i,curr_list in enumerate(lists):
    #     if curr_list:
    #         heap.append((curr_list[0], i, 0))
    heap = [(curr_list[0], i, 0) for i, curr_list in enumerate(lists) if curr_list]
    heapify(heap)

    while heap:
        curr_min, curr_list_i, curr_ele_i =  heappop(heap)
        result.append(curr_min)
        if curr_ele_i + 1 < len(lists[curr_list_i]):
            next_heap_entry = (lists[curr_list_i][curr_ele_i+1], curr_list_i, curr_ele_i + 1)
            heappush(heap, next_heap_entry)

    return result
