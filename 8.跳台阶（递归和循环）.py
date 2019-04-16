# -*- coding: utf-8 -*-
'''
对于本题,前提只有 一次 1阶或者2阶的跳法。
a.如果两种跳法，1阶或者2阶，那么假定第一次跳的是一阶，那么剩下的是n-1个台阶，跳法是f(n-1);
b.假定第一次跳的是2阶，那么剩下的是n-2个台阶，跳法是f(n-2)
c.由a\b假设可以得出总跳法为: f(n) = f(n-1) + f(n-2) 
d.然后通过实际的情况可以得出：只有一阶的时候 f(1) = 1 ,只有两阶的时候可以有 f(2) = 2
e.可以发现最终得出的是一个斐波那契数列：
        
        | 1, (n=1)
f(n) =  | 2, (n=2)
        | f(n-1)+f(n-2) ,(n>2,n为整数)

一节：一种
二节：两种
三节：三种
四节：五种（两节的跳法然后再跳一个2，三节的跳法再跳一个1）

'''
class Solution:
    def jumpFloor(self, number):
        # write code here
        tmp = [1,2]
        while  len(tmp) <= number:
            tmp.append(tmp[-1] + tmp[-2])
        if number == 1:
            return 1
        else:
            return tmp[number-1]  
#如果不减1，num=2输出的就是第三个数以此类推