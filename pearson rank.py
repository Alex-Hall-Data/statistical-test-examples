from recommendations import critics
from math import sqrt

def sim_pearson(prefs,p1,p2):
    #get list of mutually rated items
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:si[item]=1

    #find number of elements
    n=len(si)

    #if there are no ratings in common return 0
    if n==0: return 0

    #add up all preferances
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    #sum the squares
    sum1sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2sq=sum([pow(prefs[p2][it],2) for it in si])

    #sum the products
    psum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    #calculate pearson score
    num=psum-(sum1*sum2/n)
    den=((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
    if den==0: return 0

    r=num/den

    return r
