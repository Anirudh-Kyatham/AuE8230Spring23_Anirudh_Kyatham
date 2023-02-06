For Circle:-
In a while loop, we keep publishing the velocity command to move the Turtle in a circle with a constant twist velocity until the node is shut down.
Finally, in the main function, we call the move() function and handle any ROS interruptions that might occur during the execution of the code.

For OpenLoop:-

This code will make the Turtle move in a square of 2x2 units with 0.2 linear velocity and 0.2 rad/s angular velocity using open loop control. The Turtle will move forward for 2 seconds and then stop for 0.5 seconds before turning to the next direction.
At each iteration of the loop, the linear velocity x and angular velocity z are set and published. The rospy.Rate and rospy.sleep functions are used to control the rate at which the velocity is published.

ClosedLoop:-

The goal of the square_closedloop.py code is to make the Turtle move in a square shape of 3x3 units by utilizing velocity control. The coordinate points of the square are pre-defined in the program, with the turtle starting at point (5,5) and moving to points (8,5), (8,8), (5,8), and finally back to (5,5). The code uses velocity control to accurately move the turtle from one point to another, resulting in a smooth and precise movement in the shape of a square.
