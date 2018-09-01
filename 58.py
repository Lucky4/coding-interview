class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1_length = len(nums1)
        nums2_length = len(nums2)

        is_odd = False
        if (nums1_length + nums2_length) % 2 != 0:
            is_odd = True

        median_num = (nums1_length + nums2_length) / 2 + 1

        tmp_arr = []
        num1_index = 0
        num2_index = 0
        while num1_index < nums1_length and num2_index < nums2_length:
            if nums1[num1_index] <= nums2[num2_index]:
                tmp_arr.append(nums1[num1_index])
                num1_index += 1
            else:
                tmp_arr.append(nums2[num2_index])
                num2_index += 1
            
            if len(tmp_arr) == median_num:
                break

        if len(tmp_arr) < median_num:
            while num1_index < nums1_length:
                tmp_arr.append(nums1[num1_index])
                num1_index += 1
                if len(tmp_arr) == median_num:
                    break

            while num2_index < nums2_length:
                tmp_arr.append(nums2[num2_index])
                num2_index += 1
                if len(tmp_arr) == median_num:
                    break

        if is_odd:
            return tmp_arr[len(tmp_arr) - 1]
        return (tmp_arr[len(tmp_arr) - 1] + tmp_arr[len(tmp_arr) - 2]) / 2.0
