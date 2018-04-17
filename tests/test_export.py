# -*- coding: utf-8 -*-

from wiki.core import Page

from . import WikiBaseTestCase

PAGE_CONTENT = u"""\
title: Test
tags: one, two

Hello, how are you guys?

Is it not magnificent?
"""

class pdf(WikiBaseTestCase):
    page_content = PAGE_CONTENT

    def setUp(self):
        super(pdf, self).setUp()
        self.page_path = self.create_file('test.md', self.page_content)
        self.page = Page(self.page_path, 'test')

    def test_page_loading(self):
        """
            Assert that content is loaded correctly from disk.
        """
        assert self.page.content == PAGE_CONTENT

    def test_pdf_exists(self):
        print 'here'
        print self.page_path
        url = self.page.url
        pdf = self.wiki.pdf(url)
        ## assert that returned is pdf format
        assert pdf[:4]=='%PDF'
