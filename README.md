# Robot Challenge

## Description

- The description and scope of the Challenge can be found in [CHALLENGE.md](CHALLENGE.md)
- This project includes my solution to the aforementioned challenge. Essentially it is a toy robot moving on a 5 X 5 table.
- The application assumes you have Python3 installed.


## Requirements
This solution was developed on Mac OS X 11.2.3 using Python 3.8.2. It has also been tested on Ubuntu 18.04 running Python 3.6.5.
``` 
	Python >= 3.6.5
```

You can check your version by running the following command:
```
	$ python3 --version
```
Alternatively if you have already symmlinked python3 to be python then just run
```
	$ python --version
```

To use the automated tests please install pytest by following this command
```
	$ pip3 install pytest==6.2.2
```

## Usage
There is no other installation required. The [toy_robot.py](toy_robot.py) file in the project directory is an executable. If for any reason you cannot execute it please change the permissions using the following command.

```
	$ chmod +x toy_robot.py
```


From here you should be able to run some commands according to the [CHALLENGE.md](CHALLENGE.md)

The basic way to run the application would is navigate to the project directory and run: 
```
	$ ./toy_robot.py
```

At this point it will wait for input from stdin, where the user is able to enter commands. Use the PLACE, MOVE, LEFT, RIGHT and REPORT commands to test the functionality of the robot. On invalid input the app should not crash and should notify the user in a friendly manner.

### Some Basic Examples
```
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
```
```
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST
```
```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
```

### Some examples with input test data
There are some input test examples in [example_input](example_input), we can direct them into the application by running the following commands
```
	$ ./toy_robot.py < example_input/test_invalid_comm_input.txt
```
This file purposely has an invalid command issued in the beginning. Below is what you should see.  
```
SKIPPING: Invalid Command 'ytb'. Please issue one of the following commands 'PLACE X,Y,F', 'MOVE', 'LEFT', 'RIGHT', 'REPORT'.
Output: 1,2,NORTH
Output: 1,3,NORTH
Output: 1,4,NORTH
Output: 1,4,WEST
Output: 0,4,WEST
Output: 0,4,NORTH
Output: 0,4,EAST
Output: 1,4,EAST
Output: 1,2,EAST
Output: 2,2,EAST
Output: 3,2,EAST
Output: 3,2,NORTH
Output: 3,3,NORTH
```

The other example data contains no invalid commands
```
	$ ./toy_robot.py < example_input/test_input_example.txt
```
Which should then output:
```
Output: 0,3,SOUTH
```





## Assumptions
There are many different ways this application can be solved. I chose to approach it in a more OO manner. If I was to deploy the solution in a production environment I would create a docker container and deploy an instance of the application. 

Now based on some of the points presented in [CHALLENGE.md](CHALLENGE.md), it mentions to make the code as extensible as possible. So therefore I made it such that, the Table can be any dimensions in the shape of a rectangle. 

I also ensured that commands and user input are case insensitive. 

I've implemented error handling how I saw it fit, i.e. when a PLACE command is issued outside of the table bounds the application raises an OutOfTableError internally, however user sees a friendly message. Similar error handling styles have been used for the MOVE command etc. 



## Testing
There are 22 unit tests in the [tests](tests) folder seperated into files depending on functionality being tested.

To run these tests firstly, ensure you have pytest installed by following the above instructions. 
Finally after installing pytest, navigate to the project directory and run:
```
	$ pytest --verbose
```




