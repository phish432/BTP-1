import utils.S2T.stage2 as stage2
import utils.S2T.stage3 as stage3
import utils.S2T.stage4 as stage4

modelName = "Shinji Watanabe/librispeech_asr_train_asr_transformer_e18_raw_bpe_sp_valid.acc.best"


def stage2Main():
    return stage2.prepareModel(modelName)


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
