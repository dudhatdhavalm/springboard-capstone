from db import db


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actual = db.Column(db.Boolean)
    predict = db.Column(db.Boolean)
    default = db.Column(db.Float)
    none_default = db.Column(db.Float)

    def json(self):
        return {
            "id": self.id,
            "actual": self.actual,
            "predict": self.predict,
            "default": self.default,
            "none_default": self.none_default
        }
