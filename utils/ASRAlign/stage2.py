from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.asr_align import CTCSegmentation


def prepareAligner(
    modelName="Shinji Watanabe/librispeech_asr_train_asr_transformer_e18_raw_bpe_sp_valid.acc.best",
):
    d = ModelDownloader()
    model = d.download_and_unpack(modelName)
    aligner = CTCSegmentation(**model)
    aligner.set_config(gratis_blank=True)
    return aligner
