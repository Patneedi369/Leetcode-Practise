class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the point in the rectangle closest to the circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate distance components
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        
        # Check if the closest point lies within or on the boundary of the circle
        return (dx * dx + dy * dy) <= radius * radius