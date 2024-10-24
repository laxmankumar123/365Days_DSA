


	def backtrack(start, current, current_sum):
            if current_sum == target:
                result.append(current[:])
                return
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i]) 
                backtrack(i, current, current_sum + candidates[i])
                current.pop()
            
        result = []
        backtrack(0, [], 0)
        return result
