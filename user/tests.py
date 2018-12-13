import unittest

from mongoengine.connection import _get_db
from flask import session

from application import create_app as create_app_base
from user.models import User


class UserTest(unittest.TestCase):
    def create_app(self):
        self.db_name = 'flaskbook_test'
        return create_app_base(
            MONGODB_SETTINGS={'DB': self.db_name},
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SECRET_KEY='mySecret',
        )

    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()

    def tearDown(self):
        db = _get_db()
        db.connection.drop_database(db)

    def user_dict(self):
        return dict(
                first_name="FName",
                last_name="LName",
                username="test_user",
                email="test@user.com",
                password="test123",
                confirm="test123"
            )

    def test_register_user(self):
        # basic registration
        rv = self.app.post('/register', data=self.user_dict(), follow_redirects=True)
        assert User.objects.filter(username='test_user').count() == 1

    def test_login_user(self):
        # create user
        self.app.post('/register', data=self.user_dict())
        # login user
        rv = self.app.post('/login', data=dict(
            username=self.user_dict()['username'],
            password=self.user_dict()['password']
        ))
        # check the session is set
        with self.app as context:
            rv = context.get('/')
            assert session.get('username') == self.user_dict()['username']
