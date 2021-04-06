from app import app, api
from flask_restful import Resource, reqparse
from db import db
from model import Loan


class LoanIdResource(Resource):
    def get(self):
        loan_list = Loan.query.limit(20).all()
        return [loan.id for loan in loan_list]

class LoanResource(Resource):
    def post(self, id):
        loan_data = Loan.query.get(id)
        if loan_data != None:
            return loan_data.json(), 200
        else:
            return "", 404

api.add_resource(LoanIdResource, "/loan/id")
api.add_resource(LoanResource, "/loan/<int:id>")


if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:password@localhost/loan"
    db.init_app(app)
    app.run(debug=True)