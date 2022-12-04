""" RobotsMaliAI: Bayelemaba """

import datasets

_CITATION = """\
@misc{bayelemaba2022
    title={Machine Learning Dataset Development for Manding Languages},
    author={
        Valentin Vydrin and
        Christopher Homan and
        Michael Leventhal and
        Allashera Auguste Tapo and
        Marco Z... and
        INALCO Members

    },
    howpublished = {url{https://github.com/robotsmali-ai/datasets}},
    year={2022}
}
"""

_DESCRIPTION = """\
The Bayelemabaga dataset is a collection of 44160 aligned machine translation ready Bambara-French lines, 
originating from Corpus Bambara de Reference. The dataset is constitued of text extracted from 231 source files, 
varing from periodicals, books, short stories, blog posts, part of the Bible and the Quran.
"""

_URL = {
    "parallel": "https://robotsmali-ai.github.io/datasets/bayelemabaga.tar.gz"
}

_LanguagePairs = [
    "bam-fr", "fr-bam"]

class BayelemabagaConfig(datasets.BuilderConfig):
    """ BuilderConfig for Bayelemabaga """

    def __init__(self, language_pair, **kwargs) -> None:
        """
        Args:
            language_pair: language pair, you want to load
            **kwargs: -> Super()
        """
        super().__init__(**kwargs)

        self.language_pair = language_pair

class Bayelemabaga(datasets.GeneratorBasedBuilder):
    """ Bi-Lingual Bam, Fr text made for Machine Translation """

    VERSION = datasets.Version("1.0.0")
    BUILDER_CONFIG_CLASS = BayelemabagaConfig

    BUILDER_CONFIGS = [
        BayelemabagaConfig(name="bam-fr", description=_DESCRIPTION, language_pair="bam-fr"),
        BayelemabagaConfig(name="fr-bam", description=_DESCRIPTION, language_pair="fr-bam")
    ]

    def _info(self):
        src_tag, tgt_tag = self.config.language_pair.split("-")
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features({"translation": datasets.features.Translation(languages=(src_tag, tgt_tag))}),
            supervised_keys=(src_tag, tgt_tag),
            homepage="https://robotsmali-ai.github.io/datasets",
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        lang_pair = self.config.language_pair
        src_tag, tgt_tag = lang_pair.split("-")

        archive = dl_manager.download(_URL["parallel"])

        train_dir = "bayelemabaga/train"
        valid_dir = "bayelemabaga/valid"
        test_dir = "bayelemabaga/test"
        
        train = datasets.SplitGenerator(
            name=datasets.Split.TRAIN,
            gen_kwargs = {
                "filepath": f"{train_dir}/train.{src_tag}",
                "labelpath": f"{train_dir}/train.{tgt_tag}",
                "files": dl_manager.iter_archive(archive)
            }
        )

        valid = datasets.SplitGenerator(
            name=datasets.Split.VALIDATION,
            gen_kwargs = {
                "filepath": f"{valid_dir}/dev.{src_tag}",
                "labelpath": f"{valid_dir}/dev.{tgt_tag}",
                "files": dl_manager.iter_archive(archive)
            }
        )

        test = datasets.SplitGenerator(
            name=datasets.Split.TEST,
            gen_kwargs = {
                "filepath": f"{test_dir}/test.{src_tag}",
                "labelpath": f"{test_dir}/test.{tgt_tag}",
                "files": dl_manager.iter_archive(archive)
            }
        )

        output = []

        output.append(train)
        output.append(valid)
        output.append(test)

        return output
    
    def _generate_examples(self, filepath, labelpath, files):
        """ Yield examples """
        src_tag, tgt_tag = self.config.language_pair.split("-")
        src, tgt = None, None

        for path, f in files:
            if(path == filepath):
                src = f.read().decode("utf-8").split("\n")[:-1]
            elif(path == labelpath):
                tgt = f.read().decode("utf-8").split("\n")[:-1]
            
            if(src is not None and tgt is not None):
                for idx, (s,t) in enumerate(zip(src, tgt)):
                    yield idx, {"translation": {src_tag: s, tgt_tag: t}}
                break
