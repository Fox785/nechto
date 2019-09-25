import time as t
import requests as r
import datetime
import random as ran


TOKEN='125648327cf0f2c016559044fe7257a85c6f5d5dcd88501d590c08eb46fad3da756f4254b226bb8af5db4'



def req(method,kwargs):
    ans = { 'access_token': TOKEN,'v':'5.101'}
    for key,value in kwargs.items():
        ans.update({key: value})
    print(ans)
    ans = r.get(f'https://api.vk.com/method/{method}', params=ans).json()
    try:
        return ans['response']
    except KeyError:
        return ans

def mess(text):
    print(req('messages.send',{'peer_id':-91050183,'message':text,'random_id':0}))

while True:
    server=req('messages.getHistory',{'peer_id':-91050183,'count':1}) 
    sms=server['items'][0]['text']  
    print(sms)
    if '1. Мне нравится.' in sms:
        badwords=['блять','пиздец','ебать',',беседа','беседу','хуйло','член','хуй','долбоеб']
        if any(words in sms for words in badwords):
            mess(3)
        else:
            if ran.choice([1,2])==1:
                mess(2) 
                t.sleep(2) 
                mess('Буду рада видеть тебя в беседе') 
            else:
                mess(3) 
    elif '1. Продолжить просмотр анкет'in sms:
        mess(1)
    elif '1. Оценить еще кого-то.'in sms or 'Есть взаимная симпатия!'in sms:
        p=req('messages.getHistory',{'peer_id':-91050183,'count':1})
        sms=p['items'][0]['text']
        o=sms.split('http://vk.com/id')[1].split()[0] 
        req('friends.add',{'user_id':o,'text':'Я по поводу беседы'})
        mess(1)
    # elif 'Есть взаимная симпатия!'in sms:
    #     n=req('messages.getHistory',{'peer_id':-91050183,'count':1})
    #     sms=n['items'][0]['text']
    #     k=sms.split('http://vk.com/id')[1]
    #     req('friends.add',{'user_id':o,'text':'Я по поводу беседы'})
    #     mess(1)    
    elif 'Кто-то тобой заинтересовался! Заканчивай с вопросом выше и посмотрим кто там' in sms:
        mess(3) 
    elif 'В твоей анкете свосем нет текста, если ты напишешь немного о себе и кого ищешь, мы сможем лучше подобрать тебе пару.' in sms:
        mess(1)   
    elif 'Елена, пришли мне свое местоположение и увидишь кто находится рядом' in sms:
        mess(1) 
    elif 'Нашли кое-кого для тебя ;) Заканчивай с вопросом выше и увидишь кто это' in sms:
        mess(3)  
    elif 'Твоя анкета может собирать больше лайков.' in sms:
        mess(2) 
    elif 'Кому-то понравилась твоя анкета! Заканчивай с вопросом выше и посмотрим кто это' in sms:
        mess(3)
    elif '1. Мне нравится.2. Не очень.' in sms:
        ran.choice([1,2])
    elif 'Отлично! Надеюсь хорошо проведете время ;)' in sms:
        mess(1)
    elif 'Нет такого варианта ответа, напиши одну цифру' in sms:
        mess(1)    
    elif 'Напиши сообщение для этого пользователя' in sms:
        mess('Буду рада видеть тебя в беседе')   
    elif 'Нашел кое-кого для тебя, смотри:':
        if ran.choice([1,2])==1:
            mess(2)
            t.sleep(2)
            mess('Буду рада видеть тебя в беседе')
        else:
            mess(3)    
    t.sleep(10)
    n=r.get('https://api.vk.com/method/friends.get',params={'access_token': TOKEN,'v':'5.101',}).json() 
    for i in n['response']['items']: 
        req('messages.addChatUser',{'chat_id':17,'user_id':i}) 
        print(req('messages.addChatUser',{'chat_id':17,'user_id':i}))        
        req('friends.delete',{'user_id':i})     
