import re
import csv
tweet = [i for i in open("Dataset 20.txt").read().split('\n') if re.search(r'[\w]+',i)]

slang = ['adventuritter', 'AFAIK', 'attwaction', 'attwicted', 'B2BTOTY', 'b4', 'b/c', 'beetweet', 'BFN', 'bgd', 'BR', 'Bird-of-mouth', 'chk', 'cld', 'clk', 'CT', 'cre8', 'da', 'twitamin', 'deets', 'deja-tweet', 'detweet', 'DM', 'drive-thru tweet', 'drive-by tweet', 'drunktwittering', 'dweet', 'eavestweeting', 'egotwistical', 'EM/eml', 'EMA', 'emergatweet', 'F2F', 'FAV', 'FF', 'ICYMI', 'IRL', 'MM', 'mistweet', 'NTS', 'OH', 'PRT', 'retweet', 'TMB', 'TMI', 'twabbreviating', 'twacklist', 'twaddict', 'twaffic', 'twalking', 'twama', 'twamily', 'twamous', 'twebay', 'tweeple', 'tweet', 'tweetaholic', 'tweet chat', 'tweeter', 'tweetroduce', 'tweetsult', 'twegal advice', 'twettiquette', 'twewbie', 'tweekend', 'twenius', 'twendy', 'twis', 'twitosphere', 'twittcrastination', 'twitterati', 'twitter-ific', 'twitterage', 'twitterapps', 'twitterpated', 'twitterphoria', 'twitterfly', 'twittersona', 'twittworking', 'woz', 'wtv', 'ykyat', 'yoyo', 'ztwitt']

emoticons = ['(.V.)', 'O:-)', 'X-(', '~:0', ':-D', '(*v*)', ':-#', '</3', '<\3', '=^.^=', '*<:o)', 'O.o', 'B-)', ':_(', ":'(", 'T.T', '\:D/', '*-*', ':o3', '#-o', ':*)', '//_^', '>:)', '<><', ':(', ':-(', '=P', ':-P', '8-)', '$_$', ':->', '=)', ':-)', ':)', '<3', '{}', ':-|', 'X-p', ':-)*', ':-*', ':*', '(-}{-)', 'XD', '=D', ')-:', '(-:', '<3', '=/', ':-)(-:', '<:3)~', '~,~', ':-B', '^_^', '<l:0', ':-/', '=8)', '@~)~~~~', '=(', ':S', ':-@', '=O', ':-o', ':-Q', ':>', ':P', ':o', ':-J', ':-&', '=-O', ':-\\', ':/', ':-E', '=D', ';-)', ';)', '|-O']

o = open('Output.csv',"wb")
writer = csv.writer(o, delimiter=',')
data = [['HashTag','RT','URL','ID','SLANGS','EMOTICONS']]
for i in tweet:
    a = [0,0,0,0,0,0]
    a[0] = len(re.findall(r'#\w+\.*\s',i)) # HASHTAG
    a[1] = len(re.findall(r'^RT\s',i)) # RT
    a[2] = len(re.findall(r'[a-zA-z]+:\/\/\w+\.',i)) # URL
    a[3] = len(re.findall(r'@+\w+',i)) # ID
    for j in slang: #SLANGS
        a[4] += len(re.findall(j,i))
    for j in emoticons: #EMOTICONS
        a[5] += len(re.findall(re.escape(j),i))
    data.append(a)
for line in data:
    writer.writerow(line)


