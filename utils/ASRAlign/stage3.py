import os
import soundfile
import numpy as np
import pandas as pd

pathToGivenFiles = "data/files"
pathToASRAlignerInference = "output/ASRAlign/inference.csv"
pathToS2TInference = "output/S2T/inference.csv"


def getInferences(aligner):
    inferences = []

    listOfGivenFiles = os.listdir(pathToGivenFiles)
    listOfGivenFiles.sort()

    df = pd.read_csv(pathToS2TInference)

    for i, filename in enumerate(listOfGivenFiles):
        print(f"---> [{i + 1}] Working on {filename} ... ", end="", flush=True)

        pathToGivenFile = os.path.join(pathToGivenFiles, filename)
        speech, fs = soundfile.read(pathToGivenFile)

        text = "utt0 " + str(df[df["filename"] == filename]["hypothesis"].values[0])

        inference = aligner(speech, text, fs=fs)

        inferences.append(
            np.array(
                [
                    filename,
                    str(inference).split(" ")[4],
                ]
            )
        )

        print(f"Done", flush=True)

    return np.asarray(inferences)


def storeInferences(inferences):
    df = pd.DataFrame(
        {
            "filename": inferences[:, 0],
            "score": inferences[:, 1],
        }
    )
    df.to_csv(pathToASRAlignerInference, index=False)


def inference(aligner):
    print("--> Getting Inferences", flush=True)
    inferences = getInferences(aligner)
    print("--> Done", flush=True)

    print("--> Storing Inferences", flush=True)
    storeInferences(inferences)
    print("--> Done", flush=True)
