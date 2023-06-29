# OneAssure-assignment-backend
**Built with Flask and MongoDB**

### Hosted on AWS and DNS config using Cloudflare
- Server running on an EC2 instance
- Proxied requests using Nginx
- Couldflare DNS is used to redirect the requests from https://srinivasmekala.me to the EC2 instance
## Endpoints
a. /calc-premium**

    Method: POST
    
    Description:
    - Receives a JSON object as the body with four fields:
    - Calculates the insurance premium by sorting the age list and getting the rates from the database based on the city tier, tenure, and insurance sum provided by the user
   
    Parameters:
    - age_list - A list of ages provided by the user
    - sum_insured - A string value of the Insurance sum chosen from three options [300000, 400000, 500000]
    - city_tier - A string value of the city tier chose from the options [1,2]
    - tenure - A string value of the number of years chosen from the options [1,2]
    
    Request Headers:
      {
         'Content-Type' : 'application/json'
      }
      
    Request body:
      Format: JSON
      Example:
              {
                  "age_list" : [age1, age2, age3....],
                  "sum_insured" : '300000' or '400000' or '500000',
                  "city_tier" : '1' or '2',
                  "tenure" : '1' or '2'
              }
              
     Response:
      Format: JSON
      Example:
              {
                  status: "success",
                  "expectedPremium": <An integer value of the expected premium>
             }

## Installation Guide
### With Docker
- Clone the Repository:
  ```$ git clone https://github.com/sri-nivas1227/OneAssure-assignment-backend```
- Change into the directory
  ```$ cd OneAssure-assignment-backend```
- Run Docker Compose (Keep the docker daemon running in your PC)
  ```$ docker-compose up --build -d```
- Now you can access the server on [localhost:5000](http://localhost:5000/)
- Send a POST request to the server with the following body
      ```{{
                  "age_list" : [10, 35, 46],
                  "sum_insured" :  '500000',
                  "city_tier" : '1' ,
                  "tenure" : '1'
              }}```
### In local environment
Note: You need Python3 installed. And MongoDB installed and running.
Opena a terminal and 👇🏻
- Clone the Repository:
  ```$ git clone https://github.com/sri-nivas1227/OneAssure-assignment-backend```
- Change into the directory
  ```$ cd OneAssure-assignment-backend```
- Create virtual environment and activate the environment
  ```$ python -m venv venv```
  Windows ```$ './venv/scripts/activate'```
  Linux: ```$ source venv/bin/activate```
- Install required packages
  ```$ pip install -r requirements.txt```
- Change the `MONGO_DB_URI` in the `.env ` file to `mongodb://localhost:27017`
- Run the server
  ```$ flask run```
  You can access the server on [localhost:5000](http://localhost:5000/)

  
  
    
