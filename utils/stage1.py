import os


def readFile(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            text = f.readlines()[0].split(",")
            text[-1] = text[-1][:-1]
            return text


def createFileFromList(path, list):
    with open(path, "w") as f:
        f.write(",".join(list))
        f.write("\n")


def generateNewRating(oldRating):
    try:
        r1, r2 = oldRating.split("-")
        return r1.zfill(3) + "-" + r2
    except ValueError:
        return oldRating.zfill(3)


def fixData(path):
    for file in os.listdir(path):
        oldName, ext = file.split(".")
        arg1, arg2, arg3, oldRating = oldName.split("_")

        newRating = generateNewRating(oldRating)

        newName = "_".join([arg1.lower(), arg2, arg3, newRating]) + "." + ext
        os.rename(os.path.join(path, file), os.path.join(path, newName))


def prepareData(
    pathToAllFilenames,
    pathToAllRatings,
    pathToGivenFiles,
    pathToGivenFilenames,
    pathToGivenRatings,
):
    allFilenames = readFile(pathToAllFilenames)
    allRatings = readFile(pathToAllRatings)

    givenFilenames = [fn for fn in os.listdir(pathToGivenFiles)]
    givenFilenames.sort()

    givenRatings = []
    for fn in givenFilenames:
        givenRatings.append(allRatings[allFilenames.index(fn.split(".")[0])])

    createFileFromList(pathToGivenFilenames, givenFilenames)
    createFileFromList(pathToGivenRatings, givenRatings)
