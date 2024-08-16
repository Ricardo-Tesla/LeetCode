def isValidSudoku(board):
    # Initialize sets to track seen numbers in rows, columns, and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    # Iterate over each cell in the board
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue
            
            # Check the row
            if num in rows[r]:
                return False
            rows[r].add(num)
            
            # Check the column
            if num in cols[c]:
                return False
            cols[c].add(num)
            
            # Check the box
            box_index = (r // 3) * 3 + (c // 3)
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)
    
    return True

# Example 1
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board1))  # Output: True

# Example 2
board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board2))  # Output: False
