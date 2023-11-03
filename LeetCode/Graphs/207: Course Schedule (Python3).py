class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Creating a hashmap for the number of courses with an empty array to store their prereqs
        preMap = { i:[] for i in range(numCourses)}

        #Append the prereqs to the courses in preMap
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        #Create visitSet = store all courses along the current DFS path (will detect infinte prereq Loop (FALSE))
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False #We have already visist this course on this path == False
            if preMap[course] == []:
                return True #We can complete it since this course has no prereqs to take before it
            
            visitSet.add(course) #If base cases don't pass, we want to add course to our set

            for pre in preMap[course]: #We now iterate through every prereq of the current course
                if not dfs(pre): return False #if the course can't be taken, return false immediately

            visitSet.remove(course) #We verified its a course that can be taken, so remove it from set since we are starting new DFS branch
            preMap[course] = [] #update original hashmap so we can easily return True case

            return True

        #Have to create for loop to iterate through all course incase graph isn't connected
        for course in range(numCourses):
            if not dfs(course): return False

        return True

        
#TIME COMPLEXITY: O(N + # of prereqs)
