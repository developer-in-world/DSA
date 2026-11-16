class Solution:
    def brute_force(self, fruits):
        n = len(fruits)
        max_length = 0

        for i in range(n):
            my_set = set()
            for j in range(i, n):
                my_set.add(fruits[j])
                if len(my_set) > 2:
                    break
                max_length = max(max_length, j-i+1)

        return max_length

    def better_solution(self, fruits):
        left, right = 0, 0
        n = len(fruits)
        max_length = 0
        my_dict = {}

        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1

            while len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1

            if len(my_dict) <= 2:
                max_length = max(max_length, right - left + 1)
            right += 1

        return max_length

    def optimal(self, fruits):
            left, right = 0, 0
            n = len(fruits)
            max_length = 0
            my_dict = {}
    
            while right < n:
                my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1
    
                if len(my_dict) > 2:
                    my_dict[fruits[left]] -= 1
                    if my_dict[fruits[left]] == 0:
                        del my_dict[fruits[left]]
                    left += 1
    
                if len(my_dict) <= 2:
                    max_length = max(max_length, right - left + 1)
                right += 1
    
            return max_length
    


solver = Solution()
nums = list(map(int, input("Enter the list of fruits : ").split()))
result = solver.optimal(nums)
print(f"Output : {result}")
