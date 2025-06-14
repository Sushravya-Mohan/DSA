class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows  # Initialize rows as a list of strings
        idx, d = 0, 1  # Start at the top row and move downward initially

        for char in s:
            rows[idx] += char  # Append character directly to the current row string
            # Change direction if at the top or bottom row
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        return "".join(rows)  # Join all rows into the final result string
