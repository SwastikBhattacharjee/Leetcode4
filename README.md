# Median of Two Sorted Arrays (LeetCode #4)

Find the median of two sorted arrays.

## Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (min(m, n)))`.

## Solution

Here is the Python solution for the Median of Two Sorted Arrays problem:

```py
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
        else:
            return nums[len(nums) // 2]
```


## Test Cases

To ensure the solution works correctly, here are some test cases:

- **Test Case   1:**
```
Input: nums1 = [1,2], nums2 = [3,4]; Output: 2.5
```

- **Test Case   2:**
```
Input: nums1 = [1,2], nums = [3]; Output: 2
```

- **Test Case   3:**
```
Input: nums1 = [1,2], nums2 = []; Output: 1.5
```

- **Test Case   4:**
```
Input: nums1 = [1,2,3,4], nums2 = [5,6]; Output: 3
```


## Usage

To run the solution locally, follow these steps:

1. Save the above Python code in a file named `median_of_two_sorted_arrays.py`.
2. Open a terminal and navigate to the directory containing the `median_of_two_sorted_arrays.py` file.
3. Execute the Python file using the command `python median_of_two_sorted_arrays.py`.

## License

This project is licensed under the terms of the MIT license.

---

For any feedback or improvements, feel free to contribute to this repository.
