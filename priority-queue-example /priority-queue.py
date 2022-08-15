import heapq


class Queue:

    @staticmethod
    def sort_queue(tasks):
        q = []
        for task in tasks:
            heapq.heappush(q, task)

        return [heapq.heappop(q) for i in reversed(range(len(q)))]


print(Queue().sort_queue(['task19', 'task10', 'task2', 'task1']))
