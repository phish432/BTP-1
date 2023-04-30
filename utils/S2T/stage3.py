import string
import os
import soundfile
import pandas as pd
import numpy as np

pathToGivenFiles = "data/files"
pathToS2TInference = "output/S2T/inference.csv"


def text_normalizer(text):
    text = text.upper()
    return text.translate(str.maketrans("", "", string.punctuation))


def getInferences(speech2text):
    inferences = []

    listOfGivenFiles = os.listdir(pathToGivenFiles)
    listOfGivenFiles.sort()

    for i, filename in enumerate(listOfGivenFiles):
        print(f"---> [{i + 1}] Working on {filename} ... ", end="", flush=True)

        pathToGivenFile = os.path.join(pathToGivenFiles, filename)
        speech, _ = soundfile.read(pathToGivenFile)

        texts = speech2text(speech)
        text = texts[0]

        inferences.append(
            np.array(
                [
                    filename,
                    text_normalizer(text[0]),
                    text[-1].score.item(),
                    text[-1].scores["decoder"].item(),
                    text[-1].scores["lm"].item(),
                    text[-1].scores["ctc"].item(),
                ]
            )
        )

        print(f"Done", flush=True)

    return np.asarray(inferences)


def storeInferences(inferences):
    df = pd.DataFrame(
        {
            "filename": inferences[:, 0],
            "hypothesis": inferences[:, 1],
            "overall-score": inferences[:, 2],
            "decoder-score": inferences[:, 3],
            "lm-score": inferences[:, 4],
            "ctc-score": inferences[:, 5],
        }
    )
    df.to_csv(pathToS2TInference, index=False)


def inference(speech2text):
    print("--> Getting Inferences", flush=True)
    inferences = getInferences(speech2text)
    print("--> Done", flush=True)

    print("--> Storing Inferences", flush=True)
    storeInferences(inferences)
    print("--> Done", flush=True)
