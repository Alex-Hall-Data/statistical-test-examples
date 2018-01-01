#binomial test for coin. 70 flips performed with 45 heads. p=p(heads)
#null hypothesis is p=0.5
#alternative hypothesis p!=0.5

pp=binom.test(45,70,p=0.5,conf.level=0.9)
pp

#alternative hypothesis true - coin is biased. p value is 0.022 so the evidence isn't overwhelmingly strong
#90% confidence interval is between 54% and 74% (ie percentage bias). This is a big range so a bigger sample size is needed to ascetain the bias.

