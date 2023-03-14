# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:49:21 2023
comp3600/20
assignment 1
name:Reem Al Harrasi
id:126146
"""
#importing heapq to use prioroty queue
import heapq
line='_'*40
#put our tower of hanoi space set in a dictionary
space={'LMS,0,0':[('LM,0,S',1),('LM,S,0',1)],
           'LM,0,S':[('L,M,S',2),('LM,S,0',1),('LMS,0,0',1)],
           'LM,S,0':[('L,S,M',2),('LM,0,S',1),('LMS,0,0',1)],
           'L,M,S':[('L,MS,0',1),('LS,M,0',1),('LM,0,S',2)],
           'L,S,M':[('L,0,MS',1),('LS,0,M',1),('LM,S,0',2)],
           'L,MS,0':[('0,MS,L',3),('LS,M,0',1),('L,M,S',1)],
           'LS,M,0':[('L,MS,0',1),('LS,0,M',2),('L,M,S',1)],
           'LS,0,M':[('L,0,MS',1),('LS,M,0',2),('L,S,M',1)],
           'L,0,MS':[('0,L,MS',3),('LS,0,M',1),('L,S,M',1)],
           '0,MS,L':[('S,M,L',1),('0,M,LS',1),('L,MS,0',3)],
           '0,L,MS':[('S,L,M',1),('0,LS,M',1),('L,0,MS',3)],
           'S,M,L':[('S,0,LM',2),('0,M,LS',1),('0,MS,L',1)],
           '0,M,LS':[('M,0,LS',2),('S,M,L',1),('0,MS,L',1)],
           '0,LS,M':[('M,LS,0',2),('S,L,M',1),('0,L,MS',1)],
           'S,L,M':[('S,LM,0',2),('0,LS,M',1),('0,L,MS',1)],
           'S,0,LM':[('0,0,LMS',1),('0,S,LM',1),('S,M,L',2)],
           'M,0,LS':[('M,S,L',1),('MS,0,L',1),('0,M,LS',2)],
           'M,LS,0':[('MS,L,0',1),('M,L,S',1),('0,LS,M',2)],
           'S,LM,0':[('0,LMS,0',1),('0,LM,S',1),('S,L,M',2)],
           '0,0,LMS':[('0,S,LM',1),('S,0,LM',1)],
           '0,S,LM':[('M,S,L',2),('0,0,LMS',1),('S,0,LM',1)],
           'M,S,L':[('0,S,LM',2),('MS,0,L',1),('M,0,LS',1)],
           'MS,0,L':[('M,S,L',1),('MS,L,0',3),('M,0,LS',1)],
           'MS,L,0':[('M,L,S',1),('MS,0,L',3),('M,LS,0',1)],
           'M,L,S':[('0,LM,S',2),('MS,L,0',1),('M,LS,0',1)],
           '0,LM,S':[('0,LMS,0',1),('M,L,S',2),('S,LM,0',1)],
           '0,LMS,0':[('0,LM,S',1),('S,LM,0',1)]}


#creating a function for uniform cost algorithm 
def UCS(start_state, goal_state, space_set):
    #initialize needed libraries
    explored = set()
    queue = [(0, start_state, [])]
    while queue:
        x= heapq.heappop(queue)
        print(x)
        (cost, current_state, path) =x
        
        if current_state == goal_state:
            return path, cost
        if current_state not in explored:
            explored.add(current_state)
            for (child_state, child_cost) in space_set[current_state]:
                heapq.heappush(queue, (cost + child_cost, child_state, path + [(current_state, child_state)]))
    return None,None


#initialize our start and goal state and call the function
start = 'LMS,0,0'
goal = '0,0,LMS'
path,cost = UCS(start, goal, space)
if path==None:
    print('solution does not exist')
else:
    print('path:')
    for i in path:
        print(i[0])
    print('\ncost:',cost)
