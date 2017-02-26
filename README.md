Instructions:
This microservice accepts arguments from the command line, converts the string to Pig Latin and returns the result as a response in HTTP message body using GET. The result can be viewed on the browser by opening the port localhost:80

Install the following by typing in the terminal.

•	install homebrew:
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
•	install python3:
brew install python3
•	install virtualenv:
pip3 install virtualenv
•	install Flask:
pip3 install Flask
•	install request:
sudo pip3 install request
•	Running the microservice: (For running on port 80, you would need administrative privileges)
sudo python3 PigLatin.py Enter the paragraph here!
•	install Django: (For executing test cases)
sudo pip3 install django
•	Running the test file:
python3 Test_PigLatin.py

Note: A new test case can be easily added in the Test_PigLatin file by adding a new function
External Libraries used:
Flask: Used Flask since it provides with tools, libraries and technologies that allows us to build microservices. 
Request: This module is imported for using the HTTP Get request
