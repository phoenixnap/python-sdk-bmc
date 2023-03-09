import json

import requests

executed_reset = False

class TestUtils:
    
    def setup_expectation(requestToMock, responseToGet, times):
        
        url = 'http://localhost:1080/expectation'

        body = {
            'httpRequest': requestToMock,
            'httpResponse': responseToGet,
            'times': {
                'remainingTimes': 1,
                'unlimited': False
            }
        }

        response = requests.put(url=url, data=json.dumps(body))

        return response.json()[0]['id']

    def verify_expectation_matched_times(expectation_id, times):
        url = 'http://localhost:1080/verify'

        body = {
            'expectationId': {
                'id': expectation_id
            },
            'times': {
                'atLeast': times,
                'atMost': times
            }
        }


        response = requests.put(url=url, data=json.dumps(body))

        return response

    def reset_mockserver():
        global executed_reset
        if not executed_reset:
            url = 'http://localhost:1080/reset'
            executed_reset = True
        requests.put(url=url)

    def reset_expectations():
        url = 'http://localhost:1080/clear'
        requests.put(url=url)

    def generate_payloads_from(filename, payloadsPath = "./payloads"):
        with open(f'{payloadsPath}/{filename}.json') as file:
          payload = json.load(file)
        return payload['request'], payload['response']

    def generate_query_params(request):
        opts = {}
        qplist = request['queryStringParameters']
        for qp in qplist:
            opts[qp['name']] = qp['values'][0]
        return opts

    def extract_id_from(request, symbol = 'id'):
        return request['pathParameters'][symbol][0]

    def extract_request_body(request):
        return request['body']['json']
    
    def convert_camel_to_snake_case(request):
        request_snake_case = {}
        for key, value in request['body']['json'].items():
            snake_case_key = ""
            for i, c in enumerate(key):
                if c.isupper() and i != 0:
                    snake_case_key += "_" + c.lower()
                else:
                    snake_case_key += c.lower()

            request_snake_case[snake_case_key] = value

        return request_snake_case