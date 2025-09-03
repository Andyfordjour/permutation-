# permutation-

String Permutations

Overview

This project generates all permutations of a given string without using libraries. The solution is implemented in Python and uses a recursive approach to generate permutations.

Design

The solution uses a recursive function generate_permutations to generate all permutations of the input string. The function works by selecting each character in the string and generating permutations for the remaining characters.

Implementation

The code is implemented in Python and consists of two functions: generate_permutations and main. The generate_permutations function generates all permutations of the input string, while the main function calls generate_permutations with the user  input string "Andy" and prints the permutations.

# Run code locally 
Clone the repository:
git clone from repository 
To run the code use the "python app.py" at the terminal to run.
NOTE:  make sure you have python installed with a version of 3.9.0 and above 


# ARCHITECTURE

 User Input  ->  UI (Input box: string)/ Terminal  -> Backend (Python recursion code) -> Output: permutations 


Users would interact with a simple UI (text box) using a exapmle python flask application .

The UI sends the string to the backend API (Python app).

The backend computes permutations and returns results.

# Docker Containerization

This application can be containerized with Docker for portability. The Dockerfile provided defines the runtime environment.

Build the Docker image:

docker build -t string-permutations .

Run the container interactively so you can input a string

docker run -it --rm string-permutations



# OUT RESULTS
In the file is a screenshot of how the code runs
