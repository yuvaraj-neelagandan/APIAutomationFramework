import json
import requests
from requests import RequestException

from models.responseModel import ResponseModel
from utilities.baseUtility import BaseUtility
from utilities.settings import application_urls


class Actions:

    @staticmethod
    def send_request(request_type, endpoint, params):
        logger = BaseUtility().getLogger()
        responseModel = ResponseModel()
        try:
            if params is not None:
                response = request_type(endpoint, params)
            else:
                response = request_type(endpoint)
            logger.info("success")
            logger.info(response)
            responseModel.response_status_code = response.status_code
            if response.text:
                responseModel.response_data = json.loads(response.text)
            return responseModel
        except Exception as e:
            logger.info("Exception Occurred")
            logger.info(e)


class RequestTypes:
    GET = requests.get
    POST = requests.post
    PUT = requests.put
    PATCH = requests.patch
    DELETE = requests.delete

class Endpoints:
    BASE_URL = application_urls['base_url']
    SAMPLE_GET = BASE_URL + application_urls['sample_get']
    SAMPLE_POST = BASE_URL + application_urls['sample_post']
    SAMPLE_PUT = BASE_URL + application_urls['sample_put']
    SAMPLE_PATCH = BASE_URL + application_urls['sample_patch']
    SAMPLE_DELETE = BASE_URL + application_urls['sample_delete']


class StatusCodes:
    STATUS_200 = 200
    STATUS_201 = 201
    STATUS_204 = 204
    STATUS_300 = 300
    STATUS_400 = 400
    STATUS_500 = 500
