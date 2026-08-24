class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        box_size = int(n ** 0.5)
        print(rows,box_size)
        for r in range(n):
            for c in range(n):

                value = board[r][c]
                
                if value == ".":
                    continue
                if value in rows[r]:
                    return False

                if value in cols[c]:
                    return False
                print(r // box_size,c // box_size,(r // box_size) * box_size + (c // box_size))
                box = (r // box_size) * box_size + (c // box_size)

                if value in boxes[box]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)



        return True