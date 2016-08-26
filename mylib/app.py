from tracked import Tracked
myMobile = Tracked('12345')
hisMobile =Tracked('6789')
herMobile =Tracked('34567')


myMobile.AllowedTrackers.append(hisMobile)
myMobile.AllowedTrackers.append(herMobile)
print (myMobile.AllowedTrackers)