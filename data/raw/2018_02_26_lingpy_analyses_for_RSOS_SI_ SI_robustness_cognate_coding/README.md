# Analyses and Data Accompanying the Paper "A Bayesian phylogenetic study of the Dravidian language family"

This folder contains the analyses regarding testing of robustness of cognate coding described in the following paper:

Kolipakam, Vishnupriya, Jordan, Fiona M., Dunn, Michael, Greenhill, Simon J., Bouckaert, Remco, Gray, Russell D. & Verkerk, Annemarie. (2018). A Bayesian phylogenetic study of the Dravidian language family. Royal Society Open Science. 


# Methodology as Described in the Paper

> To provide a further check on cognate coding, we used new methods designed to aid robustness of linguistic inferences. Sound sequences in the original data were adjusted with help of orthography profiles (Moran and Cysouw 2017, "segments" package) that provide a simple means to segment and correct phonetic transcriptions. To increase the future comparability of the data, all concepts were linked to the Concepticon (List et al. 2016). An automatic cognate detection analysis of the data was performed with LingPy (version 2.5.1, List and Forkel 2016) using the LexStat-Infomap algorithm (List et al. 2017). The standard threshold of 0.55 (List et al. 2017: 8) yielded precision values of 0.90 and an overall F-Score of 0.84 (using B-Cubed evaluation scores), giving 90% agreement between our cognate coding and the automatic cognate detection algorithm. The cognate-coded dataset is made available on GitHub and published on Zenodo.

* Moran, S. & Cysouw, M. 2017. The Unicode Cookbook for Linguists: Managing writing systems using orthography profiles. Zenodo. http://doi.org/10.5281/zenodo.290662.

* List, J.-M., Cysouw, M. & Forkel, R. 2016. Concepticon. A resource for the linking of concept lists. In N. Calzolari, K. Choukri, T. Declerck, S. Goggi, M. Grobelnik, B. Maegaard, J. Mariani, H. Mazo, A. Moreno, J. Odijk, & S. Piperidis (eds.), Proceedings of the Tenth International Conference on Language Resources and Evaluation, 2393-2400. European Language Resources Association (ELRA).

* List, J.-M. & Forkel, R. 2016. LingPy: A Python library for historical linguistics. Version 2.5. URL: http://lingpy.org, With contributions by S. Moran, P. Bouda, J. Dellert, T. Rama, F. Nagel, and S. Greenhill. Jena: Max Planck Institute for the Science of Human History. (https://zenodo.org/badge/latestdoi/5137/lingpy/lingpy.)

* List, J.-M., Greenhill, S. J. & Gray, R. D. 2017. The potential of automatic word comparison for historical linguistics. Plos One 12, 1-18.

# Requirements

* python3 (https://www.python.org/download/releases/3.0/)
* lingpy (http://lingpy.org, Version 2.6)
* segments (https://github.com/cldf/segments)
* igraph (http://igraph.org/python/)

# Data

* DravLex-2017-04-23.csv  - the cognate-coded dataset used in the paper;

This is the main data file. Additionally, the file:

* profile.tsv

provides the orthography profile to refine the data.

# Code

To run the robustness test, just open a terminal in the folder (or cd into the folder from the terminal) and type:

```shell
$ python process.py thresholds
```

This will create output on the commandline and additional datafiles. Please
look in the Python script for more options that the code offers. If you have
questions, feel free to turn to the team which programs lingpy at
info@lingpy.org.
