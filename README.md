# MAP555 : Signal Processing

This is the latex sources for the lecture notes of MAP555 Signal Processing
Course from École Polytechnique. 

The document can be viewed in
[PDF](https://rflamary.github.io/map555-signal-processing/poly.pdf) or [HTML](https://rflamary.github.io/map555-signal-processing/).


**Warning** : This document is currently being written and should be considered
unfinished and full of mistakes and typos. It should not be used yet as a
pedagogical support for a course.


<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license"
href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.



## Features

+ A unique Latex source for the 
  [PDF](https://rflamary.github.io/map555-signal-processing/poly.pdf) and
  [HTML](https://rflamary.github.io/map555-signal-processing/) versions (using [lwarp](https://ctan.org/pkg/lwarp?lang=en) +
  adapted CSS).
+ Creative Commons CC BY-NC-SA 4.0 Licence (non commercial).
+ Automatic compilation of [PDF](https://rflamary.github.io/map555-signal-processing/poly.pdf) and
  [HTML](https://rflamary.github.io/map555-signal-processing/) when pushing to `main` branch with
  Github Actions.
+ All python script generating the figures will be available with MIT Licence.
+ Add HTML links to bibliography entries + link to scholar for references.
+ Alternative to [jupyterbooks](https://jupyterbook.org/intro.html) or
  [Bookdown](https://bookdown.org/) for people who prefer Latex (also better PDF with vector images).

## Compilation



The course can be compile using the Makefile. It follows 3 steps:
1. Compile  `poly.tex` to PDF with `latexmk`
2. Compile  to HTML with `lwarpmk`
2. Post process  HTML with `post_process.py` (remove ugly titles, add links to biblio).

It compiles on Ubuntu 20.04 (necessary for a recent version of latex package lwarp).


