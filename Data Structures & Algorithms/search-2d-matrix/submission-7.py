class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_row = len(matrix)
        num_col = len(matrix[0])
        
        start_index = 0
        end_index = num_row * num_col - 1
        while(start_index +1 < end_index):
            mid_index = (start_index + end_index)//2

            print(f"{start_index} and {end_index}")
            r = mid_index //num_col
            c = mid_index % num_col
            print(r,c)
            if matrix[r][c] < target:
                start_index = mid_index
            elif matrix[r][c] > target:
                end_index = mid_index

            elif matrix[r][c] == target:
                return True

        if matrix[start_index//num_col][start_index % num_col] == target:
            return True 
        elif matrix[end_index//num_col][end_index % num_col] == target:
            return True
        else:
            return False  