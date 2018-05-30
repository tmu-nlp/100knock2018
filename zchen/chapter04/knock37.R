library(ggplot2)
# exec with: Rscript *.R

# too many to plot, unable to sort and trunc in geom_bar
# not this kind of trunc: (high and low)
# https://stackoverflow.com/questions/20235321/truncate-highest-bar-in-ggplot?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# neither this: (wrap text)
# https://stackoverflow.com/questions/41568411/how-to-maintain-size-of-ggplot-with-long-labels?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# this is close to the solution:
# https://stackoverflow.com/questions/14771022/ggplot2-geom-bar-plot-where-count-greater-than-x/14771213#14771213da
data = read.delim('neko.tag', stringsAsFactors = F, header = F, na.strings = '')
data <- data[ !is.na( data$V2 ), 1]
data.small <- as.data.frame(table(data))
# data.small <- subset(data.small, Freq > 3000) # which nrow/length for df/c
names(data.small) = c("word", 'freq')
data.small <- data.small[order(data.small$freq, decreasing = T)[1:20],]
data.small$rank <- c(1:20)

# data = read.csv('freq.csv')
#
# # Slicing in data.frame
# # https://stats.idre.ucla.edu/r/modules/subsetting-data/
# data.small <- data[1:10,]
# reorder is a callback-like function, arranging factor levels according to some ordered variable
#
base <- ggplot( data.small, aes( reorder( word, -freq ), freq, fill = word, label = word)) +
    geom_col( show.legend = F ) +
    # geom_bar( stat = "identity" ,show.legend = F ) +
    # guides( fill = FALSE )  + # specially for fill, or all legend in theme
    # coord_flip() +
    # scale_x_reverse() +
    # labs( x = '単語', y = 'カウント') +
    scale_x_discrete('単語', breaks=NULL) + # limits, name/labels
    scale_y_continuous('カウント', breaks=NULL) +
    geom_text(family = "HiraMaruProN-W4", aes(y = freq + 200, label = freq, color = word)) + #, show.legend = F) +
    geom_text(family = "HiraMaruProN-W4", aes(y = - 200, label = rank)) + #, show.legend = F) +
    geom_text(family = "HiraMinPro-W6", aes(y = 200, label = word), color = 'white') + #, show.legend = F) +
    theme(legend.position="none") +
    theme( text = element_text(family = "HiraMinPro-W6")) # mystery

# navi in Finder with Cmd+Shf+G
ggsave('knock37.png', plot = base, width = 10, height = 5)
