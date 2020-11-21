from pulp import *
#import pulp

items = ['chicken', 'beef', 'mutton', 'rice', 'wheat', 'gel']
costs = {'chicken': 0.013, 
         'beef': 0.008, 
         'mutton': 0.010, 
         'rice': 0.002, 
         'wheat': 0.005, 
         'gel': 0.001}

protein = {'chicken': 0.100, 
            'beef': 0.200, 
            'mutton': 0.150, 
            'rice': 0.000, 
            'wheat': 0.040, 
            'gel': 0.000}

fat = {'chicken': 0.080, 
        'beef': 0.100, 
        'mutton': 0.110, 
        'rice': 0.010, 
        'wheat': 0.010, 
        'gel': 0.000}

fibre = {'chicken': 0.001, 
          'beef': 0.005, 
          'mutton': 0.003, 
          'rice': 0.100, 
          'wheat': 0.150, 
          'gel': 0.000}

salt = {'chicken': 0.002, 
         'beef': 0.005, 
         'mutton': 0.007, 
         'rice': 0.002, 
         'wheat': 0.008, 
         'gel': 0.000}

#创建问题实例，求最小极值
prob = LpProblem("The CatFood Problem", LpMinimize)

#构建Lp变量字典，变量名以item开头，如item_chicken，下界是0
item_vars = LpVariable.dicts("item", items, lowBound=0, upBound=100)
print(item_vars)

#添加目标方程
prob += lpSum([costs[i]*item_vars[i] for i in items])

#添加约束条件
prob += lpSum([item_vars[i] for i in items]) == 100
prob += lpSum([protein[i] * item_vars[i] for i in items]) >= 8.0
prob += lpSum([fat[i] * item_vars[i] for i in items]) >= 6.0
prob += lpSum([fibre[i] * item_vars[i] for i in items]) <= 2.0
prob += lpSum([salt[i] * item_vars[i] for i in items]) <= 0.4

#求解
prob.solve()
# 查看解的状态, “Not Solved”, “Infeasible”, “Unbounded”, “Undefined” or “Optimal”
print("Status:", LpStatus[prob.status])
#print('prob.status:', prob.status)
# 查看解
for i in items:
  print('{} = {}'.format(item_vars[i],item_vars[i].value()))
