from django.test import TransactionTestCase
from rest_framework.test import RequestsClient
from .models import AirportInfo

# Inherited TransactionTestCase because TestCase class is causing errors when when I try to test using postgres.
class ApiTests(TransactionTestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.airport1 = AirportInfo(
            ident='test1',
            type='test1',
            name='test name1',
            latitude_deg=555445.445,
            longitude_deg=332.225,
            elevation_ft='test',
            continent='te',
            iso_country='te',
            iso_region='test',
            municipality='test',
            scheduled_service=1,
            gps_code=55444,
            iata_code='sxf',
            local_code='45DF',
            wikipedia_link='http://test.com',
            keywords=''
        )

        self.airport2 = AirportInfo(
            ident='test2',
            type='test2',
            name='test simitest name2',
            latitude_deg=555445.445,
            longitude_deg=332.225,
            elevation_ft='test',
            continent='te',
            iso_country='te',
            iso_region='test',
            municipality='test',
            scheduled_service=1,
            gps_code=55444,
            iata_code='bmf',
            local_code='45DF',
            wikipedia_link='http://test.com',
            keywords=''
        )

        self.airport3 = AirportInfo(
            ident='test3',
            type='test3',
            name='test name3 similar',
            latitude_deg=555445.445,
            longitude_deg=332.225,
            elevation_ft='test',
            continent='te',
            iso_country='te',
            iso_region='test',
            municipality='test',
            scheduled_service=1,
            gps_code=55444,
            iata_code='sde',
            local_code='45DF',
            wikipedia_link='http://test.com',
            keywords=''
        )
        self.list_data = [
            self.airport1,
            self.airport2,
            self.airport3
        ]

        AirportInfo.objects.bulk_create(self.list_data)



    def test_fetching_all_airports_success(self):
        """
        Test if fetching all data api is working
        """
        response = self.client.get('http://localhost:8000/api/airports')
        self.assertEqual(response.status_code, 200)

    def test_fetching_all_airports_fails(self):
        """
        Test what code status is sent when the link was written wrongly
        """
        response = self.client.get('http://localhost:8000/api/airport')
        self.assertEqual(response.status_code, 404)

    def test_searching_by_iata_code_success(self):
        """
        Test if search by iata code api is working
        """
        response = self.client.get('http://localhost:8000/api/airports/iata_code/sxf')
        self.assertEqual(response.status_code, 200)

    def test_searching_by_iata_code_returns_expected_result(self):
        """
        Test if search by iata code api is searching the requested results
        """
        response = self.client.get('http://localhost:8000/api/airports/iata_code/sxf')
        self.assertEqual(response.json()['iata_code'], 'sxf')

    def test_searching_by_iata_code_case_insensetive_returns_expected_result(self):
        """
        Test if search by iata code allow case insensitive searching.
        """
        response = self.client.get('http://localhost:8000/api/airports/iata_code/sXf')
        self.assertEqual(response.json()['iata_code'], 'sxf')

    def test_searching_by_iata_code_not_found(self):
        """
        Test if search by iata code api is giving the correct status code when results are not found
        """
        response = self.client.get('http://localhost:8000/api/airports/iata_code/sxfss')
        self.assertEqual(response.status_code, 404)

    def test_filter_by_name_code_success(self):
        """
        Test if filter by name api is working
        """
        response = self.client.get('http://localhost:8000/api/airports/search_name/simi')
        self.assertEqual(response.status_code, 200)
    
    def test_filter_by_name_multiple_return_expected_number_of_results(self):
        """
        Test if filter by name api is giving the expected number of results when it filters
        """
        response = self.client.get('http://localhost:8000/api/airports/search_name/simi')
        self.assertEqual(len(response.json()), 2)

    def test_filter_by_name_multiple_case_sensitive_return_expected_number_of_results(self):
        """
        Test if filter by name api allow case insensitive searching and partial matches. 
        """
        response = self.client.get('http://localhost:8000/api/airports/search_name/siMi')
        self.assertEqual(len(response.json()), 2)

    def test_filter_by_name_multiple_return_expected_number_of_results(self):
        """
        Test if filter by name api is giving the expected number of results when it filters
        """
        response = self.client.get('http://localhost:8000/api/airports/search_name/name1')
        self.assertEqual(len(response.json()), 1)

    def test_filter_by_name_code_not_found(self):
        """
        Test if filter by name api is giving the expected status code when there is no results.
        """
        response = self.client.get('http://localhost:8000/api/airports/search_name/simisis')
        self.assertEqual(response.status_code, 404)