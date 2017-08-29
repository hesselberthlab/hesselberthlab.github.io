+++
title = "Software"
author = "Jay Hesselberth"
date = '2017-08-18'
slug = "software"
tags = ["software"]
image_preview = "/hex/genomics-hex.svg"

summary = "Tools to enable analysis and visualization of large-scale biological data sets."

[header]
  image = "hex/genomics-hex.svg"
+++

# valr <img src="/img/hex/valr-logo.png" style="float: right;" />

**`valr` provides tools to read and manipulate genome intervals and signals**, similar to the [`BEDtools`](http://bedtools.readthedocs.org/en/latest/) suite. [`valr`](http://rnabioco.github.io/valr/) enables analysis in the R/RStudio environment, leveraging modern R tools in the [`tidyverse`](tidyverse.org) for a terse, expressive syntax. Compute-intensive algorithms are implemented in [`Rcpp`](http://www.rcpp.org/)/C++, and many methods take advantage of the speed and grouping capability provided by [`dplyr`](https://dplyr.tidyverse.org).
