from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # boxy = 0
        # boxx = 0
        # box = list()
        for boxy in range(3):
            for boxx in range(3):
                box = list()
                for i in range(3):
                    for j in range(3):
                        # print(f"location: {i + boxy * 3},{j + boxx * 3}")
                        # print(board[i + boxy * 3][j + boxx * 3])
                        if board[i + boxy * 3][j + boxx * 3] in box and board[i + boxy * 3][j + boxx * 3] != ".":
                            return False
                        box.append(board[i + boxy * 3][j + boxx * 3])
                # print(box)

        for linex in range(9):
            box = list()
            for indexx in range(9):
                if board[linex][indexx] in box and board[linex][indexx] != ".":
                    return False
                box.append(board[linex][indexx])

        for liney in range(9):
            box = list()
            for indexy in range(9):
                if board[indexy][liney] in box and board[indexy][liney] != ".":
                    return False
                box.append(board[indexy][liney])

        return True
    
def main():
    sol = Solution()
    
    # Example 1
    board = [["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]
    output = sol.isValidSudoku(board)
    print(output) # True
    
    # Example 2
    board = [["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","1",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]
    output = sol.isValidSudoku(board)
    print(output) # False
    
if __name__ == "__main__":
    main()