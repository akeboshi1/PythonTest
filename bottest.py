from hiyobot import hackchat as hc

bot=hc.Bot("programming","awaBot","SomePassword") #在programming频道创建名为awaBot的机器人,密码为SomePassword
@bot.on(hc.Matcher(lambda x:x.get("text") == "Hello")) #当有人发送内容为"Hello"的内容时
async def event(session,data): #构造事件处理器
    #session为此次会话
    #data为json包内容
    session.bot.send("Hello there!") #发送 Hello there!
bot.run() #进入事件主循环