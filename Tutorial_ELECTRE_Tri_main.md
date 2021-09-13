# Tutorial "ELECTRE_Tri_main.py"

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), France, 27/07/2021

## Introduction

In order to dissociate the representative functions of the ELECTRE-Tri method and their execution in the case of examples or concrete applications, a "main" executable code has been created. The [**ELECTRE_Tri_main.py**](ELECTRE_Tri_main.py) code is the executable. It contains the different instructions that will lead to the construction of the objects used throughout the method. The different stages of this executable code are presented here.

## 1. First step

#### 1.1 Cutting threshold
The first step is to define the "**cutting threshold λ**". The cutting threshold is the basis of the comparison. It allows to decide on the existing over-ranking relationships between actions "*a*" and "*b*". The closer it is to 1, the more demanding the ranking will be. The most common values for this cutting threshold are generally between *0.60* and *0.75*.

#### 1.2 Categories
The names of the different categories should then be given in ascending order. Be careful here as the **[Categories]** list cannot be modified without changing the source code. As a reminder, the code has been built on the basis of three categories which are "**Bad**", "**Moderate**", and "**Good**".

## 2. Second step

The second step consist of importing the input data of the problem. These data should be stored in csv files according to the data structure presented in the document [Tutorial_CSV_files_structure.md](Tutorial_CSV_files_structure.md). There should be four such files:
- a csv file containing the different data related to the criteria and their weight. 

    *Example: [Building_retrofit_scenarios_CRIT.csv](Building_retrofit_scenarios_CRIT.csv)*
    
- a csv file containing the different data related to actions and their performances. 

    *Example: [Building_retrofit_scenarios_PERF.csv](Building_retrofit_scenarios_PERF.csv)*
    
- a csv file containing the different data related to the thresholds and reference profile for the "Good" category. 

    *Example: [Building_retrofit_scenarios_THRG.csv](Building_retrofit_scenarios_THRG.csv)*
    
- a csv file containing the different data related to the thresholds and reference profile for the "Moderate" category. 

    *Example: [Building_retrofit_scenarios_THRM.csv](Building_retrofit_scenarios_THRM.csv)*

To import the data, the following functions are used, where the input parameters are of the csv files names:
- "**_input_criteria(name)_**"
- "**_input_performances(name)_**"
- "**_input_thresholds(name_moderate, name_good)_**"

These functions will then return the different objects needed for the rest of the process.

## 3. Third step

In the third step the objective is to use the input data to calculate the indicators of the ELECTRE-Tri method. To calculate these indicators we use the following functions:
- Calculation of concordance indices by criteria: "***concordance***"
- Calculation of discordance indices by criteria: "***discordance***"
- Calculation of global concordance indices: "***global_concordance***"
- Calculation of credibility degrees: "***credibility***"
- Construction of the outranking relationships: "***over_ranking_relations***"

Particular attention should be paid to the calculation of these indicators. Each of them must be calculated as many times as there are reference profiles. This means that the functions used to perform these calculations must be called several times except for the construction of the over-ranking relationships.

## 4. Fourth step

#### 4.1 Ranking of actions
The fourth step consists in classifying the actions in the categories, based on the outranking relations obtained previously, and following two ranking procedures: "**optimistic sorting**" and "**pessimistic sorting**".

To achieve this sorting we call the two functions "***pessimistic_sorting***" and "***optimistic_sorting***" and display the result of the ranking in the form of lists representing the categories and containing the actions.

#### 4.2 Calculation of median rank
In this fourth step the median rank of each action is also calculated with the function "***median_rank***".

## 5. Fifth step

When all the steps are completed, it is then possible to display results with the "***display_results***" function for a better visualisation of the ranking of the actions and of the median ranks.
