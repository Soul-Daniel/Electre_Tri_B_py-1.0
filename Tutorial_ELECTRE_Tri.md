# Tutorial "ELECTRE_Tri.py"

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), France, 27/07/2021

## 1. ELECTRE Tri method

The [**ELECTRE_Tri.py**](ELECTRE_Tri.py) code is based on the ELECTRE-Tri ranking method and follows exactly the same procedure. This method is part of the sorting problem or assignment procedure. One of the particularities of this method is that reference actions are used to segment the criteria space into categories. Thus each category is bounded below and above by two reference actions. Another particularity of the code presented below is that it allows to take into account only three categories defined by two reference actions. A modification of the code would be necessary to take into account more categories. Finally, the **ELECTRE_Tri.py** code has been designed according to an object-oriented architecture, however there is no need to define classes and instances and only methods (or functions) are used.

## 2. Import of data

The first step of the **ELECTRE_Tri.py** code is to retrieve the analysis data from the csv files. The functions "**input_criteria**", "**input_performances**" and "**input_thresholds**" are used for this.
___
***input_criteria(name)***

Generates from a .csv file the list of criteria and the dictionary of weights.

    :param name: Name of the .csv file which must contain on the first line the
        name of the criteria and on the second line the weightings.

    :return C: List of strings corresponding to the names of the criteria in the
        order they are given in the csv file.

    :return W: Dictionary where the keys are the names of the criteria and the
        values are the corresponding weightings.
___
***input_performances(name)***

Generates from a .csv file the list of actions and the performance dictionary.

    :param name: Name of the .csv file which must contain on the first line the names
        of the actions, on the second line the names of the criteria and on the
        following lines the performance of each action against each criterion.

    :return A: List of strings corresponding to the names of the actions in the order
        in which they are given in the csv file.

    :return P: Dictionary in which the keys are the names of the actions and the values
        are dictionaries where the keys are the criteria and the values are the
        performances.
___
***input_thresholds(name_moderate, name_good)***

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
        and the values are dictionaries in which the keys are the criteria and the values
        are a list containing the data of bk, qi, pi and vi.

## 2. Concordance indices

The following function calculates the concordance indices by criteria. This is an indicator of how well an action ***a(i)*** is at least as good as the reference profil ***b(k)*** for a given criterion ***j***.
___
***concordance(CRITERIA, ACTIONS, PERFORMANCES, THRESHOLDS, CATEGORIES)*** 

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

## 3. Discordance indices

The following function calculates the discordance indices by criteria. This indicator is expressed using the veto threshold. They mark the limit beyond which the hypothesis that a given action ***a(i)*** outperforms a reference profile ***b(k)*** for a given criterion ***j*** can be rejected without affecting the credibility of the opposite hypothesis.
___
***discordance(CRITERIA, ACTIONS, PERFORMANCES, THRESHOLDS, CATEGORIES)***

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

## 4. Global concordance indices

The global concordance indices allow to state to what extent the hypothesis "the action ***a(i)*** globally outperforms the reference profile ***b(k)***" is met.
___
***global_concordance(CONCORDANCE, CRITERIA, ACTIONS, WEIGHTS)***

Calculates the global concordances vectors for a given reference profile using a given concordance matrix.

    :param CONCORDANCE: Matrix of concordance of actions with regard to
        a given reference profile.

    :param CRITERIA: List containing the names of the criteria as strings.

    :param ACTIONS: List containing the names of the actions as strings.

    :param WEIGHTS: Dictionary containing the weightings of each criterion.

    :return Global_concordance: Dictionary containing two vectors corresponding
        to the global concordance of the actions Si with the reference profile
        defined in input bk, and of bk with the actions Si.
        The keys are '(ai,bk)' and '(bk,ai)'.

## 5. Credibility

In the ELECTRE-Tri method, the credibility of the outranking relationships between the scenarios and the reference profiles varies from pair to pair and is represented by the degree of credibility of the outranking.
___
***credibility(GLOBAL_CONCORDANCE, DISCORDANCE, CRITERIA, ACTIONS)***

Calculates the credibility vectors for a given reference profile using the global concordance vector and the discordance matrix for the same reference profile.

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

## 6. Over-ranking relation

This function dedicated to over ranking relationships uses the lambda cut-off value and the credibility values to decide on four over ranking relationships.
___
***over_ranking_relations(CREDIBILITY_MODERATE, CREDIBILITY_GOOD, LAMBDA)***

Built the over ranking relations matrix using the credibility vectors and the cutting threshold. The result is a matrix containing the following four outranking relations:
- preference of *a(i)* over *b(k)*: "**>**"
- preference of *b(k)* over *a(i)*: "**<**"
- indifference: "**I**"
- incomparability: "**R**".


    :param CREDIBILITY_MODERATE: List of credibility values for the reference profil
    "Moderate".

    :param CREDIBILITY_GOOD: List of credibility values for the reference profil "Good".

    :param LAMBDA: Cutting threshold value.

    :return over_ranking: Dictionary containing the over ranking relation and where
    the keys are 'Floor', 'Moderate', 'Good' and 'Roof', représenting the limits and
    boundaries of the three different categories.

## 7. Pessimistic and Optimistic sorting

Two sorting procedures specific to the ELECTRE-Tri method are performed on the basis of these over ranking relationships. Each of these sorting procedures assigns the actions studied to one of three performance categories: Bad "**_C1_**", Moderate "_**C2**_" or Good "**_C3_**". The difference between the two procedures is the ranking of incomparabilities (***R***).

For pessimistic sorting an incomparability relationship between a action ***a(i)*** and a reference profile ***b(k)*** moves the action into the lower performance category.

For optimistic sorting an incomparability relationship between a action ***a(i)*** and a reference profile ***b(k)*** moves the action into the upper performance category.
___
***pessimistic_sorting(ACTIONS, OVER_RANKING, CATEGORIES)***

***optimistic_sorting(ACTIONS, OVER_RANKING, CATEGORIES)***

Ranks actions in the three different categories according to a pessimistic or optimistic procedure.

    :param ACTIONS: List containing the names of the actions as strings.

    :param OVER_RANKING: Dictionary containing the over ranking relations.

    :param CATEGORIES: List containing the names of the three different categories.

    :return: ranking: Dictionary containing the rank of each actions according to a
    pessimistic or optimistic procedure. The keys are the actions and the values are 
    the median ranks.

    :return: category: Dictionary containing the three different categories and the actions
        they contain. The keys are the categories 'Bad', 'Moderate', and 'Good'. The values
        are lists containing the actions.

## 8. Median rank

When the two sorting procedures do not lead to the same results, a median rank is calculated. Thus an action classified as "**_C2_**" by the optimistic sorting and "**_C1_**" by the pessimistic sorting, will therefore belong to the "**_C12_**" category with a median rank of **1.5** (it will be less preferable than a scenario belonging to the "**_C22_**" category with a median rank of **2.0**).
___
***median_rank(ACTIONS, PESSIMISTIC_SORTING, OPTIMISTIC_SORTING)***

Calculates the median rank of each action.

    :param ACTIONS: List containing the names of the actions as strings.

    :param PESSIMISTIC_SORTING: Dictionary containing the actions classified according to
        the pessimistic procedure

    :param OPTIMISTIC_SORTING: Dictionary containing the actions classified according to
        the optimistic procedure.

    :return med_rank: Dictionary containing the median rank of each action. The keys are the
        names of the actions and the values are the median ranks.

## 9. Display

When all the steps are completed, it is then possible to display results with the "***display_results***" function for a better visualisation of the ranking of the actions and of the median ranks.
___
***display_results(ACTIONS, PESSIMISTIC_SORTING, OPTIMISTIC_SORTING, MEDIAN_RANK)***

Display of the median ranks and of the categories in which each action is classified.

    :param ACTIONS: List containing the names of the actions as strings.

    :param PESSIMISTIC_SORTING: Dictionary containing the actions classified according to
        the pessimistic procedure.

    :param OPTIMISTIC_SORTING: Dictionary containing the actions classified according to
        the optimistic procedure.

    :param MEDIAN_RANK: Dictionary containing the median rank of each action.