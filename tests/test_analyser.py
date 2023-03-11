import unittest
from plink import options, analyser

def create_default_analyser():
    o = options.Options()
    a = analyser.Analyser(options)
    return a

class TestAnalyser(unittest.TestCase):
    def test_retrieve_links_from_html(self):
        a = create_default_analyser()

if __name__ == '__main__':
    unittest.main()