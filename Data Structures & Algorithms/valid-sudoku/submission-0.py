class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for j in range(9):
                if board[j][col] == ".":
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])

        for st_row in range(0, 9, 3): # iterate over the indexes a box can start for a row
            for st_col in range(0, 9, 3): # iterate over the indexes a box can start for a column
                seen = set()

                for cur_row in range(st_row, st_row + 3): # iterate thru each trio of indexes
                    for cur_col in range(st_col, st_col + 3):
                        if board[cur_row][cur_col] == ".":
                            continue
                        if board[cur_row][cur_col] in seen:
                            return False
                        seen.add(board[cur_row][cur_col])

        return True