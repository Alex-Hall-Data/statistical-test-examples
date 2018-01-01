#dictionary of movie rankings

critics={'lisa rose':{'lady in the water':2.5,'snakes on a plane':3.5,'just my luck':3.0,'superman returns':3.5,'you me and dupree':2.5,'the night listener':3.0},
         'gene seymour':{'lady in the water':3.0,'snakes on a plane':3.5,'just my luck':1.5,'superman returns':5.0,'you me and dupree':3.5,'the night listener':3.0},
         'michael phillips':{'lady in the water':2.5,'snakes on a plane':3.0,'superman returns':3.5,'the night listener':4.0},
         'claudia puig':{'snakes on a plane':3.5,'just my luck':3.0,'superman returns':4.0,'you me and dupree':2.5,'the night listener':4.5},
         'mick lasalle':{'lady in the water':3.0,'snakes on a plane':4.0,'just my luck':2.0,'superman returns':3.0,'you me and dupree':2.0,'the night listener':3.0},
         'jack matthews':{'lady in the water':3.0,'snakes on a plane':4.0,'superman returns':5.0,'you me and dupree':3.5,'the night listener':3.0},
         'toby':{'snakes on a plane':4.5,'superman returns':4.0,'you me and dupree':1.0},
         'me':{'just my luck':3.0,'superman returns':5.0,'the night listener':3.5}

         }

#pearson rank
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

#EUCLIDIAN DISTANCE
#return distance based similarity for 2 individuals
def sim_distance(prefs,person1,person2):
    #get list of shared items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

        #if no items in common, return 0
    if len(si)==0: return 0

    #add up squares of differences
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])

    return 1/(1+sum_of_squares)

#to run this just type sim_distance(critics,'name1',name2')



#RANK CRITICS
#return best matches for person from the dictionary
def topmatches(prefs,person,n=5,similarity=sim_pearson):
    #apply chosen function to the dictionary
    scores=[(similarity(prefs,person,other),other) for other in prefs if other !=person]

    #sort list so highest scores appear at top
    scores.sort()
    scores.reverse()
    return scores[0:n]

# to run this just type topmatches(critics,'me',n=<number of critics to compare against>)



#gets recommendation by using weighted average
def getrecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simsums={}
    for other in prefs:
        #don't compare me to myself
        if other==person: continue
        sim=similarity(prefs,person,other)

        #ignore scores <=0
        if sim<=0: continue
        for item in prefs[other]:

            #only score movied I haven't seen yet
            if item not in prefs[person] or prefs[person][item]==0:
                #similarity*score
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                #sim of similarities
                simsums.setdefault(item,0)
                simsums[item]+=sim


        #create the normalised list
        rankings=[(total/simsums[item],item) for item, total in totals.items()]

        #return sorted list
        rankings.sort()
        rankings.reverse()
        return rankings


        
