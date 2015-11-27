import os
import re
import app
import unittest

class AppTest(unittest.TestCase):

    # pre-compiled regular expressions
    rgba_str = 'rgba\(\d+,\d+,\d+,[\d.]*\)'
    circle_str = '<circle cx=\"\d+\" cy=\"\d+\" r=\"\d+\" stroke="{0}" stroke-width="\d+" fill="{1}" />'.format(rgba_str,rgba_str)
    svg_str = '<svg width="\d+%" height="\d+%">({0})*</svg>'.format(circle_str)

    color_pattern = re.compile(rgba_str)
    circle_pattern = re.compile(circle_str)
    svg_pattern = re.compile(svg_str)

    def setUp(self):
        self.app = app.app.test_client()

    def test_manipulator(self):
        from app.textManipulate import TextTransform
        text = TextTransform('brian eugene')

        assert text.backwards() == 'enegue nairb'
        assert text.palindrome() == 'brian eugenenegue nairb'
        assert text.piglatin() == 'ianbray eugeneay'

    def test_encoder(self):
        from app.VizGenerate import TextEncode
        te = TextEncode('Brian')
        assert te.encodedText == '29915'
        assert re.search(self.color_pattern,te.color_string) != None

    def test_SVG_element_generation(self):
        from app.VizGenerate import Circle
        circ = Circle('brian')
        assert re.search(self.circle_pattern,circ.circle) != None

    def test_SVG_generation(self):
        from app.VizGenerate import SVG
        svg = SVG('brian')
        assert re.search(self.svg_pattern,svg.SVG) != None

if __name__ == '__main__':
    unittest.main()
