# LinkedIn Bot
A bot to fetch name, email, title and url of linkedin user based on their public profile and upload that data to google spreadsheet using google api. 

### Running locally

Clone this repo
```sh
$ git clone https://github.com/shubham-shrivastava/linkedin_bot.git
```
Now create the virtualenv of Python3.6 using
```sh
$ virtualenv my_env
```
OR if using conda
```sh
$ conda create --name my_env python=3
```
Activate the environment.
```sh
$ activate my_env
```
or
```sh
$ ./bin/activate
```
Now install requirements using pip, navigate to linkedin folder which have spider as a subfolder and start the bot

```sh
$ pip install -r requirements.txt
$ scrapy crawl linkedin.com
```
Your application will now be running.
