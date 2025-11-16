# Last updated: 11/15/2025, 6:24:37 PM
class Solution:
    def freqAlphabets(self, s: str) -> str:
        d={ '1':'a', '2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i',
           '10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o','16#':'p'
           ,'17#':'q','18#':'r','19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z','#':'' }
        a=""        
        c=0
        l=[]
        i=0
        while(i<=len(s)-3):
            if(s[i+2]=='#'):
                l.append(s[i:i+3])
                i=i+3
                c=c+3
            else:
                l.append(s[i])
                i=i+1
                c=c+1
        if(c!=len(s)):
            for x in s[len(s)-2:len(s)]:
                l.append(x)
        for x in l:
            a=a+d[x]
        return a
                
            