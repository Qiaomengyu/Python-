# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:15:53 2019

@author: ASUS
"""

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0

思路：使用二分查找
1、设置一个首部指针low,一个尾部指针high，以及一个最小值初始值minVal
2、求出中间坐标middle，
 二分法核心：
若a[low]小于a[middle]，把low移到中间，否则将high移到中间
3、循环2，直到 high-low = 1，则最小值为a[high]
特殊情况：当数组为空时返回0，当数组有大量重复时，使用for循环普通方法找最小值
'''
class Solution:
    def fibonacci(self, n):
        # write your code here
        num = [0, 1]
#num是新的list
        #n == 0可以不要，默认没有0，位置从1开始
        if n == 0:
            return 0
        elif n == 1:
            return 0
        for i in range(2, n):	#从2到n不包含n
            num.append(num[-1] + num[-2])
        return num[-1]