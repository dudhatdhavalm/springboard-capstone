import unittest
import os
import json
from app import create_app


class EndPointTestcase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client

    def test_get_loan_ids(self):
        res = self.client().get("/loan/id")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(len(data), 20)

    def test_loan_data_response(self):
        res = self.client().get("/loan/id")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(len(data), 20)
        id = data[0]
        res = self.client().post("/loan/{}".format(id))
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["id"], id)


if __name__ == "__main__":
    unittest.main()