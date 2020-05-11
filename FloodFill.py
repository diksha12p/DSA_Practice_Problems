from typing import List

"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image 
(from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value 
newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting 
pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels 
(also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels 
with the newColor.

At the end, return the modified image.

Example 1:

Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image

        # BFS Implementation
        fringe, old_color = [(sr,sc)], image[sr][sc]
        while fringe:
            curr_row, curr_col = fringe.pop(0)

            if 0 <= curr_row < len(image) and 0 <= curr_col < len(image[0]) and image[curr_row][curr_col] == old_color:
                image[curr_row][curr_col] = newColor
                fringe.append((curr_row - 1, curr_col))
                fringe.append((curr_row + 1, curr_col))
                fringe.append((curr_row, curr_col + 1))
                fringe.append((curr_row, curr_col - 1))

        return image


sol = Solution()
image_user = [[1,1,1],[1,1,0],[1,0,1]]
print(sol.floodFill(image_user, 1, 1, 2))

