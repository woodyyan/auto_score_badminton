from src.badminton_examination import BadmintonExamination

if __name__ == '__main__':
    examination = BadmintonExamination()
    student_scores = examination.check('/Users/songbai.yan/Downloads/Python/auto')
    print(len(student_scores))
    for score in student_scores:
        print(score.student_id)
        print(score.part_a_score)
        print(score.part_b_score)
        print(score.part_c_score)
