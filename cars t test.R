cars<-read.table("cars.txt",header=T)

attach(cars)

#t test
tt=t.test(MPG)
tt

##99% interval t test
tt99=t.test(MPG,conf.level=0.99)
tt99

#filter by American cars only
is.american=(Country=="U.S.")

#2 sample t test. tests whether american cars have higher MPG than others
twot=t.test(MPG~is.american)
twot

#get categories for two sample t test
names(twot)

#get 95% confidence interval.
twot$conf.int