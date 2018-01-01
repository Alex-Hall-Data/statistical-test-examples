#paired t test for paired dataset (hind and foreleg length o a set of 10 deer)

deer=read.table("deer.txt",header=T)

deer.pairedt=t.test(deer$Foreleg,deer$Hindleg,paired=T)

deer.pairedt

#small P value so reject null hypothesis. So, leg lengths differ with 95% confidence interval of 1-5.5cm

plot(deer$Foreleg,deer$Hindleg)
lines(lowess(deer$Foreleg,deer$Hindleg))