import re
index=open("index.txt","r").readlines()
for line in index:
    try:
        match =  re.match("((\d+\.)+\d*\s+.+\((Not\sScored|Scored)\))",line)
        if match:
            data =  match.group()
            #print data
            match1 = re.match("(((\d+\.)+)\d*)",data)
            print '"'+match1.group()+'",',
    except:
        pass
