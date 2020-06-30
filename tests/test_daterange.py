import os
import time
import unittest


class DateRangeTest(unittest.TestCase):
    def setUp(self):
        self.openlicensefile = os.path.join(
                                os.path.dirname(__file__),
                                '../LICENSE')
        self.pattern = 'Copyright (C) %s, SeWeMail, Inc. <opensource@sowemail.com>' % (
                        time.strftime("%Y"))
        fh = open(self.openlicensefile)
        self.license_file = fh.read()
        fh.close()

    def test__daterange(self):
        self.assertIn(self.pattern, self.license_file)
