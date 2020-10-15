This is the dataset accompanying the publication by Gerardi and Reichert, titled "The Tupí-Guaraní Language Family:A Phylogenetic Classification", which will appear in Diachronica. 

When converting the original data to CLDF, we found some problems in the mapping of concept labels in the lexical data file (called `Aligned_matrix_lexical.csv`, in the folder `raw`) and the cognate assignments (called `Cognate matrix.csv` also in `raw`). We have marked these cases by adding error codes which are triggered when running the CLDFBench command, and currently, there are five items which either do not have a counterpart in the lexical data file or in the cognate file.

```
$ cldfbench lexibank.makecldf gerarditupi
WARNING Concept CAIR could not be found
WARNING Concept LAY missing
WARNING Concept FALL missing
WARNING Concept HEAT_UP/WARM_UP missing
WARNING Concept CHEST missing
```

We could not resolve these cases and will leave them for now, but we will update the data later, when we manage to find out what happened. The results of the analyses, however, should not have been influenced by these mismatches.
