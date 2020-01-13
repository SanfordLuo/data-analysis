"""
区别于Python的内建列表，数组的切片是原数组的视图。这意味着数据并不是被复制了，任何对于视图的修改都会反映到原数组上
如果你还是想要一份数组切片的拷贝而不是一份视图的话，你就必须显式地复制这个数组，例如arr[5：8].copy（）
"""
import numpy as np

arr01 = np.arange(10)
print("001\n", arr01)

arr01[5:8] = 12
print("002\n", arr01)

arr01_slice = arr01[5:8]
print("003\n", arr01_slice)

arr01_slice[1] = 12345
print("004\n", arr01)

arr01_slice[:] = 64
print("005\n", arr01)

arr02 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("006\n", arr02)
print("007\n", arr02[2])

arr03 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("008\n", arr03)
print("009\n", arr03[0])

# 切片
print("010\n", arr02[:2, 1:])
print("011\n", arr02[2, 1:])
print("012\n", arr02[:, :1])

"""
001
 [0 1 2 3 4 5 6 7 8 9]
002
 [ 0  1  2  3  4 12 12 12  8  9]
003
 [12 12 12]
004
 [    0     1     2     3     4    12 12345    12     8     9]
005
 [ 0  1  2  3  4 64 64 64  8  9]
006
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
007
 [7 8 9]
008
 [[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
009
 [[1 2 3]
 [4 5 6]]
010
 [[2 3]
 [5 6]]
011
 [8 9]
012
 [[1]
 [4]
 [7]]
"""