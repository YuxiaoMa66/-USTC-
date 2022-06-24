from email import utils
import util

"""
Data sturctures we will use are stack, queue and priority queue.

Stack: first in last out
Queue: first in first out
    collection.push(element): insert element
    element = collection.pop() get and remove element from collection

Priority queue:
    pq.update('eat', 2)
    pq.update('study', 1)
    pq.update('sleep', 3)
pq.pop() will return 'study' because it has highest priority 1.

"""

"""
problem is a object has 3 methods related to search state:

problem.getStartState()
Returns the start state for the search problem.

problem.isGoalState(state)
Returns True if and only if the state is a valid goal state.

problem.getChildren(state)
For a given state, this should return a list of tuples, (next_state,
step_cost), where 'next_state' is a child to the current state, 
and 'step_cost' is the incremental cost of expanding to that child.

"""
def myDepthFirstSearch(problem):
    visited = {}
    frontier = util.Stack()

    frontier.push((problem.getStartState(), None))

    while not frontier.isEmpty():
        state, prev_state = frontier.pop()

        if problem.isGoalState(state):
            solution = [state]
            while prev_state != None:
                solution.append(prev_state)
                prev_state = visited[prev_state]
            return solution[::-1]                
        
        if state not in visited:
            visited[state] = prev_state

            for next_state, step_cost in problem.getChildren(state):
                frontier.push((next_state, state))

    return []

def myBreadthFirstSearch(problem):
    # YOUR CODE HERE
    visited = {}
    frontier = util.Queue()
    
    frontier.push((problem.getStartState(),None))

    while not frontier.isEmpty():
        state, prev_state = frontier.pop()

        if problem.isGoalState(state):
            solution = [state]
            while prev_state != None:
                solution.append(prev_state)
                prev_state = visited[prev_state]
            return solution[::-1]

        if state not in visited:
            visited[state] = prev_state

            for next_state, step_cost in problem.getChildren(state):
                frontier.push((next_state, state))

    return []

def myAStarSearch(problem, heuristic):
    # YOUR CODE HERE
    visited = {}
    frontier = util.PriorityQueue()
    h = heuristic(problem.getStartState())
    g = 0
    f = h + g
    frontier.update((problem.getStartState(), None, g), f)

    while not frontier.isEmpty():
        state, prev_state, g= frontier.pop()

        if problem.isGoalState(state):
            solution = [state]
            while prev_state != None:
                solution.append(prev_state)
                prev_state = visited[prev_state]
            return solution[::-1]

        if state not in visited:
            visited[state] = prev_state

            for next_state, step_cost in problem.getChildren(state):
                g_ = g + step_cost
                h = heuristic(next_state)
                f = h + g_
                frontier.update((next_state, state, g_), f)

    return []

"""
Game state has 4 methods we can use.

state.isTerminated()
Return True if the state is terminated. We should not continue to search if the state is terminated.

state.isMe()
Return True if it's time for the desired agent to take action. We should check this function to determine whether an agent should maximum or minimum the score.

state.getChildren()
Returns a list of legal state after an agent takes an action.

state.evaluateScore()
Return the score of the state. We should maximum the score for the desired agent.

"""
class MyMinimaxAgent():

    def __init__(self, depth):
        self.depth = depth

    def minimax(self, state, depth):
        if state.isTerminated():
            return None, state.evaluateScore()
        def Max_Score(state, currentDepth):
            currentDepth = currentDepth + 1 #当前深度加一
            if state.isTerminated() or currentDepth == depth:  #若当前状态已经赢了或输了 或者 已经到达了规定的深度
                return state.evaluateScore()
            v = -float('inf')               # 初始化v
            for ACT in state.getChildren():
                v = max(v, Min_Score(ACT, currentDepth))
            return v
        def Min_Score(state, currentDepth):
            if state.isTerminated():                # 若当前状态已经赢了或输了
                return state.evaluateScore()
            v = float('inf')
            for ACT in state.getChildren():     # 对每个max分支求min 其中有多个Ghost 所有多个Ghost分支
                if ACT.isMe():
                    v = min(v, Max_Score(ACT, currentDepth))
                else:
                    v = min(v, Min_Score(ACT, currentDepth))
            return v

        best_state, best_score = None, -float('inf') if state.isMe() else float('inf')

        for child in state.getChildren():
            # YOUR CODE HERE
            current_depth = 0
            current_best_score = Min_Score(child, current_depth)
            if current_best_score > best_score:
                best_score = current_best_score
                best_state = child
        return best_state, best_score

    def getNextState(self, state):
        best_state, _ = self.minimax(state, self.depth)
        return best_state

class MyAlphaBetaAgent():

    def __init__(self, depth):
        self.depth = depth
    def alphabeta(self, state, depth):
        if state.isTerminated():
            return None, state.evaluateScore()
        def Max_Score(state, currentDepth, alpha, beta):
            currentDepth = currentDepth + 1
            if state.isTerminated() or currentDepth == depth:
                return state.evaluateScore()
            v = -float('inf')
            for ACT in state.getChildren():
                v = max(v, Min_Score(ACT, currentDepth, alpha, beta))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v
        def Min_Score(state, currentDepth, alpha, beta):
            if state.isTerminated():
                return state.evaluateScore()
            v = float('inf')
            for ACT in state.getChildren():
                if ACT.isMe():
                    v = min(v, Max_Score(ACT, currentDepth, alpha, beta))
                else:
                    v = min(v, Min_Score(ACT, currentDepth, alpha, beta))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        best_state, best_score = None, -float('inf') if state.isMe() else float('inf')
        beta = float('inf')
        alpha = -float('inf')

        for child in state.getChildren():
            # YOUR CODE HERE
            current_depth = 0
            current_best_score = Min_Score(child, current_depth, alpha, beta)
            if current_best_score > best_score:
                best_score = current_best_score
                best_state = child
        return best_state, best_score
    
    def alphabeta(self, state, depth,alpha,beta):
        if state.isTerminated():
            return None, state.evaluateScore()

        best_state, best_score = None, -float('inf') if state.isMe() else float('inf')

        if depth == 0:
           best_state,best_score = state,state.evaluateScore()
        elif depth > 0:
            for child in state.getChildren():
            # YOUR CODE HERE
                child_state, child_score = self.alphabeta(child,depth-1 if child.isMe() else depth,alpha,beta)
                if state.isMe():     # 若当前状态是自己
                    if alpha <= child_score:
                        best_state = child
                        alpha = child_score
                        best_score = alpha
                    if beta < alpha:
                        break
                else:                # 若当前状态是Ghost
                    if beta >= child_score:
                        best_state = child
                        beta = child_score
                        best_score = beta
                    if beta < alpha:
                        break
        return best_state, best_score

    def getNextState(self, state):
        beta = float('inf')
        alpha = -float('inf')
        best_state, _ = self.alphabeta(state, self.depth, alpha, beta)
        return best_state
