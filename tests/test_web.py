# -*- coding: utf-8 -*-
from . import WikiBaseTestCase

PAGE_CONTENT = u"""\
title: Test
tags: one, two, 3, jö

Hello, how are you guys?

**Is it not _magnificent_**?
"""


CONTENT_HTML = u"""\
<p>Hello, how are you guys?</p>
<p><strong>Is it not <em>magnificent</em></strong>?</p>"""


WIKILINK_PAGE_CONTENT = u"""\
title: link

[[target]]
"""

WIKILINK_CONTENT_HTML = u"""\
<p><a href='/target'>target</a></p>"""

class WebContentTestCase(WikiBaseTestCase):
    """
        Various test cases around web content.
    """

    def test_index_missing(self):
        """
            Assert the wiki will correctly play the content missing
            index page, if no index page exists.
        """
        rsp = self.app.get('/')
        assert b"You did not create any content yet." in rsp.data
        assert rsp.status_code == 200
