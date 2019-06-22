# Rain-Water-Storage-2D-Problem

Leetcode 407. Trapping Rain Water Problem-2

Q) Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

The main intention of the problem is that, if we pour water from space on any object, how much of water does the object store? The object is a cuboid where it is constructed using blocks. Input is given in a 2*2 matrix format. ex[[3,3,3],[3,1,3],[3,3,3]]. Here in the given example, If I pour water from space, 2 units of water gonna store in middle block. After that, water gonna leak. So, the total storage gonna be 2. If the input matrix has 0 in middle, then there won't be any water storage since if we pour water from space, water gonna leak from middle since there's no block.

![alt text](https://assets.leetcode.com/uploads/2018/10/13/rainwater_empty.png)
