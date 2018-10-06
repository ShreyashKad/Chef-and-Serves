T = int(raw_input())

for i in range(T):
    P1, P2, K = raw_input().split()
    P1, P2, K = float(P1), float(P2), float(K)
    if ((P1 + P2)/(K*2))%1 < 0.5:
        print "CHEF"
    else:
        print "COOK"
