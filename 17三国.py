
def create(m):
    a = []
    for i in range(m):
       a.append(list(map(int, input().split())))
    return a

def juge(T,chengdu_soldiers,state):
    for i in state:
        chengdu_soldiers+=i[1]
        if chengdu_soldiers<0: 
            result.append(f"Case #{T}: No")
            return False
    result.append(f"Case #{T}: Yes")
    return True

result=[]
T = int(input())
for x in range(T):
    input()
    chengdu_soldiers = int(input())
    m_cao = int(input())
    cao_soldiers=create(m_cao)

    m_sun = int(input())
    sun_soliders=create(m_sun)
    state=[]
    for i in cao_soldiers:
        state.append([i[0]**2+i[1]**2,-i[2]])

    for i in sun_soliders:
        state.append([(i[0]**2+i[1]**2)*4,i[2]])


    state.sort(key= lambda state:state[0])
    for i in range(0,len(state)-1):
        if state[i][0]==state[i+1][0]:
            state[i+1][1]+=state[i][1]
            state[i][1]=0

    juge(x+1,chengdu_soldiers,state)

for i in result:
    print(i)