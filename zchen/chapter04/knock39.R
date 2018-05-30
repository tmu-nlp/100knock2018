library(ggplot2)
library(ggrepel)

data = read.delim('neko.tag', stringsAsFactors = F, header = F, na.strings = '')
data <- data[ !is.na( data$V2 ), 1]
data.small <- as.data.frame(table(data))
names(data.small) = c("word", 'freq')
data.small <- data.small[order(data.small$freq, decreasing = T),]
data.small$rank <- c(1:nrow(data.small))
data.text <- subset(data.small, rank %in% c(1:20, 50, 100:110, 400:410, 600, 1000:1010, 1200:1210, 1800:1810, 5000:5010, 8000, -1))

# http://www.sthda.com/english/wiki/print.php?id=188
# coord:
# http://www.sthda.com/english/wiki/ggplot2-axis-scales-and-transformations
jit <- position_jitter(height = 0.1)
tb <- scales::trans_breaks("log10", function(x) 10^x)
lb <- scales::trans_format("log10", scales::math_format(10^.x))
base <- ggplot( data.small, aes( rank, freq )) +
    #geom_bin2d() +
    geom_hex() + geom_rug(position = jit) + geom_jitter(color = alpha('black', 1/10), position = jit) +
    # stat_density_2d(geom = "raster", aes(fill=..density..), n = 10, contour = FALSE) +
    geom_smooth(method = 'loess', se = T) +
    scale_x_log10('logランク', breaks = tb, labels = lb ) +
    scale_y_log10('logカウント', breaks = tb, labels = lb ) +
    scale_fill_gradientn(trans = 'log10', colours = rainbow(4), breaks = tb, labels = lb ) +
    geom_label_repel(family = "HiraMinPro-W6", data = data.text, mapping = aes(label = word, fill = rank), color = 'white') +
    ggtitle("Zipf's law") + # labs( xytitle )
    theme( text = element_text(family = "HiraMinPro-W6"))# + annotation_logticks()

ggsave('knock39.png')
