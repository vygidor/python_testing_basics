# -*- coding: utf-8 -*-

import StringIO
import sys
import unittest
import ui_test_basics5
import HTMLTestRunner


# ----------------------------------------------------------------------

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)


def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')


# ------------------------------------------------------------------------
# This is the main test on HTMLTestRunner

class Test_HTMLTestRunner(unittest.TestCase):
    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(ui_test_basics5.UITest),
        ])

        # Invoke TestRunner
        buf = StringIO.StringIO()
        # runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            title='<Demo Test>',
            description='This demonstrates the report output by HTMLTestRunner.'
        )
        runner.run(self.suite)

        EXPECTED = u"""
        """
        # check out the output
        byte_output = buf.getvalue()
        # output the main test output for debugging & demo
        print byte_output
        # HTMLTestRunner pumps UTF-8 output
        output = byte_output.decode('utf-8')
        self._checkoutput(output, EXPECTED)

    def _checkoutput(self, output, EXPECTED):
        i = 0
        for lineno, p in enumerate(EXPECTED.splitlines()):
            if not p:
                continue
            j = output.find(p, i)
            if j < 0:
                self.fail(safe_str('Pattern not found lineno %s: "%s"' % (lineno + 1, p)))
            i = j + len(p)


##############################################################################
# Executing this module from the command line
##############################################################################

import unittest

if __name__ == "__main__":
    if len(sys.argv) > 1:
        argv = sys.argv
    else:
        argv = ['test_HTMLTestRunner.py', 'Test_HTMLTestRunner']
    unittest.main(argv=argv)
    # Testing HTMLTestRunner with HTMLTestRunner would work. But instead
    # we will use standard library's TextTestRunner to reduce the nesting
    # that may confuse people.
    # HTMLTestRunner.main(argv=argv)
