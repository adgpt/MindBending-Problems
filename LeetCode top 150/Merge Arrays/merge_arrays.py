def merge_arrays(nums1, m, nums2, n):
    """
    Merge two sorted arrays nums1 and nums2 into a single sorted array in-place.

    Args:
    nums1 (List[int]): First sorted array with extra space for nums2.
    m (int): Number of valid elements in nums1.
    nums2 (List[int]): Second sorted array.
    n (int): Number of elements in nums2.
    """
    last_index = m + n - 1
    index1 = m - 1
    index2 = n - 1

    while index2 >= 0:
        if index1 >= 0 and nums1[index1] > nums2[index2]:
            nums1[last_index] = nums1[index1]
            index1 -= 1
        else:
            nums1[last_index] = nums2[index2]
            index2 -= 1

        last_index -= 1

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3

merge_arrays(nums1, m, nums2, n)

print("Merged array:", nums1)

