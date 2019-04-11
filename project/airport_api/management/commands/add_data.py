from django.core.management.base import BaseCommand, CommandError
from airport_api.models import AirportInfo
import pandas as pd
from time import time

# Generate a list of instances.
def airports_instances_genertor(airports_tuple):
    # Begin adding data in dataframe to database using tuples fo faster proccess.
    for row in airports_tuple.itertuples():
        instance = AirportInfo(
            ident=row.ident,
            type=row.type,
            name=row.name,
            latitude_deg=row.latitude_deg,
            longitude_deg=row.longitude_deg,
            elevation_ft=' ' if row.elevation_ft == "nan" else row.elevation_ft,
            continent=row.continent,
            iso_country=row.iso_country,
            iso_region=row.iso_region,
            municipality=row.municipality,
            scheduled_service=1 if row.scheduled_service == "yes" else 0,
            gps_code=row.gps_code,
            iata_code=row.iata_code,
            local_code=row.local_code,
            wikipedia_link=row.wikipedia_link,
            keywords=row.keywords
        )

        yield instance


class Command(BaseCommand):
    help = 'Add data from csv file to the database.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='csv file contains data.')

    def handle(self, *args, **kwargs):
        start = time()
        # Use the name of the files
        file_name = kwargs['csv_file']

            # Read csv file.
        df = pd.read_csv(f'{file_name}.csv')

        # filter by data that has iata_code then replace NaN's with empty.
        df_has_iata_code = df[df.iata_code.notnull()].fillna('')
        
        # Add airports into a generator list, better for memory sufficiency.
        airports = airports_instances_genertor(df_has_iata_code)

        # Used bulk_create to send a one hit to the database that will create all the instances.
        AirportInfo.objects.bulk_create(airports)

        duration = time() - start
        self.stdout.write(self.style.SUCCESS(f'Data was added to database successfully it took {duration} seconds'))