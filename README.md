# OneAssure-assignment-backend
**Built with Flask and MongoDB**

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
                  "age_list" : [age1, age2, age3],
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

    
