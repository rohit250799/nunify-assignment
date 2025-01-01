Logical breakdown of the given problem and its solution:

1. Parsing of the input:

    a) We start by reading the dimensions of the warehouse 
    b) then, reading the initial position and movement commands for each robot in the warehouse

2. Dealing with the robot directions:
    
    a) Use a list of directions (N, E, S, W) to determine rotation with each character representing a particular direction
    b) afterwards, using a dictionary to keep track of changes in movement based on the directions

3. Handling commands:

    a) Rotating left or right based on commands L and R using the direction list from the input
    b) Moving forward in the current direction if input = M and updating the robot position on the grid
    c) Also, keeping a track of the warehouse boundaries (rectangular) - so, the robots don't cross them

4. 