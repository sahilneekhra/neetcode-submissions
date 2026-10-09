class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                box_idx = (i // 3) * 3 + (j // 3)

                if (value in row[i] or
                    value in col[j] or
                    value in box[box_idx]):
                    return False

                row[i].add(value)
                col[j].add(value)
                box[box_idx].add(value)

        return True