import unittest

from src.badminton_project_parser import BadmintonProjectParser


class TestBadmintonProjectParser(unittest.TestCase):
    def test_should_return_1_when_build_all_project_specs_given_dir(self):
        badminton_parser = BadmintonProjectParser()
        badminton_dir = './test_data'
        project_specs = badminton_parser.build_all_project_specs(badminton_dir)
        self.assertEqual(len(project_specs), 1)
        self.assertEqual(project_specs[0].student_id, '001')
        self.assertEqual(project_specs[0].badminton_service_dir,
                         './test_data/badminton_project_c001')


if __name__ == '__main__':
    unittest.main()
