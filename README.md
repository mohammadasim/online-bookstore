# Online Bookstore Project
A django application to sell books online with the ability to search for a product,
buy the product and leave reviews and comments. The application will process
payments through Stripe.

## Docker Settings
This application uses docker in the development env and will also be deployed as
docker container. The docker-compose file has all the containers required to develop
and subsequently deploy the application.
### Mounts
Each container has its own mount to persist data. Similarly any code changes are 
reflected in the application immediately due to the mount for the web container.
### Installing new dependencies
To install new dependencies add them to the requirements.txt
you can then either rebuild the image and the dependencies will be installed using 
the command `docker-compose down` to stop the containers first and then `docker-compose
 up -d --build`
 To install dependencies immediately without having to rebuild the container at 
 this time use the command
 `docker-compose exec web pip install psycopg2-binary==2.8.4`
 Django related commands can also be run in a similar way
 `docker-compose exec web python manage.py migrate`
 ### env.list files
 This setup relies on using env.list files for different containers. It is very
 useful as there is no requirement to setup env variables in IDE like pycharm config
 and then also in the activate file in your virtualenv. In this setup these env vars
 are set up only in one place.
 Each time a new variable is added simple run the commands `docker-compose down` to 
 stop the containers and then `docker-compose up`
 ### nginx.conf
 To ensure that our dev env is almost identical to the production env an Nginx
 container has been setup to reverse proxy to the django dev server. In the
 nginx.conf file the upstream server has been defined as `app` is important
 that in your `settings.py` you add `app` to the list of allowed hosts. Failure
 to do so will result in your application showing an error. 
