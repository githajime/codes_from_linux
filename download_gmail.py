
#参考　https://toolmania.info/post-9795/


# -*- coding: utf-8 -*-
import imaplib
import email
from email.header import decode_header
import codecs
 
UserName=str(input("Username:"))
PassName=str(input("Password:"))
LabelName="none"
 
#-----------------------------------
gmail = imaplib.IMAP4_SSL("imap.gmail.com",'993')
gmail.login(UserName,PassName)
gmail.select(LabelName)
 
head,data = gmail.search(None, "(UNSEEN)")
 
i=0
#取得したメール一覧の処理
for num in data[0].split():
    try:
        h,d = gmail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(d[0][1])
 
        header = decode_header(msg.get('Subject'))
        msg_subject  = header[0][0]
        msg_encoding = header[0][1] or 'ISO-2022-JP'
 
        try:
            fr=str(msg_subject.decode(msg_encoding))
        except:
            fr='gmail'+str(i)
 
        print(fr)
 
        #ファイルとして使用できない文字を除外
        fr=fr.replace('$','＄')
        fr=fr.replace('.','．')
        fr=fr.replace('<','＜')
        fr=fr.replace('>','＞')
        fr=fr.replace('@','＠')
        fr=fr.replace('%','％')
        fr=fr.replace(':','：')
        fr=fr.replace('?','？')
        fr=fr.replace('|','｜')
        fr=fr.replace('"','')
        fr=fr.replace("'",'')
        fr=fr.replace(' ','_')
        fr=fr.replace('/','／')
        fr=fr.replace('*','＊')
        fr=fr.replace('+','＋')
        fr=fr.replace('-','ー')
        fr=fr.replace('\\','￥')
        fr=fr.replace('\r\n','')
        fr=fr.replace('\n','')
        f=codecs.open(fr+str(i+1)+".eml","w","utf-8")
        f.write(str(msg))
        f.close()
        i=i+1
    except:
        i=i+1
 
#終了処理
gmail.close()
gmail.logout()
 
print("メール読み込み完了")