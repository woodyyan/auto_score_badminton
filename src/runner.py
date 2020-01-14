from src.badminton_scorer import BadmintonScorer

if __name__ == '__main__':
    badminton_scorer = BadmintonScorer()
    specs = badminton_scorer.run('/Users/songbai.yan/Downloads/Python/auto')
    print(specs[0].score)
    print(specs[1].score)
    print(specs[2].score)
    print(specs[3].score)
