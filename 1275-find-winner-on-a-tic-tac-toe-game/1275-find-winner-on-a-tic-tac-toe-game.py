class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        res = [[0,0,0], [0,0,0], [0,0,0]]
        
        for i in range(len(moves)):
            if i%2==0:
                res[moves[i][0]][moves[i][1]] += 1
            else:
                res[moves[i][0]][moves[i][1]] -= 1

        if [1,1,1] in res or (res[0][0]==1 and res[1][1]==1 and res[2][2]==1) or (res[0][2]==1 and res[1][1]==1 and res[2][0]==1) or (res[0][0]==1 and res[1][0]==1 and res[2][0]==1) or (res[0][1]==1 and res[1][1]==1 and res[2][1]==1) or (res[0][2]==1 and res[1][2]==1 and res[2][2]==1):
            return "A"

        elif [-1,-1,-1] in res or (res[0][0]==-1 and res[1][1]==-1 and res[2][2]==-1) or (res[0][2]==-1 and res[1][1]==-1 and res[2][0]==-1) or (res[0][0]==-1 and res[1][0]==-1 and res[2][0]==-1) or (res[0][1]==-1 and res[1][1]==-1 and res[2][1]==-1) or (res[0][2]==-1 and res[1][2]==-1 and res[2][2]==-1):
            return "B"

        elif len(moves)==9:
            return "Draw"

        else:
            return "Pending"