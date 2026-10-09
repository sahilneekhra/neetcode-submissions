class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        box = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in row[i]:
                        row[i].append(board[i][j])
                    else:
                        return False
            for k in range(9):
                if board[k][i] != ".":
                    if board[k][i] not in col[i]:
                        col[i].append(board[k][i])
                    else:
                        return False
            for l in range(9):
                box_idx = l//3 + (3*(i//3))
                if board[i][l] != ".":
                    if board[i][l] not in box[box_idx]:
                        box[box_idx].append(board[i][l])
                    else:
                        return False
        return True

            
        