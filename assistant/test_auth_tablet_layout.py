import re
import unittest
from pathlib import Path


class AuthTabletLayoutTests(unittest.TestCase):
    def test_registration_button_spans_form_columns_on_tablet(self):
        css = (Path(__file__).parent / 'static' / 'fresh.css').read_text()
        tablet = css.split('@media (min-width:600px) and (max-width:850px)', 1)[1]
        self.assertRegex(tablet, re.compile(
            r'\.auth-page\s+\.auth-register\s+\.auth-form\s+form\s*>\s*button\s*'
            r'\{[^}]*grid-column\s*:\s*1\s*/\s*-1\s*;', re.S))
