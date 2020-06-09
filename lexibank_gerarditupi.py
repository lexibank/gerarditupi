import attr
from pathlib import Path

from pylexibank import Concept, Language
from pylexibank.dataset import Dataset as BaseDataset
from pylexibank.util import progressbar, getEvoBibAsBibtex

from cldfbench import CLDFSpec
from csvw import Datatype
from pyclts import CLTS

import lingpy
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

        args.writer.add_sources()
        concepts = {}
        for concept in self.concepts:
            idx = '{0}_{1}'.format(concept['NUMBER'], slug(concept['ENGLISH']))
            args.writer.add_concept(
                    ID=idx,
                    Name=concept['ENGLISH'],
                    )
            concepts[concept['ENGLISH']] = idx
        languages = args.writer.add_languages(lookup_factory='Name')
        
        missing = set()
        for row, cog in zip(
                self.raw_dir.read_csv(
                    'Aligned_matrix_lexical.csv', delimiter=',', dicts=True),
                self.raw_dir.read_csv(
                    'Cognate matrix.csv', delimiter=',', dicts=True)):
            language = row[''].strip()
            for concept, concept_id in concepts.items():
                word = row[concept]
                if word.strip() and language.strip():
                    lexeme = args.writer.add_form_with_segments(
                            Language_ID=languages[language],
                            Parameter_ID=concept_id,
                            Value=row[concept],
                            Form=row[concept],
                            Segments=row[concept].split(),
                            Source='gerarditupi'
                            )
                    if concept in cog:
                        args.writer.add_cognate(
                            lexeme=lexeme,
                            Cognateset_ID='{0}-{1}'.format(slug(concept), cog[concept]),
                            Source='gerarditupi')
                    else:
                        missing.add(concept)
        for concept in missing:
            args.log.warn('Concept {0} could not be found'.format(concept))


