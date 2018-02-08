poss_score = [0, 0, 0, 1, 0, 1, 4, 0, 5, 8, 3, 16, 11, 13, 33, 14, 31, 46, 26, 53, 50, 49, 65, 50, 69, 58, 52, 70, 43, 51, 47, 32, 37, 20, 22, 16, 8, 10, 3, 4, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0]

total_poss = float(sum(poss_score))
given_or_better = float(sum(poss_score[37:]))
p_val = float(given_or_better/total_poss)

print p_val
