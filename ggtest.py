import requests


def mid(s, l, r):
    l1 = s.find(l)+len(l)
    r1 = s[l1:].find(r)+l1
    return s[l1:r1]


r=requests.get("http://f.cili001.com/index/index?c=&k="+"西部世界")
for i in range(1,10):
    first=r.text.split("<ul class=\"link-list\">")[i]
    # print(first)
    mag=mid(first,'data-magnet="','"')
    name=mid(first,'<span class="name">','</span>')
    size=mid(first,'<span class="size">','</span>')
    time=mid(first,'<span class="time">','</span>')
    date=mid(first,'<p class="link-list-title">','</p>').strip()
    print("%s\n%s %s\n大小: %s\n%s"%(name,date,time,size,mag))