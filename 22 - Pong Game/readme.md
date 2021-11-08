#Pong Game

Today's project is to implement a version of Pong using what we know from the turtle library.
Breaking the project apart into steps, we'll need:

* Main Screen
  * Dashed line separating the two sides of the screen
  * Score tally for each paddle
* 2 Paddles
  * Independent control of each paddle (WASD and arrow keys)
* 1 Ball
  * Ball needs to move automatically
  * handle angle changes based on directional contact with paddle
  * increase speed slightly each hit until one is missed
* Score handled by ball going out of bounds on one side or the other
  * score needs to increase on opposite side where missed