from actions.actions import Actions, Endpoints, RequestTypes, StatusCodes
from utilities.baseUtility import BaseUtility


class Test_Sample(BaseUtility):

    def test_sample_get(self):
        self.logData = self.getLogger()
        self.logData.info("*************** Test_001 *****************")
        responseModel = Actions.send_request(RequestTypes.GET, Endpoints.SAMPLE_GET, None)
        self.logData.info(responseModel)
        assert (responseModel.response_status_code == StatusCodes.STATUS_200)

    def test_sample_post(self):
        self.logData = self.getLogger()
        self.logData.info("*************** Test_002 *****************")
        requestParams = {
            "name": "morpheus",
            "job": "leader"
        }
        responseModel = Actions.send_request(RequestTypes.POST, Endpoints.SAMPLE_POST, requestParams)
        self.logData.info(responseModel)
        assert (responseModel.response_status_code == StatusCodes.STATUS_201)

    def test_sample_put(self):
        self.logData = self.getLogger()
        self.logData.info("*************** Test_003 *****************")
        requestParams = {
            "name": "morpheus",
            "job": "leader"
        }
        responseModel = Actions.send_request(RequestTypes.PUT, Endpoints.SAMPLE_PUT, requestParams)
        self.logData.info(responseModel)
        assert (responseModel.response_status_code == StatusCodes.STATUS_200)

    def test_sample_patch(self):
        self.logData = self.getLogger()
        self.logData.info("*************** Test_004 *****************")
        requestParams = {
            "name": "morpheus",
            "job": "zion resident"
        }
        responseModel = Actions.send_request(RequestTypes.PATCH, Endpoints.SAMPLE_PATCH, requestParams)
        self.logData.info(responseModel)
        assert (responseModel.response_status_code == StatusCodes.STATUS_200)

    def test_sample_delete(self):
        self.logData = self.getLogger()
        self.logData.info("*************** Test_005 *****************")
        responseModel = Actions.send_request(RequestTypes.DELETE, Endpoints.SAMPLE_DELETE, None)
        self.logData.info(responseModel)
        assert (responseModel.response_status_code == StatusCodes.STATUS_204)
