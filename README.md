# Ex1

# EX1- How to run on your computer:
From the json file we created 2 classes: a class of Building that contains an array of elevators
and a class of Elevator that contains details about specific elevator
From the csv file of the calls.csv we created a CallForElevator class that contains details about a specific call.
The main() has a field which is a list of CallForElevators and the main() ran the  whole program.
In order to run the program: enter the desired building with the desired Call file in the following format:
.\data\Ex1_input\Ex1_Buildings\B3.json .\data\Ex1_input\Ex1_Calls\Calls_c.csv (for building 3 with calls c)

Please enter to line 28 in the main(): filename = the path of Ex1 project on your computer (the out.csv file will be there)

Run the program and then enter the following command line in the terminal:
java -jar Ex1_checker_V1.2_obf.jar 207616830,314855099  .\data\Ex1_input\Ex1_Buildings\B1.json out1.csv out.log

In order to ran the tests- enter the suitable  path on your computer


# OUR OFFLINE ALGORITHM:
Each elevator is given a number of calls to do according to its speed.
For example - an elevator with speed=8.0 will receive 8 calls 
in this Algorithm an elevator with a high speed will receive more calls compared to the other elevators.
In this way the division of labor between the degrees will be fairer.



We came to this algorithm after lot of thinking.
First we wrote a simulator code of times - we calculated the elevator's position at a given time, in order to calculate whether take or not the new call.
We actually created a kind of algorithm online from the given csv file.
But after running we got a very high average time and realized we had to think "offline"
