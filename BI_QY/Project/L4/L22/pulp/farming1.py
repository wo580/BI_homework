import pulp
import numpy as np
from pprint import pprint

# 定义运输问题
def transportation_problem(costs, x_max, y_max):
    row = len(costs)
    col = len(costs[0])
    print(f'row:{row} col:{col}')
    # 定义初始问题
    prob = pulp.LpProblem('Transportation', sense=pulp.LpMaximize)
    # 定义相关变量
    var = [[pulp.LpVariable(f'x{i}{j}', lowBound=0, cat=pulp.LpInteger) for j in range(col)] for i in range(row)]
    # 递归展开列表
    flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
    print('var=', var)
    print('flatten=', flatten)
    print('var[1]', var[1])
    # 定义目标函数 （单价* {ij}运量）
    prob += pulp.lpDot(flatten(var), costs.flatten())
    # 定义约束条件
    for i in range(row):
        prob += pulp.lpSum(var[i]) <= x_max[i]
    for j in range(col):
        prob += pulp.lpSum([var[i][j] for i in range(row)]) <= y_max[j]

    prob.solve()
    result = {'objective':pulp.value(prob.objective), \
              'var': [[pulp.value(var[i][j]) for j in range(col)] for i in range(row)]}
    return result

# 解决具体问题
if __name__ == '__main__':
	# 设置单价成本：4个工厂，6个销售地
    costs = np.array([[500, 550, 630, 1000, 800, 700],
                      [800, 700, 600, 950, 900, 930],
                      [1000, 960, 840, 650, 600, 700],
                      [1200, 1040, 980, 860, 880, 780]])
    # 工厂最大产量
    max_plant = [76, 88, 96, 40]
    # 销售地需求量
    max_cultivation = [42, 56, 44, 39, 60, 59]
    # 使用线性规划
    result = transportation_problem(costs, max_plant, max_cultivation)
	# 输出结果
    print(f'最大值为{result["objective"]}')
    print('各变量的取值为：')
    pprint(result['var'])