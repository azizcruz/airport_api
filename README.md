# airport_api

## Installation

1. Create a folder under any name you want.
2. Navigate to the created folder.
3. Open terminal in the current working directory.
4. Clone the repository using the following command ```git clone https://github.com/azizcruz/airport_api.git .```
5. Run the docker compose command like the following ```docker-compose up``` it will take some time until it finishes downloading and setting up the environment which has python3 and postgres installed with an Ubuntu kernel.
6. When everything is finished press ```CTRL+C``` or On Mac ```Command+C``` to stop the running environments, then run ```docker-compose run web python project/manage.py migrate``` this will create the needed databases.
7. Add data to the database using the following command ```docker-compose run web python project/manage.py add_data airports```

## Hint:
Use step 7 only once otherwise you will end up with bugs or duplicated data.

## Hint:
You can navigate using ``` cd /home/edu/Desktop/test_project/project/airport_api/management/commands
``` and then run ```bash cat add_data.py``` to see the code behind how the data is added to the database.

8. Run ```docker-compose up``` then open your browser and paste the following link in the search bar http://localhost:8000/api/airports/ this will return a list of 100 results of airports informations from database, which means everything is okay to start using the rest api.

# Rest API usage

There are currently 3 endpoints:
* `/api/airports/` which returns a list of 100 results
* `/api/airports/iata_code/iata_code/` which searches in the database and returns an airport that has the same searched iata_code, note that it is case insensitive, otherwise a message with no data found.
* `/api/airports/search_name/name/` which filter results and return airports that contains the partial search_name value , note that it is case insensitive, otherwise it returns a message of data not found.

# Examples

* `/api/airports/iata_code/ghc/` will return 
```json
{"id":5170,"ident":"MYBG","type":"medium_airport","name":"Great Harbour Cay Airport","latitude_deg":25.7383,"longitude_deg":-77.840103,"elevation_ft":"18.0","continent":"","iso_country":"BS","iso_region":"BS-NB","municipality":"Bullocks Harbour","scheduled_service":false,"gps_code":"MYBG","iata_code":"GHC","local_code":"","home_link":null,"wikipedia_link":"http://en.wikipedia.org/wiki/Great_Harbour_Cay_Airport","keywords":""}
```
