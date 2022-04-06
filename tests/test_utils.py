import json

import requests

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

    def reset_expectations():
        url = 'http://localhost:1080/reset'
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