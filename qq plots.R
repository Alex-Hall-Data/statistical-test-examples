random.normal=rnorm(100,mean=10,sd=3)
hist(random.normal)

#qqplot for normally distributed random data. Good fit expected
qqnorm(random.normal)
qqline(random.normal)

random.exp=rexp(100,rate=1)
hist(random.exp)

#qq plot for exponentially dstributed random data. poor fit expected
qqnorm(random.exp)
qqline(random.exp)