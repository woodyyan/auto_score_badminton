from src.badminton_project_parser import BadmintonProjectParser
from src.badminton_scorer import BadmintonScorer


class BadmintonExamination:

    def check(self, dir: str) -> []:
        parser = BadmintonProjectParser()
        specs = parser.build_all_project_specs(dir)
        scorer = BadmintonScorer()
        all_score_info = []
        for spec in specs:
            score = scorer.check(spec.badminton_service_dir)
            all_score_info.append(ScoreInfo(spec.student_id, score))
        return all_score_info


class ScoreInfo:
    def __init__(self, student_id, score):
        self.student_id = student_id
        self.score = score
