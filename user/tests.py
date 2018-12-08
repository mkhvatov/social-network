from application import create_app as create_app_base
from mongoengine.connection import _get_db
import unittest

from user.models import User


class UserTest(unittest.TestCase):
    def create_app(self):
        self.db_name = 'flaskbook_test'
        return create_app_base(
            MONGODB_SETTINGS={'DB': self.db_name},
            TESTING=True,
            WTF_CSRF_ENABLED=False,
        )

    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()

    def tearDown(self):
        db = _get_db()
        db.connection.drop_database(db)

    def test_register_user(self):
        # basic registration
        rv = self.app.post('/register', data=dict(
                first_name="FName",
                last_name="LName",
                username="test_user",
                email="test@user.com",
                password="test123",
                confirm="test123"
            ), follow_redirects=True)
        assert User.objects.filter(username='test_user').count() == 1
