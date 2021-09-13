# ELECTRE-Tri MCDA Python

[![DOI](https://zenodo.org/badge/XXXXXXXXX.svg)]

https://mybinder.org/v2/gh/SoulJah-90/Electre_Tri_MCA_py-0.0.1/HEAD

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), France, 27/07/2021

[**ELECTRE_Tri.py**](ELECTRE_Tri.py) is a over-ranking multi criteria decision analysis procedure allowing the ranking of a number of alternatives related to an issue into categories in order to assist in decision-making. The code is based on the ELECTRE-Tri multi-criteria analysis method and aims to classify potential actions into a hierarchical set of 3 categories called "Bad", "Moderate" and "Good". The code is designed on the basis of these 3 categories but can be easily modified to take into account more categories. The particularity of the code is that it can be used to classify any action related to a decision problem as long as the input data is correctly provided.

## 1. Licence
Code is released under [MIT Lincence](https://choosealicense.com/licenses/mit/).

Docs are released under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

[![Creative Commons License](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

## 2. Quick explanations
In order to use a ELECTRE-Tri multi-criteria analysis method to select the best alternative among others, several steps must first be carried out:
- Identification of issues and objectives
- Definition of possible alternatives to achieve all or part of the objectives
- Definition of the criteria for the analysis
- Weighting of the different criteria
- Evaluation of the different alternatives regarding the different criteria
- Definition of thresholds and reference profiles.

Once these steps have been completed it is then possible to use the ELECTRE-Tri multi-criteria analysis method to determine the best alternative among those identified.

## 3. Installation

In order to use the ELECTRE-Tri code, you must have a Python interpreter installed on your computer (see [Python_interpreter]).
To execute the code it is also necessary to install the numpy ([NumPy module]) and csv modules ([CSV File Reading and Writing]).

## 4. How to use it

Typical workflow:

1. Go through all the steps defined above to define the composition of the multi-criteria analysis and build the performance matrix.
2. Store all the data of the problem in the different .csv files according to the structure defined in [Tutorial_CSV_files_structure.md](Tutorial_CSV_files_structure.md).
3. Indicate the correct name of the csv files to be imported for the analysis in the code [ELECTRE_Tri_main.py](ELECTRE_Tri_main.py).
4. Choose a lambda cutting threshold for the simulation.
5. Execute the code.
6. Interpreting the ranking results.

*Note: The correct execution of the code depends on the structuring of the csv data files. The information must be stored in a particular order.*

## 5. Contents
### 5.1 Tutorials

[Tutorial_ELECTRE_Tri.md](Tutorial_ELECTRE_Tri.md): Tutorial explaining how the calculation code [ELECTRE_Tri.py](ELECTRE_Tri.py) is built.

[Tutorial_ELECTRE_Tri_main.md](Tutorial_ELECTRE_Tri_main.md): Tutorial explaining the structure and functionalities of the executable code [ELECTRE_Tri_main.py](ELECTRE_Tri_main.py).

[Tutorial_CSV_files_structure.md](Tutorial_CSV_files_structure.md): Tutorial explaining what structure the different csv files must have in order to be interpreted by the executable.

*Note: The tutorials documents are used to explain the logic behind the calculation codes and how to use them.* 

### 5.2 Examples
#### 5.2.1 Description

[Description_Building_retrofit_scenarios.md](Description_Building_retrofit_scenarios.md): Document describing the origin and composition of the data for the example of multi-criteria decision support for the retrofit scenarios of a collective housing building.

[Description_Wall_insulation_scenarios.md](Description_Wall_insulation_scenarios.md): Document describing the origin and composition of the data related to the example of multi-criteria decision support for external thermal insulation scenarios of a collective housing building.

*Note: The description documents are used to explain how the examples are constructed and what they are made of.* 

#### 5.2.2 CSV files

[Building_retrofit_scenarios_CRIT.csv](Building_retrofit_scenarios_CRIT.csv): Example of a csv file containing the different data related to the criteria for the analysis of retrofit scenarios in the case of a collective housing building.

[Building_retrofit_scenarios_PERF.csv](Building_retrofit_scenarios_PERF.csv): Example of a csv file containing the different data related to actions and their performances for the analysis of retrofit scenarios in the case of a collective housing building.

[Building_retrofit_scenarios_THRG.csv](Building_retrofit_scenarios_THRG.csv): Example of a csv file containing the different data related to the thresholds and reference profile for the "Good" category in the case of the analysis of retrofit scenarios in the case of a collective housing building.

[Building_retrofit_scenarios_THRM.csv](Building_retrofit_scenarios_THRM.csv): Example of a csv file containing the different data related to the thresholds and reference profile for the "Moderate" category in the case of the analysis of retrofit scenarios in the case of a collective housing building.

[Wall_insulation_scenarios_CRIT.csv](Wall_insulation_scenarios_CRIT.csv): Example of a csv file containing the different data related to the analysis criteria of external thermal insulation scenarios for a collective housing building.

[Wall_insulation_scenarios_PERF.csv](Wall_insulation_scenarios_PERF.csv): Example of a csv file containing the different performance data related to the possible scenarios for external thermal insulation for a collective housing building.

[Wall_insulation_scenarios_THRG.csv](Wall_insulation_scenarios_THRG.csv): Example of a csv file containing the different data related to the thresholds and the reference profile for the "good" category in the case of the choice of an external thermal insulation material for a collective housing building.

[Wall_insulation_scenarios_THRM.csv](Wall_insulation_scenarios_THRM.csv): Example of a csv file containing the different data related to the thresholds and the reference profile for the "moderate" category in the case of the choice of an external thermal insulation material for a collective housing building.


[Python_interpreter]:https://www.python.org/

[NumPy module]:https://numpy.org/doc/stable/reference/

[CSV File Reading and Writing]:https://docs.python.org/3/library/csv.html

