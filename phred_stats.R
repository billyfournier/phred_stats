#setwd("/home/geno/dev/phred_stats")
# USAGE: R CMD BATCH phred_stats.R

read1 <- scan("out1.qual")
loess1 <- loess(read1~c(1:length(x)))
read1_threshold <- which(predict(loess1) < 25)[1]

read2 <- scan("out2.qual")
loess2 <- loess(read2~c(1:length(x)))
read2_threshold <- which(predict(loess2) < 25)[1]

plot(c(1:length(read1)),read1, type='l', ylab="Mean_PHRED", xlab="Pos #", col="red", main= "PHRED(mean) Curve")
lines(predict(loess1), col="blue")
abline(v = read1_threshold, col = "gray60")
legend(read1_threshold, 10, legend=c(read1_threshold), cex=0.5)


### The following block of code plots the output of read2. Comment out if not useing.
lines(c(1:length(read2)),read2, type='l', col="green")
lines(predict(loess2), col="orange")
abline(v = read2_threshold, col = "gray60")
legend(read2_threshold, 10, legend=c(read2_threshold),
       cex=0.5)


abline(h = 25, col = "black")
legend(1, 15, legend=c("Read1", "Read2"),
       col=c("blue", "orange"), lty=1, cex=0.8)


