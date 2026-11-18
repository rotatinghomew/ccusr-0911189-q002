import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from archive_search.workflow import report


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / 'data' / 'sample.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def test_entry(self):
        result = subprocess.run([sys.executable, '-m', 'archive_search', 'review', str(self.path)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), report(self.data))

    def test_scope_and_cutoff(self):
        output = report(self.data)
        self.assertEqual(output['coverage']['candidate']['Q1'], {'judged':0,'total':2})
        self.assertEqual(output['coverage']['current']['Q1']['judged'], 1)
        self.assertEqual(output['pending'], ['R1'])

    def test_repeated_piece_invalidates_ranking(self):
        self.data['runs']['current']['Q2'].append('s6')
        with self.assertRaises(ValueError):
            report(self.data)
