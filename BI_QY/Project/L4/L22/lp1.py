import numpy as np

# 默认求最小值
z = np.array([2, 3, 1])
a = np.array([[1, 4, 2], [3, 2, 0]])
b = np.array([8, 6])
# 取值范围
x1_bound = x2_bound = x3_bound =(0, None)
from scipy import optimize
# 默认约束条件都为 <=，如果要求大于等于，则取反
res = optimize.linprog(z, A_ub=-a, b_ub=-b,bounds=(x1_bound, x2_bound, x3_bound))
print(res)