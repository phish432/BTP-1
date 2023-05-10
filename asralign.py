import utils.ASRAlign.stage2 as stage2
import utils.ASRAlign.stage3 as stage3
import utils.ASRAlign.stage4 as stage4
import sys

modelName = "Shinji Watanabe/librispeech_asr_train_asr_transformer_e18_raw_bpe_sp_valid.acc.best"


def stage2Main():
    return stage2.prepareAligner(modelName)


def stage3Main(speech2textModel):
    stage3.inference(speech2textModel)


def stage4Main():
    print("--> Pre-Processing ... ", end="", flush=True)
    stage4.preprocessData()
    print("Done", flush=True)

    print("--> Calculating Correlations ... ", end="", flush=True)
    stage4.calculateCorrelations()
    print("Done", flush=True)


def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "4":
            print("-> Stage 4 : Data Processing", flush=True)
            stage4Main()
            print("-> Done", flush=True)
        else:
            print(f"-> Error: Invalid Argument - '{sys.argv[1]}'", flush=True)
    else:
        print("-> Stage 2 : Model Creation", flush=True)
        speech2textModel = stage2Main()
        print("-> Done", flush=True)

        print("-> Stage 3 : Inference", flush=True)
        stage3Main(speech2textModel)
        print("-> Done", flush=True)

        print("-> Stage 4 : Data Processing", flush=True)
        stage4Main()
        print("-> Done", flush=True)


if __name__ == "__main__":
    main()
