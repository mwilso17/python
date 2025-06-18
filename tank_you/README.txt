TANK YOU - by Michael Wilson

This is an arcade inspired game that runs with the pygame library and was built on Python 3.9.1.

Players take control of a smaller tank on the left side of the screen and attempt 
to hit the enemy tank on the opposite side of the screen while avoiding incoming 
rounds. When the player has been hit and has no remaining tanks, they lose. Enemy tanks
get upgraded after each one is defeated.

Controls:
UP arrow key moves the player up.
DOWN arrow key moves the player down.
SPACE fires the player's tank gun.
Q key quits the game.
START button must be clicked in order for a new game to start.


Version notes:

V1.1.0: Updated enemy behavior to fire on a timed interval and to have more rounds on 
        screen. Max number of enemy rounds on screen is based on player score.
        Enemies now change direction at random after being defeated.

V1.0.0: Player speed is fixed. Player can be hit 4 total times before they lose.
        Player can have 3 on screen rounds at a time. Enemy tanks increase speed
        after being defeated. Enemy tanks fire rounds at player at fixed intervals.
