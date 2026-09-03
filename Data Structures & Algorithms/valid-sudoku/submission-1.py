class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        boxes=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue

                #rows
                if val in rows[r]:
                    return False
                rows[r].add(val)

                #cols
                if val in cols[c]:
                    return False
                cols[c].add(val)

                #boxes
                box_index=(r//3,c//3)
                if val in boxes[box_index]:
                    return False
        
                boxes[box_index].add(val)
        return True        

                       

        