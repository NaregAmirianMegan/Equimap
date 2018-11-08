<<<<<<< HEAD
# Python Google Cloud Natural Language sample for Google App Engine Flexible Environment

This sample demonstrates how to use the [Google Cloud Natural Language API](https://cloud.google.com/natural-language/) on [Google App Engine Flexible Environment](https://cloud.google.com/appengine). This app allows users to input text, which is sent to the Google Cloud Natural Language API. The frontend of the application displays information retrieved from the Natural Language API including sentiment analysis, entity detection, and entity sentiment.

## Setup

Create a project with the [Google Cloud Platform Console Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager). Make note of your project ID, which may be different than your project name. Make sure to [Enable Billing](https://console.cloud.google.com/billing?debugUI=DEVELOPERS) for your project.

Enable the Natural Language API. Go to the [Google Cloud Platform console](https://console.cloud.google.com), click the button in the top left, select 'APIs & services', click 'Enable APIs and Services' at the top, search for 'Natural Language', click the first result, then click the 'Enable' button.

Download the [Google Cloud SDK command line tool](https://cloud.google.com/sdk/downloads#interactive), also known as `gcloud`.

Initialize gcloud, selecting your Google account and project ID:

    gcloud init

## Getting the sample code

Run the following command to clone the Github repository:

    git clone https://github.com/ryanmats/gcp-hackathon-demos.git

Change directory to the sample code location:

    cd gcp-hackathon-demos/language

## Authentication

Set up application default credentials:

    gcloud auth application-default login

Set up a service account. Visit the [Google Cloud Platform console](https://console.cloud.google.com), search 'Service Accounts' on the top search bar, click on 'Service accounts', and click the 'Create a Service Account button' towards the top. Give your service account a name and set the 'Role' to Project > Owner. Check the 'Furnish a new private key' box and click 'Create'. Save the generated service account key json file to somewhere on your computer.

Set the `GOOGLE_APPLICATION_CREDENTIALS` variable to point to the service account key location:

    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service/account/key.json

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

## Deploying to App Engine

Deploy your application to App Engine (takes several minutes). When prompted to choose a region, choose the one that is closest to you geographically.

    gcloud app deploy

## Further Reference

[Documentation for Google Cloud Client Libraries for Python](https://googlecloudplatform.github.io/google-cloud-python/latest/index.html)
=======
# CalHacksApp
Hack at Cal Hacks

{% if sentiment.score < 20 and sentiment.score >= -20 %}
            <p>The current opinion on this company appears pretty neutral. We reccomend you keep the stocks.</p>
          {% endif %}

          {% if sentiment.score < 40 and sentiment.score >= 20  %}
            <p>The company seems to be on a positive trend. We reccomend you to consider investing more into this company.</p>
          {% endif %}

          {% if sentiment.score < 75  and sentiment.score >= 40%}
            <p>The company seems to have a great outlook based on current public opinion. You may want to start considering selling your stocks for this company.</p>
          {% endif %}

          {% if sentiment.score > 75 %}
            <p>This company appears to be at a all time high and the bubble may soon burst. This is a great time to sell your stocks as demand for this company is high based on public opinion.</p>
          {% endif %}

          {% if sentiment.score < -20 and sentiment.score >= -40 %}
            <p>This company appears to be on the down side. Consider either selling or holding out on this minor low.</p>
          {% endif %}

          {% if sentiment.score < -40 and sentiment.score >= -75 %}
            <p>Things are really not looking too great. We reccomend you to sell your stocks as the public really is starting to lose trust in this company.</p>
          {% endif %}

          {% if sentiment.score < -75 %}
            <p>Public opinion for this company is nearing the bottom. It definitely is time to sell all your stocks before the stock prices drop even lower!</p>
          {% endif %}
>>>>>>> e19ea7fbe1b332877d2a0704d7e897d57bc4e0d5
