# -*- coding: utf-8 -*-
'''
因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
跳1级，剩下n-1级，则剩下跳法是f(n-1)
跳2级，剩下n-2级，则剩下跳法是f(n-2)
所以f(n)=f(n-1)+f(n-2)+...+f(1)
因为f(n-1)=f(n-2)+f(n-3)+...+f(1)
所以f(n)=2*f(n-1)
然后求解这个无穷级数的和：
思考一
因为：
f(n)=2*f(n-1)
f(n-1)=2*f(n-2)
...
f(2)=2*f(1)
f(1)=2^0
所以：
Σ=f(n)+f(n-1)+...f(2)+f(1)
  =2^(n-1)


'''
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)
        #pow(2,number-1)也可以