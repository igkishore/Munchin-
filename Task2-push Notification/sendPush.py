import FCMmanager as fcm 


class PushNotifier :
    def comment(self,name,token):
        fcm.sendPush(name,"Commented on your post",token)
    def like(self,title,message,token):
        fcm.sendPush(name,"Liked your post",token)
    def reply(self,title,message,token):
        fcm.sendPush(name,"Replyed to your Post",token)
    def share(self,title,message,token):
        fcm.sendPush(name,"Shared  your post",token)
    def follow(self,title,message,token):
        fcm.sendPush(name,"Started following You",token)



    


