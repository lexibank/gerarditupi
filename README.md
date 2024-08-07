# CLDF dataset derived from Gerardi and Reichert's "The Tupí-Guaraní Language Family: A Phylogenetic Classification" from 2021

[![CLDF validation](https://github.com/lexibank/gerarditupi/workflows/CLDF-validation/badge.svg)](https://github.com/lexibank/gerarditupi/actions?query=workflow%3ACLDF-validation)

## How to cite

If you use these data please cite
- the original source
  > Ferraz Gerardi, Fabrício and Reichert, Stanislav (2021) The Tupí-Guaraní Language Family: A Phylogenetic Classification. Diachronica 38(2). 151--188. DOI: https://doi.org/10.1075/dia.18032.fer.
- the derived dataset using the DOI of the [particular released version](../../releases/) you were using

## Description


This dataset is licensed under a CC-BY-4.0 license


Conceptlists in Concepticon:
- [Gerardi-2021-244](https://concepticon.clld.org/contributions/Gerardi-2021-244)
## Notes

This is the dataset accompanying the publication by Gerardi and Reichert, titled "The Tupí-Guaraní Language Family:A Phylogenetic Classification", which appeared in Diachronica 38(2). 151--188. DOI: https://doi.org/10.1075/dia.18032.fer. 

When converting the original data to CLDF, we one problem in the mapping of a concept label in the lexical data file (called `Aligned_matrix_lexical.csv`, in the folder `raw`) and the cognate assignments (called `Cognate matrix.csv` also in `raw`). We have marked this case by adding error codes which are triggered when running the CLDFBench command, and currently, there are only a single item which do not have a counterpart in the lexical data file or in the cognate file.

```
$ cldfbench lexibank.makecldf gerarditupi
WARNING Concept CAIR could not be found
```

We could not resolve this case and will leave it for now, but we will update the data later, when we manage to find out what happened. The results of the analyses, however, should not have been influenced by this mismatch.



## Statistics


[![CLDF validation](https://github.com/lexibank/gerarditupi/workflows/CLDF-validation/badge.svg)](https://github.com/lexibank/gerarditupi/actions?query=workflow%3ACLDF-validation)
![Glottolog: 98%](https://img.shields.io/badge/Glottolog-98%25-green.svg "Glottolog: 98%")
![Concepticon: 100%](https://img.shields.io/badge/Concepticon-100%25-brightgreen.svg "Concepticon: 100%")
![Source: 100%](https://img.shields.io/badge/Source-100%25-brightgreen.svg "Source: 100%")
![BIPA: 100%](https://img.shields.io/badge/BIPA-100%25-brightgreen.svg "BIPA: 100%")
![CLTS SoundClass: 100%](https://img.shields.io/badge/CLTS%20SoundClass-100%25-brightgreen.svg "CLTS SoundClass: 100%")

- **Varieties:** 38 (linked to 37 different Glottocodes)
- **Concepts:** 244 (linked to 242 different Concepticon concept sets)
- **Lexemes:** 7,621
- **Sources:** 74
- **Synonymy:** 1.00
- **Cognacy:** 7,590 cognates in 1,051 cognate sets (494 singletons)
- **Cognate Diversity:** 0.11
- **Invalid lexemes:** 0
- **Tokens:** 33,630
- **Segments:** 110 (0 BIPA errors, 0 CLTS sound class errors, 110 CLTS modified)
- **Inventory size (avg):** 35.97

# Contributors

Name | GitHub user | Description | Role
--- | --- | --- | ---
Ferraz Gerardi, F. | @LanguageStructure | Data Collector | Author
Reichert, S. | | Data Collector | Author
Johann-Mattis List | @lingulist | CLDF conversion | Editor
Tiago Tresoldi | @tresoldi | Minor curation, concept mapping refinement | Other




## CLDF Datasets

The following CLDF datasets are available in [cldf](cldf):

- CLDF [Wordlist](https://github.com/cldf/cldf/tree/master/modules/Wordlist) at [cldf/cldf-metadata.json](cldf/cldf-metadata.json)