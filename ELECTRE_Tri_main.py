import ELECTRE_Tri
import pandas as pd

# Cutting threshold
λ = 0.75

# Names of categories
Categories = ['Bad', 'Moderate', 'Good']

###################################################################################################
#                                      Input data import                                          #
###################################################################################################

Criteria, Weights = ELECTRE_Tri.input_criteria('Building_retrofit_scenarios_CRIT.csv')
Actions, Performances = ELECTRE_Tri.input_performances('Building_retrofit_scenarios_PERF.csv')
Thresholds = ELECTRE_Tri.input_thresholds('Building_retrofit_scenarios_THRM.csv', 'Building_retrofit_scenarios_THRG.csv')

###################################################################################################
#                   Calculation of the indicators of the Electre Tri method                       #
###################################################################################################

# Calculation of the concordance matrices for the two reference profiles
Concordance_b1 = ELECTRE_Tri.concordance(Criteria, Actions, Performances, Thresholds, 'Moderate')
Concordance_b2 = ELECTRE_Tri.concordance(Criteria, Actions, Performances, Thresholds, 'Good')

# Calculation of the discordance matrices for the two reference profiles
Discordance_b1 = ELECTRE_Tri.discordance(Criteria, Actions, Performances, Thresholds, 'Moderate')
Discordance_b2 = ELECTRE_Tri.discordance(Criteria, Actions, Performances, Thresholds, 'Good')

# Calculation of the global concordances vectors for the two reference profiles
Global_concordance_b1 = ELECTRE_Tri.global_concordance(Concordance_b1, Criteria, Actions, Weights)
Global_concordance_b2 = ELECTRE_Tri.global_concordance(Concordance_b2, Criteria, Actions, Weights)

# Calculation of the credibility vectors for the two reference profiles
Credibility_b1 = ELECTRE_Tri.credibility(Global_concordance_b1, Discordance_b1, Criteria, Actions)
Credibility_b2 = ELECTRE_Tri.credibility(Global_concordance_b2, Discordance_b2, Criteria, Actions)

# Building the matrix of outranking relations
Over_ranking = ELECTRE_Tri.over_ranking_relations(Credibility_b1, Credibility_b2, λ)

###################################################################################################
#                      Ranking of actions and calculation of median ranks                         #
###################################################################################################

# Ranking of actions in the three categories according to the pessimistic procedure and display of the result
Pessimistic_sorting = ELECTRE_Tri.pessimistic_sorting(Actions, Over_ranking, Categories)
print(' ')
print("Results of the pessimistic sorting : ")
print('Bad :', Pessimistic_sorting[0]['Bad'])
print('Moderate :', Pessimistic_sorting[0]['Moderate'])
print('Good :', Pessimistic_sorting[0]['Good'])
print('Pessimistic category :', Pessimistic_sorting[1])

# Ranking of actions in the three categories according to the optimistic procedure and display of the result
Optimistic_sorting = ELECTRE_Tri.optimistic_sorting(Actions, Over_ranking, Categories)
print(' ')
print('Results of the optimistic sorting : ')
print('Bad :', Optimistic_sorting[0]['Bad'])
print('Moderate :', Optimistic_sorting[0]['Moderate'])
print('Good :', Optimistic_sorting[0]['Good'])
print('Optimistic category : ', Optimistic_sorting[1])
print(' ')

# Calculating the median rank of each share
Median_rank = ELECTRE_Tri.median_rank(Actions, Pessimistic_sorting, Optimistic_sorting)

###################################################################################################
#                                     Display of the results                                      #
###################################################################################################

# Display of the median ranks and of the categories in which each action is classified
ELECTRE_Tri.display_results(Actions, Pessimistic_sorting, Optimistic_sorting, Median_rank)
