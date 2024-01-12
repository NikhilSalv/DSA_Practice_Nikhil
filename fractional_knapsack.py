

class Fractional_Knapsack:
    def getMaxValues(weight,profits,capacity):
        index = list(range(len(profits)))

        # List of ratios of profits to weights

        ratio = [p/w for p,w in zip(profits,weight)]

        # Index will be sorted in ascending order as per ratio

        index.sort(key= lambda i : ratio[i], reverse=True)

        max_value = 0
        fractions = [0]*len(profits)

        for i in index:
            if weight[i] <= capacity:
                fractions[i] = 1
                max_value += profits[i]
                capacity = capacity - weight[i]
            else:
                fractions[i] = capacity/weight[i]
                max_value = profits[i]*capacity/weight[i]
                break
        return max_value, fractions
    

wt = [5,10,12,4,7,9,3]
profits = [25,75,100,50,45,90,30]
capacity = 37
maxProfit, x = Fractional_Knapsack.getMaxValues(wt,profits,capacity)
print("Max profit in Fractional ", maxProfit)
print("Fractions are : ", x, end=" ")
