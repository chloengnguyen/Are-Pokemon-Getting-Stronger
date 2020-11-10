
# Capstone Project: ****Are Pokemon Getting Stronger?****
 

## Introduction

Pokemon is the most popular video game series worldwide. The game is famous for its simple yet amazing gaming mechanics. Today, there are more than different 800 Pokemon in the game, and all have different natures, skills, and abilities. Although new concepts are introduced in every game, the series has stayed true to its core concept for over 25 years and is mostly balanced among 18 "types" of pokemon. Some speculate that newer Pokemon are more powerful compared to the old ones, having higher average "stats". Players often consider the stats of the Pokemon as an important key to build a competitive team. 


## Background 
**Power creep** is a phenomenon in which new additions to a game tends to get more powerful than the old alternatives. This phenominon occurs to encourage players to buy the newer content but it often leads to an unbalance in the game. Pokemon releases many games and each game (generation) contains different sets of Pokemon. 

There are 6 stats for each pokemon: **attack, defense, special attack, special defense, speed, HP**. The summation of these stats produces the base stat totoal (BST), which is used as a metric to measure a Pokemon strength in this study. 

The study aims to determine if there is a change in pokemon strength over 8 generations.

## Data Overview 
* Source :  http://pokemondb.net/
* Subject of study: 1044 pokemon records with ID, Type, Generation, and Stats. 

## Hypothesis

**Base Stat Total = HP + Speed + Attack + Defense + Special Attack + Special Defense**

* **Null Hypothesis** : Pokemons from older generations have the same base stats as those from newer generations.

* **Experiment Hypothesis**: Pokemon from older generations has lower base stats compared to those from newer generations.

## Techniques Used

1. I first scraped data from the Pokemon database using BeautifulSoup 
2. The dataset was cleaned and organized by Pandas and SQL. There are special Pokemon that shared an identical identification (ID) with the original Pokemon. The dataframe was rearranged to sort them in their appropriate groups/genrations. I wrote a function identify these special pokemon with a word identifier like "Mega" or "Alola" in their name.
3. The dataset was then split into two groups: new generations (I-IV) and new generations (V-VII). Generation IV is used as a marker as the game designers began to become more experimental with the game mechanics. 
4. After the two dataframes were constructed, I plotted histograms of the average base state for each groups.
5. An outlier function was used to return a list of outliers using three standard deviation as a threshold. Outliers from both dataframes were removed.
6. The last function calculated the p-value from a two sample t-test statistics. 

## Data Exploration
![Average of Stat Total Per Generation](https://github.com/chloengnguyen/Capstone-1/blob/master/graph/Average-Stat-Total.png)
![Pokemon's Stat Total from Older Generations ](https://github.com/chloengnguyen/Capstone-1/blob/master/graph/Total-Stat-OldGen.png)
![Pokemon's Stat Total from Newer Generations ](https://github.com/chloengnguyen/Capstone-1/blob/master/graph/Total-Stat-NewGen.png)
![Base Stat Total vs Individual Stat](https://github.com/chloengnguyen/Capstone-1/blob/master/graph/stats-matrix.png)

## Result & Conclusion 
* The p-value was found at 0.001125 which is lower than the confidence level (alpha) of 0.05. 
* The null hypothesis was rejected and the experiment hypothesis was accepted. 
* In conlusion, Pokemon from older generations has lower base stats compared to those from newer generations. 


## Additional Questions/ Works:
* In EDA, I observed there were some noticable trends in Pokemon type combinations in addition to stat changes. A future analysis can go down this route. 

![Common Primary Type](https://github.com/chloengnguyen/Capstone-1/blob/master/graph/single_type_pokemon.png)
![Common Secondary Type](https://github.com/chloengnguyen/Capstone-1/blob/master/graph/secondary_type_pokemon.png)
![Dual-type](https://github.com/chloengnguyen/Capstone-1/blob/master/graph/dual-type.png)


* Do the introduction of Mega Evolution skew my data?  
    Mega Evolution are modification of older pokemon and they are introduced later in the series. These new pokemon share the same pokedex number (id) as their original version but have higher stats. 
* Are all stats changing at the same rate? 
 
* In EDA, I observed there were some trends in type combination. In future study, a test statistic could be done 
----

