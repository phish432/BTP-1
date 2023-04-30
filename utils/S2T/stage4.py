import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pathToGivenFilenames = "data/given_filenames.txt"
pathToGivenRatings = "data/given_ratings.txt"
pathToS2TInference = "output/S2T/inference.csv"
pathToS2TScores = "output/S2T/scores.csv"
pathToS2TResults = "output/S2T/results.txt"

reqCols = ["overall-score", "decoder-score", "lm-score", "ctc-score", "rating"]


def getRatings():
    with open(pathToGivenRatings, "r") as f:
        ratings = f.readlines()[0].split(",")
        ratings[-1] = ratings[-1][:-1]
        return pd.DataFrame(ratings, columns=["rating"])


def getInferences():
    return pd.read_csv(pathToS2TInference)


def normalize(data):
    newData = (data - data.min()) / (data.max() - data.min())  # min-max normalization
    return (newData - newData.mean()) / newData.std()  # z-score normalization


def preprocessData():
    ratings = getRatings()
    inferences = getInferences()

    df = pd.concat([inferences, ratings], axis=1)
    df[reqCols] = df[reqCols].astype(float)
    dfN = normalize(df[reqCols])
    df[reqCols] = dfN
    df.to_csv(pathToS2TScores, index=False)


def calculateCorrelations():
    df = pd.read_csv(pathToS2TScores)
    dfScore = df[reqCols]

    with open(pathToS2TResults, "w") as f:
        f.write(str(dfScore.corr()))

    plt.figure(figsize=(19.2, 10.8), dpi=100)

    plt.subplot(221)
    plt.title("Overall Score")
    plt.plot(df["overall-score"], label="overall-score", marker=".")
    plt.plot(df["rating"], label="rating", marker=".")
    plt.legend()

    plt.subplot(222)
    plt.title("Decoder Score")
    plt.plot(df["decoder-score"], label="decoder-score", marker=".")
    plt.plot(df["rating"], label="rating", marker=".")
    plt.legend()

    plt.subplot(223)
    plt.title("LM Score")
    plt.plot(df["lm-score"], label="lm-score", marker=".")
    plt.plot(df["rating"], label="rating", marker=".")
    plt.legend()

    plt.subplot(224)
    plt.title("CTC Score")
    plt.plot(df["ctc-score"], label="ctc-score", marker=".")
    plt.plot(df["rating"], label="rating", marker=".")
    plt.legend()

    plt.savefig("output/S2T/plots.png")
