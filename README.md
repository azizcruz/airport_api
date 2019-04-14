# airport_api

## Installation

1. Create a folder under any name you want.
2. Navigate to the created folder.
3. Open terminal in the current working directory.
4. Clone the repository using the following comand ```shell git clone https://github.com/azizcruz/airport_api.git . ```
5. Run the docker compose command like the following ```bash docker-compose up``` it will take some time until it finishes downloading and setting up the environment which has python3 and postgres installed with an Ubuntu kernel.
6. When everything is finished press CTRL+C or On Mac Command+C to stop the running environments, then run ```bash docker-compose run web python project/manage.py migrate``` this will create the needed databases.
7. Add data to the database using the following command ```bash docker-compose run web python project/manage.py add_data airports```

## Hint:
Use step 7 only once otherwise you will end up with bugs or duplicated data.

## Hint:
You can navigate using ```bash cd /home/edu/Desktop/test_project/project/airport_api/management/commands
``` and then run ```bash cat add_data.py``` to see the code behind how the data is added to the database.

8. Run ```bash docker-compose up``` then open your browser and paste the following link in the search bar ```bash http://localhost:8000/api/airports/ ``` this will list 100 results of data from database, which means everything is okay to start using the rest api.
