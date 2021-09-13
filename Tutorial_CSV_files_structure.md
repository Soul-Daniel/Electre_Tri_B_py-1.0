# Tutorial "CSV_files_structure"

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), France, 27/07/2021

## 1. Introduction

The Python code presented here requires some specific input data to work. This data must be stored as comma-separated values, known as CSV. This is a text file, as opposed to the so-called "binary" formats. Each line of text corresponds to a line in a table and commas are used to separate the columns. The portions of text separated by a comma thus correspond to the contents of the table cells. A line is an ordered sequence of characters terminated by an end-of-line character.


## CSV files structure

Within the source code, functions are assigned to import the input data and shape it for further processing. This input data should be provided in the form of csv files containing the names of the criteria and their weights, the names of the actions and their performances, the performances of the reference profiles and the different thresholds for each criterion.

*Note: There must be exactly four csv files that are described below.*

### csv file related to criteria and their weight

The first csv file concerns the criteria. 

It should contain on the first line the names of the criteria as strings separated by commas. To facilitate the use of the simulation results, the names of the criteria should be represented by numbering. For example the explicit criteria of a problem can be represented by the set {*g1*, *g2*, *g3*, *g4*, *g5*, *g6*}.

The second line should contain the weights of the criteria, also separated by commas. 

*Note: There should therefore be as many comma-separated text sections for the names of the criteria as for the weights.*

*Example: [Building_retrofit_scenarios_CRIT.csv](Building_retrofit_scenarios_CRIT.csv)*

### csv file related to actions and their performances

The second csv file concerns the actions.

It must contain on the first line the names of the actions as strings separated by commas. As for the criteria, the names of the actions must be represented by numbering. For example {*S1*, *S2*, *S3*, *S4*, *S5*, *S6*, *S8*, *S9*, *S10*}.

The second line must be identical to the name of the criteria separated by commas as in the criteria csv file.

Finally, the following lines should represent, in the correct order, the performance of the actions against each criterion. For example, the third line represents the performance of the action *S1* with regard to each criteria {*g1*, *g2*, *g3*, *g4*, *g5*, *g6*}. Then the next line the performance of the action *S2* and so on.

*Note: The performances of the actions must be numerical values.*

*Example: [Building_retrofit_scenarios_PERF.csv](Building_retrofit_scenarios_PERF.csv)*

### csv file related to the thresholds and reference profile for the "Good" category

The third csv file concerns the reference profile representing the boundaries between the "*Good*" and "*Moderate*" categories.

It must contain on the first line the name of the criteria separated by commas as in the criteria csv file.

The following line should contain, in the correct order, the performance of the reference profile for the criteria considered and the values of the indifference, preference and veto thresholds. For example, the second line must contain in the correct order and for the criterion "*g1*": the performance of the reference profile "*Good*", the indifference threshold "*qj*", the preference threshold "*pj*" and the veto threshold "*vj*". The next line will concern the analogous values for the criteria "*g2*" and so on.

*Note: There should be a first line with the names of the criteria and then as many lines as there are criteria. From the second line onwards, each line must contain four portions of value separated by a comma.*

*Example: [Building_retrofit_scenarios_THRG.csv](Building_retrofit_scenarios_THRG.csv)*

### csv file related to the thresholds and reference profile for the "Moderate" category

The fourth csv file concerns the reference profile representing the boundaries between the "*Moderate*" and "*Bad*" categories.

It must contain on the first line the name of the criteria separated by commas as in the criteria csv file.

The following line should contain, in the correct order, the performance of the reference profile for the criteria considered and the values of the indifference, preference and veto thresholds. For example, the second line must contain in the correct order and for the criterion "*g1*": the performance of the reference profile "*Moderate*", the indifference threshold "*qj*", the preference threshold "*pj*" and the veto threshold "*vj*". The next line will concern the analogous values for the criteria "*g2*" and so on.

*Note: Between the two csv files concerning the thresholds and reference profiles, only the performance of the reference profiles changes. The values of the different thresholds are absolute and remain the same for the different reference profiles.*

*Example: [Building_retrofit_scenarios_THRM.csv](Building_retrofit_scenarios_THRM.csv)*









