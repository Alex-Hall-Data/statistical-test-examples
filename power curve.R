#sample to compute power of any true mean
mypower=function(true.mean){
  pp=power.t.test(n=38,delta=true.mean-20,sd=6.5,type="one.sample")
  pp$power
}
  

#vector of range of true means to be evaluated
means=seq(from=20,to=25,by=0.5)

#apply mypower function to vector of means
powers=sapply(means,mypower)

#produce table of means and respective powers
cbind(means,powers)

#plot power curve. Gives chance of correctly rejecting null hypothesis for range of true means for given sample size
plot(means,powers)
lines(spline(means,powers))
abline(h=1,lty=2)
grid(col="black")