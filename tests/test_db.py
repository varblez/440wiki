from wiki.core import Db
import unittest
from pymongo import MongoClient

URL = u'testurl'
TITLE = u'test title'
TAGS = u'test tags'
BODY = u'test body'

test_client = MongoClient()
test_db = test_client.wiki
my_db = Db()


class TestDb(unittest.TestCase):
    def delete_document(self, my_url=URL):
        """
        Helper function to delete a document from the database
        :param my_url:
        :return: True or False depending if the delete was successful
        """
        result = test_db.wiki.delete_one({'url': my_url})
        if result is not None:
            return True
        return False

    def create_document(self, my_url=URL, my_title=TITLE, my_tags=TAGS, my_body=BODY):
        """
        Helper function to create a document in the database with parameters
        :param my_url:
        :param my_title:
        :param my_tags:
        :param my_body:
        :return: True or False depending if the insert was successful
        """
        result = test_db.wiki.insert_one({'url': my_url, 'title': my_title, 'tags': my_tags, 'body': my_body})
        if result is None:
            return False
        return True

    def get_document(self, my_url=URL):
        return test_db.wiki.find_one({'url': my_url})

    def exists_document(self, my_url=URL):
        """
        Helper function to check the existence of a document in the database.
        :param my_url:
        :return: True or False whether the document exists or not
        """
        result = self.get_document(my_url)
        if result is None:
            return False
        return True

    def test_insert(self):
        """
        Tests if the given content to a document is valid
        :return:
        """
        my_db.insert(URL, TITLE, TAGS, BODY)
        result = self.get_document()
        assert result is not None
        assert URL in result['url']
        assert TITLE in result['title']
        assert TAGS in result['tags']
        assert BODY in result['body']

    def test_delete(self):
        """
        Test deleting a document
        :return:
        """
        self.create_document()
        my_db.delete(URL)
        assert self.exists_document() is False

    def test_exists(self):
        """
        Test if a given url exists or doesn't
        :return:
        """
        result = my_db.exists(URL)
        assert result is False
        self.create_document()
        result = my_db.exists(URL)
        assert result is True

    def test_get_page(self):
        """
        Test if the data retrieved from the document is the same as the data used to create it
        :return:
        """
        result = my_db.get_page(URL)
        assert result is None
        self.create_document()
        result = my_db.get_page(URL)
        assert result is not None
        assert URL in result[0]
        assert URL in result[1]['url']
        assert TITLE in result[1]['title']
        assert TAGS in result[1]['tags']
        assert BODY in result[1]['body']

    def test_update_url(self):
        """
        Test the changing of a url in a document
        :return:
        """
        self.create_document()
        new_url = u'notatesturl'
        my_db.update_url(URL, new_url)
        assert self.exists_document() is False
        assert self.exists_document(new_url) is True

    def test_get_pages(self):
        """
        Test getting every document from the database
        :return:
        """
        self.create_document(u'1', u'1', u'1', u'1')
        self.create_document(u'2', u'2', u'2', u'2')
        self.create_document(u'3', u'3', u'3', u'3')
        result = my_db.get_pages()
        assert u'1' in result[0]
        assert u'2' in result[1]
        assert u'3' in result[2]

    def tearDown(self):
        """
        Delete every document in the database
        :return:
        """
        test_db.wiki.delete_many({})


def main():
    unittest.main()


if __name__ == "__main__":
    main()
