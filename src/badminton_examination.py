from src.badminton_project_parser import BadmintonProjectParser
from src.badminton_scorer import BadmintonScorer, ScoreSummary


class BadmintonExamination:

    def check(self, dir: str) -> []:
        parser = BadmintonProjectParser()
        specs = parser.build_all_project_specs(dir)
        scorer = BadmintonScorer()
        student_scores = []
        for spec in specs:
            score_summary = scorer.check(spec.badminton_service_dir)
            student_scores.append(StudentScore(spec.student_id, score_summary))
        return student_scores


class StudentScore:
    def __init__(self, student_id, score_summary: ScoreSummary):
        self.student_id = student_id
        self.score_summary = score_summary
