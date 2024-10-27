#Simple Try - except -finally
lt1 = [1,2,3,5,6]
pos = {1:'st',2:'nd',3:'rd'}

def meth(sv):
    i = lt1.index(sv)
    p = pos.get(i)
    if p == None: p = 'th'
    print(f'{sv} is in {i}{p} position')

while(True):
    try:
        sv = int(input('Enter Number:'))
        meth(sv)
        #print(i)
    except Exception as e:
        print('Err>', e)
    finally:
        r = input('Continue(y/n) ?')
        if not r.lower()=='y': break

