# Explanation of the merge function

## Function Overview:
The `merge_arrays` function merges two sorted arrays `nums1` and `nums2` in-place. The input array `nums1` has extra space to hold all elements from both arrays.

## Key Components:
- **nums1:** The array that contains `m` valid elements followed by `n` zeros to accommodate the elements from `nums2`.
- **nums2:** The second array, which is sorted and contains `n` elements.
- **m and n:** Represent the number of valid elements in `nums1` and the length of `nums2` respectively.

## Approach:
The function starts merging from the end of both arrays. This prevents overwriting any elements in `nums1` before they are compared.

### Steps:
1. **Pointers Initialization:** 
   - `last_index` points to the last available position in `nums1`.
   - `index1` points to the last valid element in `nums1`.
   - `index2` points to the last element in `nums2`.

2. **Merging:** 
   - Compare the elements of `nums1` and `nums2` from the end.
   - Place the larger element at the position `last_index` in `nums1`.
   - Adjust the pointers (`index1`, `index2`, and `last_index`) accordingly.

3. **Result:** 
   - The result is stored in `nums1` itself.

### Example:
```
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
```

### Example Output:
```
Merged array: [1,2,2,3,5,6]
```

