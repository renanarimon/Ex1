# Ex1

# main classes
From the json files we created 2 classes:
  * Building: array of elevators
  * Elevator: details about specific elevator


From the csv file of the calls.csv:
  * CallForElevator: details about a specific call.
  * main: has a field which is a list of CallForElevators and the main() ran the  whole program.


in addition:
  * Algo_offline: the Algorithm class, allocate() function.
  
# How to run on your computer:
In order to run the program: enter the desired building with the desired Call file in the following format:
.\data\Ex1_input\Ex1_Buildings\B3.json .\data\Ex1_input\Ex1_Calls\Calls_c.csv (for building 3 with calls c)

Please enter into line 28 in the main(): filename = <the path of Ex1 project on your computer> (the out.csv file will be there)

Run the program and then enter the following command line in the terminal:
java -jar Ex1_checker_V1.2_obf.jar 207616830,314855099  .\data\Ex1_input\Ex1_Buildings\B3.json out1.csv out.log

In order to ran the tests- enter the suitable  path on your computer


# OUR OFFLINE ALGORITHM:
The logic of the algorithm - 
Each elevator has a different speed, so in order to distribute the calls in a balanced way, 
it is divided so that relatively each elevator will receive a quantity of calls according to its speed.
To maintain balance, we will divide the elevators as explained above,
for each group of calls - calculated by the sum of the speeds of all the elevators.
For example - building with 2 elevators
  * id: 0, speed: 3
  * id: 1, speed: 2


every 5 calls is divided: 3 calls to elevator 0, and 2 calls to elevator 1.

We came to this algorithm after lot of thinking.
First we wrote a simulator code of times - we calculated the elevator's position at a given time, in order to calculate whether take or not the new call.
We actually created a kind of algorithm online from the given csv file.
But after running we got a very high average time and realized we had to think "offline",
therefore we decided to write a simple algorithm that works effectively for the given cmd.
