import heapq

def build_heap(arr, d):
    # Create a min-heap from the given array
    heapq.heapify(arr)
    return arr

def insert_into_heap(heap, x, d):
    heapq.heappush(heap, x)

def delete_min_from_heap(heap, d):
    return heapq.heappop(heap)

def level_order_traversal(heap):
    return heap

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    
    n = int(data[index])
    index += 1
    d = int(data[index])
    index += 1
    
    heap = []
    for _ in range(n):
        heap.append(int(data[index]))
        index += 1
    
    elements_to_insert = []
    while index < len(data) and data[index] != '#':
        elements_to_insert.append(int(data[index]))
        index += 1
    index += 1  # Skip the '#'
    x = int(data[index])
    
    # Build the initial heap
    heap = build_heap(heap, d)
    
    # Insert the element x into the heap
    insert_into_heap(heap, x, d)
    
    # Delete the min element from the heap
    min_element = delete_min_from_heap(heap, d)
    
    print(f"min = {min_element}")
    
    # Output the level-order traversal of the heap
    traversal_result = level_order_traversal(heap)
    
    for elem in traversal_result:
        print(elem)

if __name__ == "__main__":
    main()
