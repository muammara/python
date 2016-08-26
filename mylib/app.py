from tracked import Tracked
myMobile = Tracked('12345')
hisMobile =Tracked('6789')
herMobile =Tracked('34567')


myMobile.Allow(hisMobile)
myMobile.Allow(herMobile)
myMobile.Allow(hisMobile)
myMobile.Allow(herMobile)

print (myMobile.AllowedTrackers)

myMobile.Revoke(herMobile)
print (myMobile.AllowedTrackers)
myMobile.Revoke(hisMobile)
print (myMobile.AllowedTrackers)