from collections import namedtuple

class LogLine:
    def __init__(self,zap):
        self.full = zap
        self.remote_addr = zap.partition(' -')[0]
        self.time_local = zap.partition('[')[2].partition(']')[0]
        self.request = zap.partition('] "')[2].partition('"')[0]
        self.status = zap.partition('" ')[2].partition(' ')[0]
                
metods = 'CONNECT DELETE GET HEAD OPTIONS POST PUT TRACE'.split()
ChekAd = ''
ChekTm = ''
buf = []
err = 0
f = open('test1.txt','r')
for line in f:
    h = LogLine(line)
    if h.remote_addr == ChekAd:
        if ChekTm == h.time_local:
            kolT += 1
            if kolT > 4:
                err += 1
        else:
            ChekTm = h.time_local
        if not (h.request.partition(' ')[0] in metods):
            err += 1
        if h.status[0] == '4' or h.status[0] == '5':
            kolR += 1
            if kolR > 3:
                err += 1      
        buf += line
    else:
        if err > 0:
            print(ChekAd,'\n',"".join(buf))
        ChekAd = h.remote_addr
        ChekTm = h.time_local
        kolT = 0
        kolR = 0
        buf = []
        err = 0
        if not (h.request.partition(' ')[0] in metods):
            err += 1
        buf += line
if err > 0:
        print(ChekAd,'\n',"".join(buf))
print(buf)
f.close()
