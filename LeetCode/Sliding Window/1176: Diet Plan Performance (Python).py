class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        points = 0
        total_calories = sum(calories[:k])

        if total_calories < lower:
            points -= 1
        elif total_calories > upper:
            points += 1

        for i in range(k, len(calories)):
            total_calories += calories[i] - calories[i - k]

            if total_calories < lower:
                points -= 1
            elif total_calories > upper:
                points += 1
    
        return points
