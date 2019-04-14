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
{
    "id": 5170,
    "ident": "MYBG",
    "type": "medium_airport",
    "name": "Great Harbour Cay Airport",
    "latitude_deg": 25.7383,
    "longitude_deg": -77.840103,
    "elevation_ft": "18.0",
    "continent": "",
    "iso_country": "BS",
    "iso_region": "BS-NB",
    "municipality": "Bullocks Harbour",
    "scheduled_service": false,
    "gps_code": "MYBG",
    "iata_code": "GHC",
    "local_code": "",
    "home_link": null,
    "wikipedia_link": "http://en.wikipedia.org/wiki/Great_Harbour_Cay_Airport",
    "keywords": ""
}
```

* `/api/airports/search_name/china/` will return
```json
[{
    "id": 1027,
    "ident": "CZO",
    "type": "small_airport",
    "name": "Chistochina Airport",
    "latitude_deg": 62.5634994507,
    "longitude_deg": -144.669006348,
    "elevation_ft": "1850.0",
    "continent": "",
    "iso_country": "US",
    "iso_region": "US-AK",
    "municipality": "Chistochina",
    "scheduled_service": false,
    "gps_code": "CZO",
    "iata_code": "CZO",
    "local_code": "CZO",
    "home_link": null,
    "wikipedia_link": "",
    "keywords": ""
}, {
    "id": 5676,
    "ident": "OPPC",
    "type": "small_airport",
    "name": "Parachinar Airport",
    "latitude_deg": 33.9020996094,
    "longitude_deg": 70.0716018677,
    "elevation_ft": "5800.0",
    "continent": "AS",
    "iso_country": "PK",
    "iso_region": "PK-TA",
    "municipality": "Parachinar",
    "scheduled_service": true,
    "gps_code": "OPPC",
    "iata_code": "PAJ",
    "local_code": "",
    "home_link": null,
    "wikipedia_link": "http://en.wikipedia.org/wiki/Parachinar_Airport",
    "keywords": ""
}, {
    "id": 7042,
    "ident": "SQT",
    "type": "small_airport",
    "name": "China Strait Airstrip",
    "latitude_deg": -10.5627777778,
    "longitude_deg": 150.690694444,
    "elevation_ft": "10.0",
    "continent": "OC",
    "iso_country": "PG",
    "iso_region": "PG-MBA",
    "municipality": "Samarai Island",
    "scheduled_service": false,
    "gps_code": "AYCS",
    "iata_code": "SQT",
    "local_code": "CHS",
    "home_link": null,
    "wikipedia_link": "",
    "keywords": ""
}, {
    "id": 7744,
    "ident": "VCCT",
    "type": "medium_airport",
    "name": "China Bay Airport",
    "latitude_deg": 8.5385103225708,
    "longitude_deg": 81.1819000244141,
    "elevation_ft": "6.0",
    "continent": "AS",
    "iso_country": "LK",
    "iso_region": "LK-5",
    "municipality": "Trincomalee",
    "scheduled_service": true,
    "gps_code": "VCCT",
    "iata_code": "TRR",
    "local_code": "",
    "home_link": null,
    "wikipedia_link": "http://en.wikipedia.org/wiki/China_Bay_Airport",
    "keywords": "SLAF China Bay, RAF China Bay, Trincomalee Airport"
}]
```
