def maximumProfit(self, prices):
        if not prices:
            return 0
        i=0
        j=1
        max_prof=0
        while j<len(prices):
            if prices[j]>prices[i]:
                max_prof = max(max_prof, prices[j] - prices[i])
            else:
                i=j
            j+=1
        return max_prof