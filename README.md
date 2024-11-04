# acculer_task
Simple blog application where user can create, update, read and delete the post


## Getting Started
### Challeges Encountered:
1. At the beginning while setupping the project continusely getting url not found error and then I had resolved it using with the help of flask official docs by adding main function condition at the end of the flask app file
2. While adding urling in html using jinja2 template systax got error while configuring it, just for temporary fix I ahd direcltly added hard coded url due to lack of time but it is not a permanent fix

### For project UI demo you use view images in following directory
#### demo/

### Project setup:
### Follow below steps to setup project in local
1. Download and install Python 3.12
2. Install poetry using below command
```shell
pip install poetry
```
3. Clone the project
```shell
git clone https://github.com/{{username}}/acculer_task.git
```
4. Install dependencies using below command 
```shell
poetry install
```
Install poetry with dev dependencies
```shell
poetry install --with dev
```
5. Run the project
```shell
python app.py
```