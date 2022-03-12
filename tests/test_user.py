import unittest
from main import create_app, db
from models.User import User

class TestUser(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()


    def test_user_index(self):
        response = self.client.get("/users/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_user_create(self):
        response = self.client.post("/users/", json={
            "firstname": "firstNameTest",
            "lastname": "lastNameTest"
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("id" in data.keys()))

        user = User.query.get(data["id"])

        self.assertIsNotNone(user)

    def test_book_delete(self):
        user = User.query.first()

        response = self.client.delete(f"/users/{user.id}")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        user = User.query.get(user.id)

        self.assertIsNone(user)