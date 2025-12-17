## Visual Example of In-Place Partition
```
Array: [64, 34, 25, 12, 22, 11, 90]
Pivot: 90 (last element)

Step 1: i = -1
        j = 0: 64 < 90? Yes → i=0, swap arr[0] with arr[0]
        [64, 34, 25, 12, 22, 11, 90]

Step 2: j = 1: 34 < 90? Yes → i=1, swap arr[1] with arr[1]
        [64, 34, 25, 12, 22, 11, 90]

Step 3: j = 2: 25 < 90? Yes → i=2, swap arr[2] with arr[2]
        [64, 34, 25, 12, 22, 11, 90]

Step 4: j = 3: 12 < 90? Yes → i=3, swap arr[3] with arr[3]
        [64, 34, 25, 12, 22, 11, 90]

Step 5: j = 4: 22 < 90? Yes → i=4, swap arr[4] with arr[4]
        [64, 34, 25, 12, 22, 11, 90]

Step 6: j = 5: 11 < 90? Yes → i=5, swap arr[5] with arr[5]
        [64, 34, 25, 12, 22, 11, 90]

Final: Place pivot at i+1 = 6
       Swap arr[6] with arr[6]
       [64, 34, 25, 12, 22, 11, 90]
       Pivot 90 is now at correct position  ← 9 bubbled to end
