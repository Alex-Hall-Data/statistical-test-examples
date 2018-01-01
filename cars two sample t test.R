#two sample t test to find whether American cars have lower MPG but only for 4 cylinder engines. pg 58
cars<-read.table("cars.txt",header=T)
attach(cars)

#filter by American cars only
is.american=(Country=="U.S.")

twot4=t.test(MPG[Cylinders==4]~is.american[Cylinders==4])
#2 sample t test on MPG for US cars with 4 cylinders. Null Hypothesis=no difference in MPG to other nationalities
twot4

#P value exceeds alpha (0.05) so null hypothesis is true


#t test to determine a measured MPG of 20 is representative from the above:

#null hypothesis is that population mean is equal to 20.

tt=t.test(MPG,mu=20)
tt
#p value is tiny so reject null hypothesis - MPG has changed