import numpy as np
import pandas as pd
import sys

def main(submission, answers):
    
    return (answers.Species == submission.Species).mean()

if __name__ == '__main__':
    submission = pd.read_csv(sys.argv[1], delimiter=',')
    answers = pd.read_csv('data/answers.csv', delimiter=',')
    print main(submission, answers)