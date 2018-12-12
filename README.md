# Flask Crawler App
This project is a flask implementation of a crawler application which allows registered users to crawl a given domain and display an analysis report of the crawled links.

1. [Installation](#1)
2. [Deploy to Heroku](#2)
3. [Screenshots](#3)

## <div id="1">Installation</div>
Open a terminal and execute the following commands:
```
git clone https://github.com/Akhelesh/Flask_Crawler_App.git
cd Flask_Crawler_App
pip3 install -r requirements.txt
```

You will need to install Redis on your machine for the app to run. Type `sudo apt-get install redis-server` to install it. Now
we will need to set the following envionment variables:

```
export SECRET_KEY=25f9e794323b453885f5181f1b624d0b
export APP_CONFIG=config.ProductionConfig
export DATABASE_URL=sqlite:///site.db
export REDIS_URL=redis://
```

Finally type `bash ./scripts/heroku.sh` to run the application. Now visit the URL ouput in the terminal. It starts with 
127.0.0.1; be sure to add the port number. You will need to register an account before you can submit a domain to crawl.

## <div id="2">Deploy to Heroku</div>
This app can be easily deployed to Heroku but you must meet these prerequisites first:
   * Register an account with Heroku
   * Install the Heroku CLI ([visit here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install))
  
Follow these steps after you meet the above requirements:
1. Open up a new terminal and `cd` into the **Flask_Crawler_App** directory.
2. Now we need to login to Heroku. Type the following in the terminal:
    * ```heroku login```
    * Enter your login credentials and login
3. Once you are logged in we need to create a space for the application on the Heroku server. Execute this command for the same
	* ```heroku create <Project_Name>```. The project name parameter is optional and a random name will be assigned if missing.
4. Once the app is created, now it's time to set the following environment variables:
     
    ```
    heroku config:set SECRET_KEY=25f9e794323b453885f5181f1b624d0b
    heroku config:set APP_CONFIG=config.ProductionConfig
    heroku config:set DATABASE_URL=sqlite:///site.db
    ```
5. This Flask application needs Redis. Run the following to create a redis instance for our app.
    * ```heroku addons:create heroku-redis:hobby-dev```
6. Run `heroku config` to check the environment variables. `REDIS_URL` should be set by now.
If its missing, some problem has occured in the previous step.
7. Now add python build pack to the app
    * ```heroku buildpacks:set heroku/python```
* Then we deploy the code to heroku.
	* ```git push heroku master``` or
    * ```git push heroku yourbranch:master``` if you are in a different branch than master

## <div id="3">Screenshots</div>
### <div align="center">Home Page</div>
![homepage](https://github.com/Akhelesh/Flask_Crawler_App/blob/master/images/homepage.png)

### <div align="center">Results Page</div>
![results_page1](https://github.com/Akhelesh/Flask_Crawler_App/blob/master/images/results_page1.png)

![results_page2](https://github.com/Akhelesh/Flask_Crawler_App/blob/master/images/results_page2.png)
