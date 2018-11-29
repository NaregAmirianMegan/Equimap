# Creators: Matt Peng, Nareg Megan
## About: 
This project was done utilizing Google's machine larning libraries and the whole project basically does this
1. Parses through news articles on google using beatiful soup 4 and converted to json data to be utilized for analysis
2. The api was then called upon the text from the articles
3. This was all then integrated into a front end UI

## Running Locally

Set up your virtual environment:

    virtualenv env

Note: If you do not already have `virtualenv` installed, run 'sudo easy_install pip' and then 'pip install virtualenv'.

Enter your virtual environment:

    source env/bin/activate

Install dependencies:

    pip install -r requirements.txt

Test your application locally:

    python main.py

Visit `localhost:8080` to view your application running locally. Press `Control-C` from command line when you are finished.

When you are ready to leave your virtual environment:

    deactivate


# CalHacksApp
This project was built at Cal Hacks 5 and gives analysis based off sentiment score of article positivity on a certain company that a user can serach up. Stock tips include whether to invest or sell stocks.

## Contact Us:
**mattpeng3@gmail.com**
**nmegan@berkeley.edu**
