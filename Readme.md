How to test:

1. Clone the repo and download and install Python into the system. For this assignment, I have used Python 3.12.3
2. To install python 3 and setup virtual environment, [click here](https://medium.com/@pythonistaSage/installing-and-using-python-on-ubuntu-a-guided-tutorial-c4ab0eda33a3)
3. Once virtual environment is set up, activate it using - `source env/bin/activate` (for Ubuntu users) where env is the name of the 
virtual environment you used while setting up
4. To run the program, open the terminal from the root directory (which contains the requirements.txt, rc_robots_solution.py etc. files)
5. Inside the terminal, type the command `python3 rc_robots_solution.py` and enter
6. Output will be displayed on the terminal
7. To try out with different input data, you can change the **input_data** variable value in the rc_robots_solution.py file
8. For testing, I have used the Unittest framework of Python, imported in the **tests.py** file
9. To run the unit tests from the terminal, enter the command `python3 -m unittest tests.py` from the root directory in the terminal


**PEP 8 formatting rules followed**

Logical breakdown of the given problem and its solution:

1. Parsing of the input:

    a) We start by reading the dimensions of the warehouse 
    b) then, reading the initial position and movement commands for each robot in the warehouse

2. Dealing with the robot directions:
    
    a) Use a list of directions (N, E, S, W) to determine rotation with each character representing a particular direction
    b) afterwards, using a dictionary to keep track of changes in movement based on the directions

    Using modular arithmetic for ensuring that when the index goes below 0, it wraps around to the end of the list which in turn, 
    makes the directions behave like a circle. 

    Example: Assuming a list of directions, the indices are:

    N -> 0
    E -> 1
    S -> 2
    W -> 3

    If we're at 'N' (index 0) and turn left, we go "backward" in the list. Normally, subtracting 1 would give -1,
    which is invalid for list indices.

    Therefore, by Using (index - 1) % 4, -1 becomes 3 because % wraps it around to the last index.

    Thus, the list has been made circular - if we go right from 'N' it leads to 'E'. Similarly, going right from 'E' will 
    lead to 'S'

    **The warehouse coordinates have been displayed in a jpg file named 'warehouse_coordinates.jpg'**

3. Handling commands:

    a) Rotating left or right based on commands L and R using the direction list from the input
    b) Moving forward in the current direction if input = M and updating the robot position on the grid
    c) Also, keeping a track of the warehouse boundaries (rectangular) - so, the robots don't cross them

4. Ensure proper sequence is maintained:

    a) Each and every robot has to complete all its commands before the next one can start

5. Displaying the result:

    a) For this, the solve_rc_robots function is called inside the main function and the output is
    printed to the terminal.

