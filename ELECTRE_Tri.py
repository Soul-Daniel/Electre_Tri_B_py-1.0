import numpy as np
import csv


def input_criteria(name):
    """
    Generates from a .csv file the list of criteria and the dictionary of weights.

    :param name: Name of the .csv file which must contain on the first line the
        name of the criteria and on the second line the weightings.

    :return C: List of strings corresponding to the names of the criteria in the
        order they are given in the csv file.

    :return W: Dictionary where the keys are the names of the criteria and the
        values are the corresponding weightings.
    """
    C = []
    W = {}
    with open(name, 'r', newline='') as C_csv:
        reader = csv.reader(C_csv, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                [C.append(item) for item in row]
            else:
                for j in range(len(row)):
                    W[C[j]] = float(row[j])
            line_count += 1
    return C, W


def input_performances(name):
    """
    Generates from a .csv file the list of actions and the performance dictionary.

    :param name: Name of the .csv file which must contain on the first line the names
        of the actions, on the second line the names of the criteria and on the
        following lines the performance of each action against each criterion.

    :return A: List of strings corresponding to the names of the actions in the order
        in which they are given in the csv file.

    :return P: Dictionary in which the keys are the names of the actions and the values
        are sub-dictionary where the keys are the criteria and the values are the
        performances.
    """
    A = []
    C = []
    P = {}
    with open(name, 'r', newline='') as P_csv:
        reader = csv.reader(P_csv, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                [A.append(item) for item in row]
            elif line_count == 1:
                [C.append(item) for item in row]
            else:
                perf_A = {}
                for j in range(len(row)):
                    perf_A[C[j]] = float(row[j])
                P[A[line_count-2]] = perf_A
            line_count += 1
    return A, P


def input_thresholds(name_moderate, name_good):
    """
    Generates from a .csv file the dictionary of reference profiles and thresholds.

    :param name_moderate: Name of the .csv file which must contain on the first
        line the names of the criteria and on the following lines, for each criterion,
        the values of the reference profile for the moderate category, the indifference
        threshold, the preference threshold and the veto threshold.

    :param name_good: Name of the .csv file which must contain on the first line
        the names of the criteria and on the following lines, for each criterion,
        the values of the reference profile for the good category, the indifference
        threshold, the preference threshold and the veto threshold.

    :return T: Dictionary in which the keys are the names of the reference profiles
        and the values are sub-dictionary in which the keys are the criteria and the values
        are a list containing the data of bk, qi, pi and vi.
    """
    C = []
    Th_moderate = {}
    with open(name_moderate, 'r', newline='') as th_moderate_csv:
        reader = csv.reader(th_moderate_csv, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                [C.append(item) for item in row]
            else:
                th = []
                [th.append(float(item)) for item in row]
                Th_moderate[C[line_count-1]] = th
            line_count += 1

    C = []
    Th_good = {}
    with open(name_good, 'r', newline='') as th_good_csv:
        reader = csv.reader(th_good_csv, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                [C.append(item) for item in row]
            else:
                th = []
                [th.append(float(item)) for item in row]
                Th_good[C[line_count-1]] = th
            line_count += 1

    T = {'Moderate': Th_moderate, 'Good': Th_good}
    return T


def concordance(CRITERIA, ACTIONS, PERFORMANCES, THRESHOLDS, CATEGORIES):
    """
    Calculates the concordance matrix for a given reference profile.

    :param CRITERIA: List containing the names of the criteria as strings.

    :param ACTIONS: List containing the names of the actions as strings.

    :param PERFORMANCES: Performance dictionary.

    :param THRESHOLDS: Dictionary of reference profiles and thresholds.

    :param CATEGORIES: Name of the reference profiles for which you want
        to calculate the concordance matrix.

    :return Concordance: Dictionary containing the matrix of concordance of
        actions with regard to the reference profile chosen as input.
        The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Concordance = {}
    conc_2D_1 = np.empty((0, len(CRITERIA)))
    conc_2D_2 = np.empty((0, len(CRITERIA)))
    for action in ACTIONS:
        conc_1D_1 = []
        conc_1D_2 = []
        for criteria in CRITERIA:
            gbk, qbk, pbk, vbk = THRESHOLDS[CATEGORIES][criteria]
            gai = PERFORMANCES[action][criteria]
            c1 = min(1, max(0, (gai - gbk + pbk) / (pbk - qbk)))
            c2 = min(1, max(0, (gbk - gai + pbk) / (pbk - qbk)))
            conc_1D_1.append(c1)
            conc_1D_2.append(c2)
        conc_2D_1 = np.vstack((conc_2D_1, conc_1D_1))
        conc_2D_2 = np.vstack((conc_2D_2, conc_1D_2))
    Concordance['(ai,bk)'] = conc_2D_1
    Concordance['(bk,ai)'] = conc_2D_2
    return Concordance


def discordance(CRITERIA, ACTIONS, PERFORMANCES, THRESHOLDS, CATEGORIES):
    """
    Calculates the discordance matrix for a given reference profile.

    :param CRITERIA: List containing the names of the criteria as strings.

    :param ACTIONS: List containing the names of the actions as strings.

    :param PERFORMANCES: Performance dictionary.

    :param THRESHOLDS: Dictionary of reference profiles and thresholds.

    :param CATEGORIES: Name of the reference profiles for which you want
        to calculate the discordance matrix.

    :return discordance: Dictionary containing the matrix of discordance of
        actions with regard to the reference profile chosen as input.
        The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Discordance = {}
    disc_2D_1 = np.empty((0, len(CRITERIA)))
    disc_2D_2 = np.empty((0, len(CRITERIA)))
    for action in ACTIONS:
        disc_1D_1 = []
        disc_1D_2 = []
        for criteria in CRITERIA:
            gbk, qbk, pbk, vbk = THRESHOLDS[CATEGORIES][criteria]
            gai = PERFORMANCES[action][criteria]
            d1 = min(1, max(0, (gbk - gai - pbk) / (vbk - pbk)))
            d2 = min(1, max(0, (gai - gbk - pbk) / (vbk - pbk)))
            disc_1D_1.append(d1)
            disc_1D_2.append(d2)
        disc_2D_1 = np.vstack((disc_2D_1, disc_1D_1))
        disc_2D_2 = np.vstack((disc_2D_2, disc_1D_2))
    Discordance['(ai,bk)'] = disc_2D_1
    Discordance['(bk,ai)'] = disc_2D_2
    return Discordance


def global_concordance(CONCORDANCE, CRITERIA, ACTIONS, WEIGHTS):
    """
    Calculates the global concordances vectors for a given reference profile
    using a given concordance matrix.

    :param CONCORDANCE: Matrix of concordance of actions with regard to
        a given reference profile.

    :param CRITERIA: List containing the names of the criteria as strings.

    :param ACTIONS: List containing the names of the actions as strings.

    :param WEIGHTS: Dictionary containing the weightings of each criterion.

    :return Global_concordance: Dictionary containing two vectors corresponding
        to the global concordance of the actions Si with the reference profile
        defined in input bk, and of bk with the actions Si.
        The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Global_concordance = {}
    weights_sum = sum(WEIGHTS.values())
    glob_conc_1D_1 = []
    glob_conc_1D_2 = []
    for i in range(len(ACTIONS)):
        gc1 = 0.0
        gc2 = 0.0
        for j in range(len(CRITERIA)):
            gc1 = gc1 + (WEIGHTS[CRITERIA[j]] * CONCORDANCE['(ai,bk)'][i][j]) / weights_sum
            gc2 = gc2 + (WEIGHTS[CRITERIA[j]] * CONCORDANCE['(bk,ai)'][i][j]) / weights_sum
        glob_conc_1D_1.append(gc1)
        glob_conc_1D_2.append(gc2)
    Global_concordance['(ai,bk)'] = glob_conc_1D_1
    Global_concordance['(bk,ai)'] = glob_conc_1D_2
    return Global_concordance


def credibility(GLOBAL_CONCORDANCE, DISCORDANCE, CRITERIA, ACTIONS):
    """
    Calculates the credibility vectors for a given reference profile using
    the global concordance vector and the discordance matrix for the same
    reference profile.

    :param GLOBAL_CONCORDANCE: Dictionary containing the global concordances vectors
        for a given reference profile.

    :param DISCORDANCE: Matrix of discordance of actions with regard to
        the same given reference profile

    :param CRITERIA: List containing the names of the criteria as strings.

    :param ACTIONS: List containing the names of the actions as strings.

    :return Credibility: Dictionary containing two vectors corresponding to
        the credibility of the over ranking of the actions Si by the reference
        profile defined as input bk, and to the over ranking of de bk by the
        actions Si. The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Credibility = {}
    cred_1 = []
    cred_2 = []
    for i in range(len(ACTIONS)):
        cr1 = 1
        cr2 = 1
        for j in range(len(CRITERIA)):
            if DISCORDANCE['(ai,bk)'][i][j] > GLOBAL_CONCORDANCE['(ai,bk)'][i]:
                cr1 = cr1 * (1 - DISCORDANCE['(ai,bk)'][i][j]) / (1 - GLOBAL_CONCORDANCE['(ai,bk)'][i])
            else:
                cr1 = cr1 * 1
            if DISCORDANCE['(bk,ai)'][i][j] > GLOBAL_CONCORDANCE['(bk,ai)'][i]:
                cr2 = cr2 * (1 - DISCORDANCE['(bk,ai)'][i][j]) / (1 - GLOBAL_CONCORDANCE['(bk,ai)'][i])
            else:
                cr2 = cr2 * 1
        cred_1.append(cr1 * GLOBAL_CONCORDANCE['(ai,bk)'][i])
        cred_2.append(cr2 * GLOBAL_CONCORDANCE['(bk,ai)'][i])
    Credibility['(ai,bk)'] = cred_1
    Credibility['(bk,ai)'] = cred_2
    return Credibility


def over_ranking_relations(CREDIBILITY_MODERATE, CREDIBILITY_GOOD, LAMBDA):
    """
    Built the over ranking relations matrix using the credibility vectors and the
    cutting threshold. The result is a matrix containing the following four outranking
    relations:
    - preference of ai over bk: '>'
    - preference of bk over ai: '<'
    - indifference: 'I'
    - incomparability: 'R'.

    :param CREDIBILITY_MODERATE: List of credibility values for the reference profil
        "moderate".

    :param CREDIBILITY_GOOD: List of credibility values for the reference profil "good".

    :param LAMBDA: Cutting threshold value.

    :return over_ranking: Dictionary containing the over ranking relation and where
        the keys are 'Floor', 'Moderate', 'Good' and 'Roof', représenting the limits
        and boundaries of the three different categories.
    """
    over_ranking_floor = []
    over_ranking_moderate = []
    over_ranking_good = []
    over_ranking_roof = []
    over_ranking = {}

    for i in range(len(CREDIBILITY_MODERATE['(ai,bk)'])):
        over_ranking_floor.append('>')
        if CREDIBILITY_MODERATE['(ai,bk)'][i] >= LAMBDA:
            if CREDIBILITY_MODERATE['(bk,ai)'][i] >= LAMBDA:
                over_ranking_moderate.append('I')
            else:
                over_ranking_moderate.append('>')
        else:
            if CREDIBILITY_MODERATE['(bk,ai)'][i] >= LAMBDA:
                over_ranking_moderate.append('<')
            else:
                over_ranking_moderate.append('R')

    for i in range(len(CREDIBILITY_GOOD['(ai,bk)'])):
        over_ranking_roof.append('<')
        if CREDIBILITY_GOOD['(ai,bk)'][i] >= LAMBDA:
            if CREDIBILITY_GOOD['(bk,ai)'][i] >= LAMBDA:
                over_ranking_good.append('I')
            else:
                over_ranking_good.append('>')
        else:
            if CREDIBILITY_GOOD['(bk,ai)'][i] >= LAMBDA:
                over_ranking_good.append('<')
            else:
                over_ranking_good.append('R')

    over_ranking['Floor'] = over_ranking_floor
    over_ranking['Moderate'] = over_ranking_moderate
    over_ranking['Good'] = over_ranking_good
    over_ranking['Roof'] = over_ranking_roof
    return over_ranking


def pessimistic_sorting(ACTIONS, OVER_RANKING, CATEGORIES):
    """
    Ranks actions in the three different categories according to a pessimistic procedure.

    :param ACTIONS: List containing the names of the actions as strings.

    :param OVER_RANKING: Dictionary containing the over ranking relations.

    :param CATEGORIES: List containing the names of the three different categories.

    :return: ranking: Dictionary containing the rank of each actions according to a
        pessimistic procedure. The keys are the actions and the values are the median ranks.

    :return: category: Dictionary containing the three different categories and the actions
        they contain. The keys are the categories 'Bad', 'Moderate', and 'Good'. The values
        are lists containing the actions.
    """
    ranking = {}
    category = {}
    for cat in CATEGORIES:
        ranking[cat] = np.array([])
    for i in range(len(ACTIONS)):
        if OVER_RANKING['Good'][i] == '>' or OVER_RANKING['Good'][i] == 'I':
            ranking['Good'] = np.append(ranking['Good'], ACTIONS[i])
            category[ACTIONS[i]] = 3
        elif OVER_RANKING['Moderate'][i] == '>' or OVER_RANKING['Moderate'][i] == 'I':
            ranking['Moderate'] = np.append(ranking['Moderate'], ACTIONS[i])
            category[ACTIONS[i]] = 2
        elif OVER_RANKING['Floor'][i] == '>' or OVER_RANKING['Floor'][i] == 'I':
            ranking['Bad'] = np.append(ranking['Bad'], ACTIONS[i])
            category[ACTIONS[i]] = 1
    return ranking, category


def optimistic_sorting(ACTIONS, OVER_RANKING, CATEGORIES):
    """
    Ranks actions in the three different categories according to a optimistic procedure.

    :param ACTIONS: List containing the names of the actions as strings.

    :param OVER_RANKING: Dictionary containing the over ranking relations.

    :param CATEGORIES: List containing the names of the three different categories.

    :return: ranking: Dictionary containing the rank of each actions according to a
        optimistic procedure. The keys are the actions and the values are the median ranks.

    :return: category: Dictionary containing the three different categories and the actions
        they contain. The keys are the categories 'Bad', 'Moderate', and 'Good'. The values
        are lists containing the actions.
    """
    ranking = {}
    category = {}
    for cat in CATEGORIES:
        ranking[cat] = np.array([])
    for i in range(len(ACTIONS)):
        if OVER_RANKING['Moderate'][i] == '<' or OVER_RANKING['Moderate'][i] == 'R':
            ranking['Bad'] = np.append(ranking['Bad'], ACTIONS[i])
            category[ACTIONS[i]] = 1
        elif OVER_RANKING['Good'][i] == '<' or OVER_RANKING['Good'][i] == 'R':
            ranking['Moderate'] = np.append(ranking['Moderate'], ACTIONS[i])
            category[ACTIONS[i]] = 2
        elif OVER_RANKING['Roof'][i] == '<' or OVER_RANKING['Roof'][i] == 'R':
            ranking['Good'] = np.append(ranking['Good'], ACTIONS[i])
            category[ACTIONS[i]] = 3
    return ranking, category


def median_rank(ACTIONS, PESSIMISTIC_SORTING, OPTIMISTIC_SORTING):
    """
    Calculates the median rank of each action.

    :param ACTIONS: List containing the names of the actions as strings.

    :param PESSIMISTIC_SORTING: Dictionary containing the actions classified according to
        the pessimistic procedure

    :param OPTIMISTIC_SORTING: Dictionary containing the actions classified according to
        the optimistic procedure.

    :return med_rank: Dictionary containing the median rank of each action. The keys are the
        names of the actions and the values are the median ranks.
    """
    med_rank = {}
    for action in ACTIONS:
        med_rank[action] = (OPTIMISTIC_SORTING[1][action] + PESSIMISTIC_SORTING[1][action]) / 2
    return med_rank


def display_results(ACTIONS, PESSIMISTIC_SORTING, OPTIMISTIC_SORTING, MEDIAN_RANK):
    """
    Display of the median ranks and of the categories in which each action is classified.

    :param ACTIONS: List containing the names of the actions as strings.

    :param PESSIMISTIC_SORTING: Dictionary containing the actions classified according to
        the pessimistic procedure.

    :param OPTIMISTIC_SORTING: Dictionary containing the actions classified according to
        the optimistic procedure.

    :param MEDIAN_RANK: Dictionary containing the median rank of each action.
    """
    for action in ACTIONS:
        MEDIAN_RANK[action] = (OPTIMISTIC_SORTING[1][action] + PESSIMISTIC_SORTING[1][action]) / 2
        print(action + ' is classified in the category C' + str(OPTIMISTIC_SORTING[1][action]) +
              str(PESSIMISTIC_SORTING[1][action]) + ' with a median rank of ' + str(MEDIAN_RANK[action]))
