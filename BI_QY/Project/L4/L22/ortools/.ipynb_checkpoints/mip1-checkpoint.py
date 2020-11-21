from ortools.linear_solver import pywraplp

# 设置MIP问题解析引擎 SCIP
solver = pywraplp.Solver.CreateSolver('SCIP')

# 变量X Y均为非负
infinity = solver.infinity()
x = solver.IntVar(0.0, infinity, 'x')
y = solver.IntVar(0.0, infinity, 'y')
print('变量数量：', solver.NumVariables())

# 设置约束条件
solver.Add(x + 7 * y <= 17.5)
solver.Add(x <= 3.5)
print('约束的数量：', solver.NumConstraints())

# 求解最大值问题
solver.Maximize(x + 10 * y)
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('目标值 =', solver.Objective().Value())
    print('x =', x.solution_value())
    print('y =', y.solution_value())
else:
    print('问题没有最优解')

# 显示solve额外信息
print('执行时间（毫秒）',solver.wall_time())
print('Iteration: ',solver.iterations())
print('branch-and-bound nodes: ', solver.nodes())
