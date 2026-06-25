import unittest
import json
from scripts.validate_wiql import validate_wiql
from scripts.generate_migration_config import generate_config

class TestBravoScripts(unittest.TestCase):
    def test_validate_wiql_missing_project(self):
        query = "SELECT [System.Id] FROM WorkItems WHERE [System.Id] = 1"
        findings = validate_wiql(query)
        self.assertTrue(any(f['severity'] == 'High' and 'System.TeamProject' in f['message'] for f in findings))

    def test_validate_wiql_valid(self):
        query = "SELECT [System.Id] FROM WorkItems WHERE [System.TeamProject] = @project AND [System.WorkItemType] = 'Task' ORDER BY [System.ChangedDate] DESC"
        findings = validate_wiql(query)
        self.assertEqual(len(findings), 0)

    def test_generate_config(self):
        config = generate_config("src", "proj-s", "tgt", "proj-t", ["Task", "Bug"])
        self.assertEqual(config['Source']['Collection'], "https://dev.azure.com/src/")
        self.assertEqual(config['Target']['Project'], "proj-t")
        self.assertIn("'Task'", config['Processors'][0]['WIQLQueryBit'])
        self.assertIn("'Bug'", config['Processors'][0]['WIQLQueryBit'])

if __name__ == '__main__':
    unittest.main()
