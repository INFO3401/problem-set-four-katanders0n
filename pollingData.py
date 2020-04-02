import matplotlib.pyplot as plt

#5
def normalizeData(df):
    x=df.copy()
    sumList=[]

    for i, row in x.iterrows():
        row.drop(labels=["Poll","Date","Sample","Spread"], inplace=True)
        print(row)
        sumList.append(100-sum(row))

    x["Undecided"]=sumList
    print(x)

#7
def plotCandidate(candidate, df):
    plt.scatter(y=df[candidate],x=df["Poll"])
    plt.title(candidate+"Polling")
    plt.ylim(0) #the end
    plit.show()

#8
def statsPerCandidate(candidate, df):
    return df[candidate].mean()

#10
def cleanSample(df):
    sampleType=[] and sampleSize=[]
    for i in df["Sample"]:
        sampleType.append(i[-2:])
        sampleSize.append(i[-2:])
    df["Sample Type"]=sampleType
    df["Sample Size"]=sampleSize
    return df

#12
def computePollWeight(df, poll):
    x=df["Poll"]==poll
    sumOfX=sum(x["Sample Size"])
    y=sum(df["Sample Size"])
    return sumOfX/y

#13
def weightedStatsPerCandidate(candidate, df):
    weightedAverages=[]
    for poll in df["Poll"].unique():
        x=sum(df[df["Poll"]==poll][candidate])
        y=computePollWeight(df,poll)
        weightedAverages.append(x*y)
    return sum(weightedAverages)/len(weightedAverages)

#15
def computerCorrelation(candidate1, candidate2, df):
    return df[candidate1].corr(df[candidate2])

#17
def superTuesday(df, candidates):
    BidenSuperTuesday=[]
    SandersSuperTuesday=[]

    for i, row in df.interrows():
        BidenCount=row["Biden"]
        SandersCount=row["Sanders"]
        for candidate in candidates:
            if candidate != "Sanders" and candidate != "Biden":
                BidenCorrelation=computerCorrelation("Biden", candidate, df)
                SandersCorrelation=computerCorrelation("sanders", candidate, df)
                if abs(BidenCorrelation)>abs(SandersCorrelation):
                    BidenCount+=row[candidate]
                else:
                    SandersCount+=row[candidate]
        BidenSuperTuesday.append(BidenCount)
        SandersSuperTuesday.append(SandersCount)

    df["BidenST"]=BidenSuperTuesday
    df["SandersST"]=SandersSuperTuesday