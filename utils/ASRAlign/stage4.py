import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pathToGivenFilenames = "data/given_filenames.txt"
pathToGivenRatings = "data/given_ratings.txt"
pathToASRAlignInference = "output/ASRAlign/inference.csv"
pathToASRAlignScores = "output/ASRAlign/scores.csv"
pathToASRAlignResults = "output/ASRAlign/results.txt"
pathToASRAlignPlots = "output/ASRAlign/plots.png"

reqCols = ["score", "rating"]


def getRatings():
    with open(pathToGivenRatings, "r") as f:
        ratings = f.readlines()[0].split(",")
        ratings[-1] = ratings[-1][:-1]
        return pd.DataFrame(ratings, columns=["rating"])


def getInferences():
    return pd.read_csv(pathToASRAlignInference)


def normalize(data):
    newData = (data - data.min()) / (data.max() - data.min())  # min-max normalization
    return (newData - newData.mean()) / newData.std()  # z-score normalization


def preprocessData():
    ratings = getRatings()
    inferences = getInferences()

    df = pd.concat([inferences, ratings], axis=1)
    df[reqCols] = df[reqCols].astype(float)
    # dfN = normalize(df[reqCols])
    # df[reqCols] = dfN
    df.to_csv(pathToASRAlignScores, index=False)


def calculateCorrelations():
    df = pd.read_csv(pathToASRAlignScores)
    dfScore = df[reqCols]

    with open(pathToASRAlignResults, "w") as f:
        f.write(str(dfScore.corr()))

    plt.figure(figsize=(19.2, 10.8), dpi=100)
    plt.title("ASR Aligner Score")
    plt.plot(df["score"], label="score", marker=".")
    plt.plot(df["rating"], label="rating", marker=".")
    plt.legend()
    plt.savefig(pathToASRAlignPlots)
