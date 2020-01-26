def latest(scores):
    """For retrieving the latest score added to the list."""
    return scores[-1]


def personal_best(scores):
    """For getting the best score in a list of scorers."""
    return max(scores, default=None)


def personal_top_three(scores):
    """Gets the three best scores from a list of scores."""
    top_three_scores = []
    for i in range(3):
        if personal_best(scores):
            top_three_scores.append(personal_best(scores))
            scores.remove(top_three_scores[i])
    return top_three_scores
