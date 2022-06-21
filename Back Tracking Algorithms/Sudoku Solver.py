from collections import defaultdict


class Solve:
    def __init__(self):
        self.solved = []

    def solveSudoku(self, boards) -> None:
        h = defaultdict(set)  # track the digits already present in each of the 9 sub-boxes
        rows, cols = defaultdict(set), defaultdict(set)  # track the digits already present in each row and column
        for i in range(9):
            for j in range(9):
                if boards[i][j] != '.':
                    h[3 * (i // 3) + j // 3].add(int(boards[i][j]))
                    rows[i].add(int(boards[i][j]))
                    cols[j].add(int(boards[i][j]))

        # helper function that makes use of backtracking
        def helper(row, col):
            if row == 9:
                for k in range(9):
                    self.solved.append(boards[k][:])
                return
            if boards[row][col] == '.':
                for num in range(1, 10):
                    if num not in h[(row // 3) * 3 + col // 3] and num not in rows[row] and num not in cols[col]:
                        boards[row][col] = str(num)
                        h[(row // 3) * 3 + col // 3].add(num)
                        rows[row].add(num)
                        cols[col].add(num)
                        if col == 8:  # move to the next row
                            helper(row + 1, 0)
                        else:
                            helper(row, col + 1)
                        h[(row // 3) * 3 + col // 3].remove(num)
                        rows[row].remove(num)
                        cols[col].remove(num)
                        boards[row][col] = '.'
            else:
                if col == 8:
                    helper(row + 1, 0)
                else:
                    helper(row, col + 1)

        helper(0, 0)
        # overwrite values
        for i in range(9):
            for j in range(9):
                boards[i][j] = self.solved[i][j]


sol = Solve()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

sol.solveSudoku(board)
print(board)

