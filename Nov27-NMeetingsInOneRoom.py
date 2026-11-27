class Meetings:
    def __init__(self, start:int, end:int, position:int) -> None:
        self.st = start
        self.en = end
        self.pos = position

class Solution:
    def n_meetings_in_one_room(self, start:list[int], end:list[int]) -> int:
        
        n = len(start)
        meet = [Meetings(start[i], end[i], i+1) for i in range(n)] #i+1 cause I am keeping position 1 not index 0.
        meet.sort(key = lambda x: (x.en, x.st))

        result = [meet[0].pos]
        count = 1
        lastTime = meet[0].en

        for i in range(1,n):
            if meet[i].st > lastTime:
                count += 1
                result.append(meet[i].pos)
                lastTime = meet[i].en

        return count

solver = Solution()
start = list(map(int, input("Enter the start values : ").split()))
end = list(map(int, input("Enter the end values : ").split()))
result = solver.n_meetings_in_one_room(start, end)
print(f"Output : {result}")

"""
Enter the start values : 1 3 0 5 8 5
Enter the end values : 2 4 6 7 9 9
Output : 4
"""