from flask_restful import Resource
from model import Loan
import logging


class LoanIdResource(Resource):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger()

    def get(self):
        self.logger.info("LoanIdResource get request")
        loan_list = Loan.query.limit(20).all()
        self.logger.info("LoanIdResource get return with {}".format(
            len(loan_list)))
        return [loan.id for loan in loan_list]


class LoanResource(Resource):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger()

    def post(self, id):
        self.logger.info("LoanResource Post request with {}".format(id))
        loan_data = Loan.query.get(id)
        self.logger.info("LoanResource Post request return with {}".format(
            loan_data.json()))
        if loan_data != None:
            return loan_data.json(), 200
        else:
            return "", 404


def configure_routes(api):
    api.add_resource(LoanIdResource, "/loan/id")
    api.add_resource(LoanResource, "/loan/<int:id>")
