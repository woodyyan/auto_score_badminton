from src.badminton_project_parser import BadmintonProjectParser
from src.badminton_scorer import BadmintonScorer


class BadmintonExamination:

    def check(self, root_dir: str) -> []:
        parser = BadmintonProjectParser()
        specs = parser.build_all_project_specs(root_dir)
        scorer = BadmintonScorer()
        student_scores = []
        for spec in specs:
            score = scorer.check(spec)
            student_scores.append(score)
        return student_scores
