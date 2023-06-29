# OneAssure-assignment-backend
**Built with Flask and MongoDB**

## Endpoints
- ### /calc-premium**
  **Method:** POST
  **Description:**
  - Receives a JSON object as the body with four fields:
      - age_list - A list of ages provided by the user
      - sum_insured - A string value of the Insurance sum chosen from three options [300000, 400000, 500000]
      - city_tier - A string value of the city tier chose from the options [1,2]
      - tenure - A string value of the number of years chosen from the options [1,2]
  - Calculates the insurance premium by sorting the age list and getting the rates from the database based on the city tier, tenure, and insurance sum provided by the user

  **Parameters:**
  - age_list:
  
