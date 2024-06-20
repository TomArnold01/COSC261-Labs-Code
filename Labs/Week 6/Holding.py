

import Testing_space

def testing():
    # A simple case to check that the function returns a set
    cfg = "S=done"
    generating = generating_nts(cfg)
    print(generating)
    print(type(generating) is set)
    print("1--------------------------------------------------------------------")
    
    # The CFG G1 above, in which all NTs are generating.
    cfg = """S=BA
    A=a|BA|BB
    B=b|AA"""
    print(sorted(generating_nts(cfg)) == ['A', 'B', 'S'])
    print("2--------------------------------------------------------------------")
   
    # A and C are not generating. Can you see why?
    cfg = """S=aAa|bBb
    A=aC|bAA
    B=b|aBB
    C=Ab|bA"""
    print(sorted(generating_nts(cfg)) == ['B', 'S'])
    print("3--------------------------------------------------------------------")

    # None of these are generating!
    cfg = """S=aAa|bBb
    A=aS|bAA
    B=bS|aBB"""
    print(generating_nts(cfg) == set())
    print("4--------------------------------------------------------------------")

    # A non-terminal does not have to be reachable to be generating
    cfg = "X=unreachable"
    print(sorted(generating_nts(cfg)) ==['X'])
    print("5--------------------------------------------------------------------")

    cfg = "A=0A1"
    print(sorted(generating_nts(cfg)) == [])
    print("6--------------------------------------------------------------------")

    cfg = """S=aSa|bSb|_
    A=aS|bAA
    B=bS|aBB"""
    print(sorted(generating_nts(cfg)) == ['A', 'B', 'S'])
    print("7--------------------------------------------------------------------")

    cfg = """S=aB|bA
    A=aS|bAA
    B=bS|aBB|_
    C=abC|SC"""

    print(sorted(generating_nts(cfg)) ==['A', 'B', 'S'])
    print("8--------------------------------------------------------------------")

    cfg = """S=NOPE
    A=aC
    B=bC
    C=abS|SC|_"""
    print(sorted(generating_nts(cfg)) == ['A', 'B', 'C'])
    print("9--------------------------------------------------------------------")

    cfg = """S=aB|bA|CC
    A=aS|bAA
    B=bS|aBB
    C=abS|SC|_|D
    D=DD
    E=B"""
    print(sorted(generating_nts(cfg)) ==['A', 'B', 'C', 'E', 'S'])
    print("10--------------------------------------------------------------------")

    # a CFG where some non-terminals have only an epsilon-production
    cfg = """S=X|Y
    W=_
    X=Z1|0Z|1Y|Y0
    Y=1|0|X
    Z=_"""
    print(sorted(generating_nts(cfg)) == ['S', 'W', 'X', 'Y', 'Z'])
    print("11--------------------------------------------------------------------")

    # a CFG where all non-terminals have only an epsilon-production
    cfg="""S=_
    T=_
    U=_
    V=_
    W=_"""
    print(sorted(generating_nts(cfg)) == ['S', 'T', 'U', 'V', 'W'])
    print("12--------------------------------------------------------------------")

    # a CFG with a long chain of unit-productions
    cfg="""S=T
    T=U
    U=V
    V=W
    W=X
    X=Y
    Y=Z
    Z=42"""
    print(sorted(generating_nts(cfg)) == ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    print("13--------------------------------------------------------------------")

    cfg = """S=SGR|NS|C|X|PCX|CN|XN|QNR|R|SC|N|RRT|RU|STR|XXV|NN|US|CU|XS|NC|SNM|AUC|SQX
    A=S|VVM|TDK|Q|K|IV|LV|PGI|VTQ|P|IVL|GD|TV|PG|MI|M|DDG|KGV|T|L
    B=DP|DIs|Dzg|Qt|hAGafG|Tukfo|MkfMxs|A|kh|nkT|Dv|_|GVPp|bxnGm|dzQo|Dpcad|fsh|PwVP|QlIfV|djA|TuxdId|DbvGM|rdml
    C=S|ULX|UR|U|XX|UPN|RQR|SS|UU|RKN|RKX|RU|RX|USG|NSA|NN|XS|VXU|NC|NU
    D=TGK|AAQ|S|IL|A|GIA|Q|K|I|PQD|LV|TTQ|G|P|IP|M|TG|AA|AKD|DV|KDA
    E=DT|eQtrQGr|xVdfD|wn|dge|ca|Gw|IPciLf|_|qIyP|lnLGI|oALnx|GQTn|r|wle|LpfMrp|bt|QzIrc|hI|D|LaLt
    F=lz|wT|A|_|y|qdj|gdm|eI|Pmsvm|Irp|cAlKI|TAaVu|Vcqxz|PI|VLszkyG|zGTQu|M|PAD|KmApv|zoqVIj|GuuKLaj
    G=S|AV|A|LDT|K|I|VQV|IA|PAT|IP|KL|M|QM|AQD|GQ|TQQ|PGT|T|DV|VLV|LT
    H=NS|SX|S|C|X|DCC|SVX|CN|SC|R|SDR|N|KUR|LRC|CX|CUP|RC|ANS|STR|XR|NC|XDC
    I=DPM|LA|S|GI|D|LP|IT|Q|K|GK|G|P|TV|PG|PL|KD|M|DG|KIL|IDP|T|QLD|V
    J=CIX|S|C|X|ANR|UGX|RPS|SRQ|CN|SC|R|U|N|CR|XR|XKC|CU|LCU|UGC|NU|UIC
    K=AAQ|S|LD|QG|QDV|MK|Q|I|AD|AP|KIM|KGP|L|LKL|IP|MTK|VI|T|KG|QAG|TMK|V|AIV
    L=noG|Qw|mpbLDT|AMA|Tmb|GDT|AbiwM|qf|kc|sTTlD|kqdo|ykc|KAT|rAdqa|M|AA|VI|ffKM|gLxKs|IKV|lti
    M=APT|KQ|VTG|S|MD|ML|LD|ADI|III|IV|K|I|ATV|G|P|AM|GD|GIL|GV|LII|V|LI
    N=SX|NX|C|S|SR|RSL|R|XX|KNC|UQX|NR|XCA|TSC|XMN|CX|CLS|UAR|CU|XU|CPC|NU
    O=SIX|VNX|S|SR|RAX|RVS|CC|RND|R|U|XAS|N|RKX|XC|RUM|XR|UIR|RTR|RIS|CUA|NCV|SN|UX|SRV|NU
    P=GMQ|LvGA|mLz|t|DLhj|Al|zIsww|LG|aA|itA|As|_|vcc|ngf|mgPh|Tm|KD|zQkKj|KV|tMQ|T|LL|IjoTI|TyMDol|yma
    Q=KK|VG|S|GG|TAK|VIG|MG|MMG|MV|TQ|VVL|TPM|KAP|G|TP|GVV|PI|M|VI|GL|QV|D
    R=S|C|UXM|X|TUN|UC|UR|SC|N|XUM|SS|NR|RC|QSU|XR|RR|NTC|SPC|CU|TNN|NUL|NDS|XS|LNX|TRS
    T=S|KVP|KI|LD|A|MLA|LVG|K|I|AP|LK|QL|IG|G|VV|P|PG|KP|VAL|L
    U=UMX|SX|S|URP|UN|RSD|NMN|N|SU|RSA|MSX|ACN|XC|RX|RU|UKN|AUS|NCG|MXX|NUD
    V=GPD|VIV|LA|S|DLL|KII|A|Q|K|LK|VPM|G|KA|IQL|PAT|TLL|DG|M|KV|T
    W=NDX|NS|VUR|S|C|QXU|R|U|KSX|SC|N|SUV|CX|RC|XNP|ULU|XUG|SN|SNM|SVU|SMX
    X=S|C|UN|RXD|XUD|KCR|VXR|R|U|N|SUK|NR|XC|RC|RU|RUM|NDN|XR|NCT|UNK
    Y=UMS|NX|RAC|S|C|UNG|SAX|XSD|UN|UR|SSL|R|U|CCK|N|UPU|CR|URI|UU|SLC|RUK|CU|IXN|KUS|CNG
    Z=MgjzPDo|LAndKu|ML|MMtI|IIG|brllD|PKK|jgkAy|IV|_|gePAx|Dr|dsa|zApwe|phvc|QoLauiL|Am|Gfu|xktPt|gs|VPu|l|Tw|V|LaVLb"""
    print(sorted(generating_nts(cfg)) == ['A', 'B', 'D', 'E', 'F', 'G', 'I', 'K', 'L', 'M', 'P', 'Q', 'T', 'V', 'Z'])
    print("14--------------------------------------------------------------------")
