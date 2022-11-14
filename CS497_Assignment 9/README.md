2.  Maximum Subarray
    arr[i] represents the largest sum of all subarrays ending with index i...
    then its value should be the larger one between nums[i]...
    arr[i-1] + nums[i] (largest sum plus current number with using prefix)...
    calculate arr[0], arr[1]…, arr[n] while comparing each one with current largest sum...
    if arr[i] > maxSum then maxSum = arr[i].
    Time complexity: O(n)
3.  Unique Path
    Using dynamic programing, setting up a whole new table with the last row and col having 1.
    Then I will loop backward through the col
    `newRow[j]=newRow[j+1]+row[j]`
    Time complexity: O(m\*n)

4.  Unique Path II
    Using dynamic programing, setting up a whole new table with the first row and col having 1.
    If it is contain a 1 in the obstacle table, then change that value and the value after it to 0
    Loop through the table and using this algorthym:
    `obstacleGrid[i,j] = obstacleGrid[i-1,j] + obstacleGrid[i,j-1]`
    Time complexity: O(m\*n)
