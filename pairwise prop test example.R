
#group 1 successes
x1 <- 6085
#group 1 counts
n1 <- 13353



#group 2 successes
x2 <- 6566
#group 2 counts
n2 <- 14213

pairwise.prop.test(x=c(x1,x2) , n=c(n1,n2))