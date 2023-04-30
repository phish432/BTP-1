import utils.stage1 as stage1

pathToAllFilenames = "data/all_filenames.txt"
pathToAllRatings = "data/all_ratings.txt"
pathToGivenFiles = "data/files"
pathToGivenFilenames = "data/given_filenames.txt"
pathToGivenRatings = "data/given_ratings.txt"


def main():
    print("-> Stage 1 : Data Preparation", flush=True)

    print("---> Fixing data ... ", end="", flush=True)
    stage1.fixData(pathToGivenFiles)
    print("Done", flush=True)

    print("---> Preparing data ... ", end="", flush=True)
    stage1.prepareData(
        pathToAllFilenames,
        pathToAllRatings,
        pathToGivenFiles,
        pathToGivenFilenames,
        pathToGivenRatings,
    )
    print("Done", flush=True)

    print("-> Done", flush=True)


if __name__ == "__main__":
    main()
