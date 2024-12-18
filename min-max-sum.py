arr = [1, 2, 3, 4, 5]

def calc_sum_recursive(
    arr,
    count, 
    start = 0,
    current_sum = 0
):
    if count == 0:
        return [current_sum] 

    results = []
    for i in range(start, len(arr)):
            results.extend(
                calc_sum_recursive(
                    arr,
                    count - 1,
                    i + 1,
                    arr[i] + current_sum 
                )
            )
    return results 
    
def miniMaxSum(arr):
    results = calc_sum_recursive(arr, 4)

    print(str(min(results)) + " " + str(max(results)))

miniMaxSum(arr)