class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #hahsmap to store the count of unique fruits
        count = collections.defaultdict(int) # Fruit Type -> Count in Baskets
        l, total, res = 0, 0, 0 

        #Iterate through the length of fruits until we get more than 2 unique fruits
        for r in range(len(fruits)):
            count[fruits[r]] += 1 
            total += 1

            #Start decrementing from the left until only two unique fruits are left
            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -=1
                l += 1

                #Remove left fruit from hashmap if it becomes 0 so count is 2
                if not count[f]:
                    count.pop(f)
                
            res = max(res, total)

        return res
