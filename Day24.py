



candidates.sort()
        reslt1=[]
        def res(start ,current, current_sum):
            if current_sum==target:
                reslt1.append(current[:])
                return 
            if current_sum>target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                res(i+1 ,current, current_sum+candidates[i])
                current.pop()
        res(0 ,[], 0)
        return reslt1 
