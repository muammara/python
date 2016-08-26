class Tracked:
# This class defines the tracked object, and allowed tracking objects

    def __init__(self,mobile):
        self.mobile=mobile
        self.EnableTracking =False
        self.AllowedTrackers =[]
    def __repr__(self):
        return self.mobile

    def Allow(self,track):
        if track not in self.AllowedTrackers:
            self.AllowedTrackers.append(track)
    def Revoke(self,track):
        if track in self.AllowedTrackers:
            self.AllowedTrackers.remove(track)



