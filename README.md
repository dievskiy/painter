This is 1-day project to practice aws skills. The idea of the app is to allow users to draw and publish pictures online (using amazon s3 service)
so that they can share it using only link. ~~[demo](http://webdrawer.tech)~~

# how to build
To run this app, configure env variables (bucket name and aws credentials if needed) in .env file and simply use:
```
docker-compose up
```
After that, navigate to http://0.0.0.0:8000 in your browser.
# tech stack
Built using micro web framework Flask on backend side and Bootstrap CSS-framework & jQuery on the frontend.

The app is deployed to ec2 instances as a docker container. EC2 instance is in subnet in VPC, which is connected to Load Balancer facing internet connections.
