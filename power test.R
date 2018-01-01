cars<-read.table("cars.txt",header=T)

attach(cars)

#t test
tt=t.test(MPG,mu=20)
tt

#power of t test
pp=power.t.test(n=38,delta=25-20,sd=6.5,type="one.sample")
pp

#power gives the probability of being correctly able to reject the null hypothesis. In this case, this gives us the chance of being able to correctly reject the null of the mean MPG being 20 if it is really 25.