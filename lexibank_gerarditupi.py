"""
Build lexibank dataset for `gerarditupi`.
"""

from pathlib import Path
import attr

from pylexibank import Concept, Language
from pylexibank.dataset import Dataset as BaseDataset
from pylexibank.util import progressbar, getEvoBibAsBibtex

from clldutils.misc import slug


@attr.s
class CustomConcept(Concept):
    Number = attr.ib(default=None)


@attr.s
class CustomLanguage(Language):
    Latitude = attr.ib(default=None)
    Longitude = attr.ib(default=None)
    SubGroup = attr.ib(default=None)
    Source = attr.ib(default=None)


class Dataset(BaseDataset):
    dir = Path(__file__).parent
    id = "gerarditupi"
    concept_class = CustomConcept
    language_class = CustomLanguage

    def cmd_makecldf(self, args):
        # Write sources to CLDF
        args.writer.add_sources()

        # Collect languages and add to CLDF, also building look-up
        languages = {}
        for language in self.languages:
            args.writer.add_language(
                ID=language["ID"],
                Name=language["Name"],
                Glottocode=language["Glottocode"],
            )
            languages[language["Name"]] = {
                "ID": language["ID"],
                "Source": language["Source"].split(","),
            }

        # Collect concepts and add to CLDF, also building look-up
        concepts = {}
        for concept in self.concepts:
            idx = "{0}_{1}".format(concept["NUMBER"], slug(concept["ENGLISH"]))
            args.writer.add_concept(
                ID=idx, Name=concept["ENGLISH"], Concepticon_ID=concept["CONCEPTICON"]
            )
            concepts[concept["ENGLISH"]] = idx

        # Define a list os string replacements -- as the raw data is already
        # segmented, and these few cases are actually inconsistencies, it is better
        # than jus tusing a profile
        replacements = {
            "wu": ["w", "u"],
            "wã": ["w", "ã"],
            "ja": ["j", "a"],
            "oj": ["oi"],
            "kãʔã": ["k", "ã", "ʔ", "ã"],
            "ej": ["ei̯"],
            "ij": ["ii̯"],
            "ɨp": ["ɨ", "p"],
            "ɪw": ["ɪu̯"],
            "e͂": ["ẽ"],
        }

        missing, missing2 = set(), set()
        for row, cog in progressbar(
            zip(
                self.raw_dir.read_csv(
                    "Aligned_matrix_lexical.csv", delimiter=",", dicts=True
                ),
                self.raw_dir.read_csv("Cognate matrix.csv", delimiter=",", dicts=True),
            )
        ):
            language = row[""].strip()
            for concept, concept_id in concepts.items():
                if concept in row:
                    word = row[concept]
                    if word.strip() and language.strip():
                        segments = []
                        for segment in word.split():
                            segments += replacements.get(segment, [segment])
                        lexeme = args.writer.add_form_with_segments(
                            Language_ID=languages[language]["ID"],
                            Parameter_ID=concept_id,
                            Value=row[concept],
                            Form=row[concept],
                            Segments=segments,
                            Source=languages[language]["Source"],
                        )
                        if concept in cog:
                            args.writer.add_cognate(
                                lexeme=lexeme,
                                Cognateset_ID="{0}-{1}".format(
                                    slug(concept), cog[concept]
                                ),
                                Source="gerarditupi",
                            )
                        else:
                            missing.add(concept)
                else:
                    missing2.add(concept)

        # Log missing concepts
        for concept in missing:
            args.log.warn("Concept {0} could not be found".format(concept))
        for concept in missing2:
            args.log.warn("Concept {0} missing".format(concept))
