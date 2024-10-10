from ortools.linear_solver import pywraplp
import pandas as pd
def Tuglpexample():
   # Define Solver
   solver = pywraplp.Solver.CreateSolver('GLOP')
   if not solver:
       return
   #Define Variables non-negativite
   #Para resolver esse problema de Maximização de Lucro/h
   #os valores de x se referem ao número de vezes que cada procecdimento é feito
   # x1 = Envelopamento de fios
   # x2 = Escova Nutritiva
   # x3 = Nanocristalização
   # x4 = Hidratação
   #1680 = 28 horas
   x1 = solver.NumVar(0, solver.infinity(), 'x1')
   x2 = solver.NumVar(0, solver.infinity(), 'x2')
   x3 = solver.NumVar(0, solver.infinity(), 'x3')
   x4 = solver.NumVar(0, solver.infinity(), 'x4')

   print('Número de variáveis =', solver.NumVariables())
   #Define Constraints
   solver.Add(90*x1 + 85*x2 + 70*x3 + 50*x4 <= 1680 , name='R1')
   solver.Add(x1 >= 2, name='R2')
   solver.Add(x2 >= 1,  name='R3')
   solver.Add(x3 >= 1, name='R4')

   print('Número de restrições =', solver.NumConstraints())

   #Define Objective Function
   solver.Maximize(59.33*x1 + 62.96*x2 + 78.86*x3 + 95.52*x4)
   
   #Invoke Solver
   status = solver.Solve()

   #Display the solution
   if status == pywraplp.Solver.OPTIMAL :
       print('Solução')
       print('Valor Objetivo =', round(solver.Objective().Value(), 2))
       for var in solver.variables():
           print(var.name(), '=', round(var.solution_value(), 2))

   else :
       print('O Problema não tem solução ótima')

   print('-----------------------------------------------------------')
   print('Análise de Sensibilidade:')
   activities = solver.ComputeConstraintActivities()
   o = [{'Nome': c.name(), 'Preço Sombra': c.dual_value(), 'Folga': c.ub() - activities[i]} for i, c in
        enumerate(solver.constraints())]
   print((pd.DataFrame(o).round(2)))
   print('-----------------------------------------------------------')
   print('Uso avançado:')
   print('Problema resolvido em %.2f ms' % solver.wall_time())
   print('Problema resolvido em %d iterações' % solver.iterations())

Tuglpexample()