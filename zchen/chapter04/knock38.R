library(ggplot2)

data = read.delim('neko.tag', stringsAsFactors = F, header = F, na.strings = '')
data <- data[ !is.na( data$V2 ), 1]
data.small <- as.data.frame(table(data))
names(data.small) = c("word", 'freq')
data.small <- data.small[order(data.small$freq, decreasing = T),]
data.small$rank <- c(1:nrow(data.small))

# data = read.csv('freq.csv')
#
# # Slicing in data.frame
# # https://stats.idre.ucla.edu/r/modules/subsetting-data/
# data.small <- data[1:10,]
# reorder is a callback-like function, arranging factor levels according to some ordered variable
#
base <- ggplot( data.small, aes( log(freq) )) +
    geom_density( aes(y = log(..count..)) ) + # log(..density..)
    scale_x_continuous('logカウント') +
    scale_y_continuous('logカウントの密度') +
    theme( text = element_text(family = "HiraMinPro-W6"))

ggsave('knock38.png')
