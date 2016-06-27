#setwd("/home/geno/dev/phred_stats")

read1 <- scan("out1.qual")
loess1 <- loess(read1~c(1:length(x)))
read1_threshold <- which(predict(loess1) < 25)[1]

plot(c(1:length(myData)),read1, type='l', ylab="Mean_PHRED", xlab="Pos #", col="red", main= "PHRED(mean) Curve")
lines(predict(loess1), col="blue")
abline(v = read1_threshold, col = "gray60")
legend(read1_threshold, 10, legend=c(read1_threshold), cex=0.5)

#lines(a, type='l', col="green")
#lines(predict(read2_lo), col="orange")
#abline(v = read2_threshold, col = "gray60")
#legend(read2_threshold, 10, legend=c(read2_threshold),
#       cex=0.5)


#abline(h = 25, col = "black")
#legend(1, 15, legend=c("Read1", "Read2"),
#       col=c("blue", "orange"), lty=1, cex=0.8)


