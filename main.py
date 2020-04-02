#KATHLEEN ANDERSON W/ YIZHEN WU

from utils import *
from pollingData import *
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

df = loadAndCleanData("PostSuperTuesday.csv")

#1 I think that Biden will win the democratic party to compete against Trump. In terms of presidential winnings 
  #it could very much go either way, but I honestly think Trump will still win because of his benefit of the electoral college.
 

#3 1. There are a lot of repeated Rows. 2. The spread is huge especially on Bernie Sanders' end. 3. What is Tulsi Gabbard doing at this point?


#6
normalizeData(df)

#7
for candidate in df.columns:
    if candidate not in ["Poll", "Date", "Sample", "Spread", "Undecided"]:
        plotCandidate(candidate, df)

#9
myCandidate = []
for candidate in df.columns:
    if candidate not in ["Poll", "Date", "Sample", "Spread", "Undecided"]:
        myCandidate.append(candidate)
        print(candidate.statsPerCandidate(candidate, df))

#11
df = cleanSample(df)
print(cleanSample)

#14
weightedStatsPerCandidate("Biden", df)
weightedStatsPerCandidate("Warren", df)
weightedStatsPerCandidate("Sanders", df)
weightedStatsPerCandidate("Biden", df)

#Biden is going to win based off the weighted summations.

#16
repeatedList = []

for candidate1 in myCandidate:
    for candidate2 in myCandidate:
        if candidate1 != candidate2:
            if [candidate1, candidate2] not in repeatedList and [canidate1, candidate2] not in repeatedList:
                print(candidate1 + "vs " + candidate2 + ": " + computerCorrelation(candidate1, candidate2, df))
                repeatedList.append([candidate1, candidate2])
#Biden and Klobuchar are the most correlated. 
#Sanders and Steyer are the least correlated.
 

#18
superTuesday(df, myCandidate)
print("Biden Mean: " + df["BidenST"].mean())
print("Sanders Mean: " + df["SandersST"].mean())
print("Biden Weighted Mean: " + weightedStatsPerCandidate("BidenST", df))
print("Sanders Weighted Mean: " + weightedStatsPerCandidate("SandersST", df))

#Biden will win as he is higher in stats for both weighted and unweighted averages.
 
#19
getConfidenceInterval(df["BidenST"])
getConfidenceInterval(df["SandersST"])

#The difference is super tiny. Biden=1.139 and Sanders=1.248, so 1.248-1.139=.109.

#20
print("Numbers: " + runTTest(df["Biden"], df["Sanders"]))
print("Aggregated Numbers: " + runTTest(df["BidenST"], df["SandersST"])) 

#I think the conclusions are pretty much the same, they just kind of get to the point faster as there's not so much to work with.


#22 Super Tuesday came through with old data proving that Biden will likely take this race in all factions. 
#This is such complicated data and such a large spread which explains that not everything can be solved with correlations and statistics in one setting.
