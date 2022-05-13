#우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제(Python)
import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 삽입
    for value in iterable:
        heapq.heappush(h, value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result


arr = [3, 2, 5, 4, 7, 1]

res = heapsort(arr)

print(res)

# max heap 사용할 때는 