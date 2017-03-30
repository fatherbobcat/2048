# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 01:12:52 2017

@author: lsha
"""

# AI Manager to detail AI to solve 2048 puzzle

from BaseAI import BaseAI
import time
import sys
from threading import Thread

class PlayerAI(BaseAI):
   
    nextMove = None
    startTime = None
    
    def getMove(self, grid):
        
        sys.setrecursionlimit(10000)
        thread = Thread(target=self.maximize,args = (grid,))
        thread.start()
        #time.sleep(0.2)
        thread.join()
        print "end of thread"
       # maxTuple = self.maximize(grid)
        
        #!!!!!!!!!!need to translate end grid into the move we made
        #!!!!!!!!!need to implement a thread to stop it after time
        return nextMove
        
    
    def maximize(self, grid):
        #End State
        maxTuple = (None,float("-inf"))
    
        if not grid.canMove():
            return (None, self.utility(grid))
        else:
            moves = grid.getAvailableMoves()
            for x in moves:
                child = grid.clone()
                child.move(x)
                
                #utility = self.utility(child)                
                utility = self.minimize(child)[1]
                if utility > maxTuple[1]:
                    maxTuple = (child,utility)
                    global nextMove
                    nextMove = x
        #print "STOOOOOOOOOOOOOOp"    
        return maxTuple
    
    def minimize (self, grid):
        
        cells = grid.getAvailableCells()
        #End State
        if not cells:
            return (None, self.utility(grid))
        else:
            minTuple = (None,float("inf"))
            val = [2,4]
            for x in cells:
                for y in val:
                    child = grid.clone()
                    child.setCellValue(x,y)
                    utility = self.maximize(child)[1]
                    #utility = self.utility(child)
                    if utility < minTuple[1]:
                        minTuple = (child,utility)
        
        return minTuple
    
    #Calculates the utility of that number
    def utility(self, grid):
    
        #1 Highest tile number
        utility = grid.getMaxTile()
        
        #2 Position of highest tile number (corners)
        
        #3 Number of tiles on board
        
        
        return utility
    
    #Prints out the grid - for debugging
    def printGrid(self, grid):
        for i in xrange(grid.size):
            for j in xrange(grid.size):
                print "%6d  " % grid.map[i][j],
            print ""
        print ""
    
            