from src.badminton_examination import BadmintonExamination


def generate_csv(student_scores):
    lines = map(
        lambda score: ','.join(
            [score.student_id, str(score.part_a_score), str(score.part_b_score), str(score.part_c_score)]) + '\n',
        student_scores)
    with open('score.csv', 'w') as file:
        file.writelines(lines)


if __name__ == '__main__':
    examination = BadmintonExamination()
    student_scores = examination.check('./Python/end')
    generate_csv(student_scores)
