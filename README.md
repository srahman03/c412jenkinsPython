# FlaskApp with MySQL and Deploying with Jenkins

## Setup Of Systems
### Database Setup 
- First create a database, create table for movie details
- Create user for datbase and grant root priviliges for database on user
  
### Virtual Machine Setup
- install dependencies
  - `yum install python3 python3-pip3`
  - `pip install cryptography`
  - `pip install flask`
  - `pip install pymysql`

### Jenkins Setup
- Give root privileges to Jenkins user on visudo
- Create pipeline item project

## My steps
### Git cloned repo
### Created Flask App on windows
### Checked Deployment on localhost on windows
### Created Jenkins Pipeline project to build, deploy on Virtual Machine server (centOS10)
### Checked Deployment on VM (Virtual Machine) IP Address
### SUCCESS
