# hydro-service
Python AWS Services and Sensor Data Collection

## Serverless Framework  
#### More Info - https://serverless.com/
The configuration is defined in serverless.yml, and deployed to AWS through a command line tool. 
The Python functions are defined in the files in the 'handlers' folder.

## Sensor Data
hydrolog.py is a script run on the Raspberry Pi to collect and send the data to AWS - using the 'create' endpoint generated with serverless.
A DynamoDB instance is currently housing the data. 
