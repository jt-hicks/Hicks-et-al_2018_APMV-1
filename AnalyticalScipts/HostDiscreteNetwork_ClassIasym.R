#install.packages("devtools")
#devtools::install_github("mattflor/chorddiag")
library(chorddiag)
m <- matrix(c(0, 0, 0, 0, 0.938268915, 0.7366923, 0, 0,
              0, 0, 0, 0, 0.169011935, 0, 0.270503025, 0,
              0, 0, 0, 0, 0, 0.140140591, 1.964087015, 0,
              0, 0, 0, 0, 0, 0, 0, 3,
              0.938268915, 0.169011935, 0, 0, 0, 0, 0, 0,
              0.7366923, 0, 0.140140591, 0, 0, 0, 0, 0,
              0, 0.270503025, 1.964087015, 0, 0, 0, 0, 0,
              0, 0, 0, 3, 0, 0, 0, 0),
            byrow = TRUE,
            nrow = 8, ncol = 8)
categories <- c("Source_ANS", "Source_CHA", "Source_CHI", "Dummy", "Sink_CHI", "Sink_CHA", "Sink_ANS", "Dummy")
dimnames(m) <- list(source = categories,
                    sink = categories)
print(m)

pander::pandoc.table(m, style = "rmarkdown")
#groupColors <- c("#083E77", "#8B161C", "#DF7C00", "#083E77", "#8B161C", "#DF7C00", "#083E77", "#8B161C", "#DF7C00")
chorddiag(m, groupColors = "#083E77", showTicks = FALSE, chordedgeColor = NULL)
#help(package="chorddiag")
