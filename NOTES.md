This is the dataset accompanying the publication by Gerardi and Reichert, titled "The Tupí-Guaraní Language Family:A Phylogenetic Classification", which appeared in Diachronica 38(2). 151--188. DOI: https://doi.org/10.1075/dia.18032.fer. 

When converting the original data to CLDF, we one problem in the mapping of a concept label in the lexical data file (called `Aligned_matrix_lexical.csv`, in the folder `raw`) and the cognate assignments (called `Cognate matrix.csv` also in `raw`). We have marked this case by adding error codes which are triggered when running the CLDFBench command, and currently, there are only a single item which do not have a counterpart in the lexical data file or in the cognate file.

```
$ cldfbench lexibank.makecldf gerarditupi
WARNING Concept CAIR could not be found
```

We could not resolve this case and will leave it for now, but we will update the data later, when we manage to find out what happened. The results of the analyses, however, should not have been influenced by this mismatch.
