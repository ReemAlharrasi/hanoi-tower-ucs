# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:49:21 2023
comp3600/20
assignment 1
name:Reem Al Harrasi
id:126146
"""
#importing heapq to use priority queue
import heapq

#variables for design purposes
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
def UCS(start, goal, space):
    #initialize variables
    explored = set()
    frontier = [(0, start, [])]#add start to frontier with cost=0
    iteration=0
    #while frontier is not empty
    while frontier:
        #print iteration's frontier and explored
        print('\niteration number: ',iteration)
        print(line,'frontier',line)
        for i in frontier:
            print(i)
        print(line,'explored',line)
        print(explored,'\n\n')
        
        #pop out the state with the least cost
        cost, current, path =heapq.heappop(frontier)
        
        if current == goal:
            return path, cost #stop if current state is the goal
        
        if current not in explored: #explore current's neighbors and add it explored set if it is not there already
            explored.add(current)
            for item in space[current]: #get nighbors of the current state
                neighbor=item[0] #get neighbor
                neighborcost=item[1] #get neighbor cost
                newcost=cost + neighborcost #calculate new cumulative cost
                newpath=path + [(current, neighbor)] #path from start to neighbor
                #add to frontier the new neighbor with new cost and the path as a tuple
                if neighbor not in explored:
                    heapq.heappush(frontier, (newcost, neighbor, newpath))
        iteration+=1
    #return none for pathand cost if the goal state is not found
    return None,None


#ask user for start and goal state
print(' '*40,'  hanoi tower puzzle')
print(line,'possible start and goal',line)
for i in space:
    print(i , end='    ')
start=input('\n\nchoose a start state and a goal state from above\nwrite it exactly the same with capital letters\n(Tip:copy and paste from above)\nstart>> ').strip()
goal=input('goal>> ').strip()
print()#skip line: for output design purposes
#call function
path,cost = UCS(start, goal, space)
#print depending on whether we got a solution or not
if path==None:
    print('\n\nsolution does not exist')
else:
    print('\n\nshortest path obtained:')
    for i in path:
        print(i[0],end='  >  ')
    print(i[1])
    print('\ncost:',cost)
