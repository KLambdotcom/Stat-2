from math import sqrt

def r(v, d=3):
    try:
        fmt = "%." + str(d) + "f"
        return fmt % float(v)
    except:
        return str(v)

def get_list(name):
    print("Donnees " + name)
    try:
        txt = input("? ")
        txt = txt.replace(',', ' ')
        return [float(x) for x in txt.split()]
    except:
        return []

def mean(L):
    if not L: return 0
    return sum(L)/len(L)

def variance(L):
    if len(L) < 2: return 0
    m = mean(L)
    return sum([(x-m)**2 for x in L])/(len(L)-1)

def pause():
    print("-" * 15)
    input("OK >")

# --- GENERATEUR D'HYPOTHESES ---
def hyp(h0, h1):
    print("\n--- 1. HYPOTHESES ---")
    print("H0: " + h0)
    print("H1: " + h1)
    input("Recopier puis Entree >")

# --- ASSISTANT DE REDACTION ---
def concl(val_obs, stat_name, ddl_str, h0):
    print("\n- CONCLUSION -")
    print("H0:", h0)
    try:
        txt = input("Seuil table ("+stat_name+") ? ")
        txt = txt.replace(',', '.')
        s = float(txt)
        v_abs = abs(val_obs)

        print("\n--- A ECRIRE SUR COPIE ---")
        print(stat_name + " obs(" + ddl_str + ") = " + r(v_abs))

        if v_abs >= s:
            print(r(v_abs) + " >= " + r(s) + " (Seuil)")
            print("=> On REJETTE H0")
            print("=> Effet SIGNIFICATIF")
        else:
            print(r(v_abs) + " < " + r(s) + " (Seuil)")
            print("=> On CONSERVE H0")
            print("=> NON Significatif")
    except:
        print("Erreur de seuil")
    pause()

def concl_a2(nom, F_obs, ddl1, ddl2):
    print("\n- Effet", nom, "-")
    try:
        txt = input("Seuil F("+str(ddl1)+","+str(ddl2)+")? ")
        s = float(txt.replace(',', '.'))
        print("\n--- A ECRIRE ---")
        print("F(" + str(ddl1) + "," + str(ddl2) + ") = " + r(F_obs))
        if F_obs >= s:
            print(r(F_obs) + " >= " + r(s))
            print("=> REJET H0 (Signif)")
        else:
            print(r(F_obs) + " < " + r(s))
            print("=> GARDE H0 (Non Signif)")
    except:
        pass

# --- AIDE THEORIQUE ---
def theorie():
    while True:
        print("\n"*3)
        print("--- AIDE & THEORIE ---")
        print("1. Choix du Test")
        print("2. Cond. Application")
        print("3. Tests R (p-value)")
        print("4. Residus")
        print("0. Retour")
        c = input("Choix? ")

        if c == "1":
            print("\n- CHOIX DU TEST -")
            print("1 Var Quanti + 1 Quali:")
            print(" 2 grp Indep -> T-Indep")
            print(" 2 grp Lies  -> T-Pair")
            print(" >2 groupes  -> ANOVA 1")
            print("1 Var Quanti + 2 Quali:")
            print(" -> ANOVA 2")
            print("2 Variables Quanti:")
            print(" -> Reg / Correlation")
            print("Var(s) Quali (Effectifs):")
            print(" -> Chi-2")
            pause()
        elif c == "2":
            print("\n- COND. APPLICATION -")
            print("Pour Student & ANOVA:")
            print("1. Independance (EAS)")
            print("2. Normalite")
            print(" (Chaque grp ou Residus)")
            print("3. Homoscedasticite")
            print(" (Variances egales)")
            print("---")
            print("Pour Chi-2:")
            print("Effectifs Theo >= 5")
            pause()
        elif c == "3":
            print("\n- TESTS SOUS R -")
            print("Regle p-value (alpha=5%):")
            print(" p < 0.05 => REJET H0")
            print(" p >= 0.05 => GARDE H0")
            print("---")
            print("SHAPIRO (Normalite)")
            print("H0: Loi Normale")
            print("BARTLETT (Variances)")
            print("H0: Homoscedasticite")
            print("(On espere p>=0.05 !)")
            pause()
        elif c == "4":
            print("\n- RESIDUS -")
            print("Definition:")
            print("Ecart entre val. obs.")
            print("et moyenne du groupe.")
            print("Formule:")
            print("e_ij = X_ij - Moy_i")
            print("---")
            print("Propriete absolue:")
            print("Somme(Residus) = 0")
            pause()
        elif c == "0":
            break

# --- TESTS STATISTIQUES ---
def stat_desc():
    L = get_list("X")
    if len(L)<2: return
    n = len(L)
    m = mean(L)
    v = variance(L)
    s = sqrt(v)
    sem = s/sqrt(n)
    print("- DESC -")
    print("n=", n)
    print("Moy=", r(m))
    print("Var=", r(v))
    print("EcT=", r(s))
    print("ErrS=", r(sem))
    pause()

def t_indep():
    L1 = get_list("G1")
    L2 = get_list("G2")
    if len(L1)<2 or len(L2)<2: return

    # Hypotheses formelles
    hyp("mu_1 = mu_2 (Moy. identiques)", "mu_1 != mu_2 (Moy. diff.)")

    n1, n2 = len(L1), len(L2)
    m1, m2 = mean(L1), mean(L2)
    v1, v2 = variance(L1), variance(L2)
    vp = ((n1-1)*v1 + (n2-1)*v2)/(n1+n2-2)
    se = sqrt(vp*(1/n1+1/n2))
    t = (m1-m2)/se
    ddl = n1+n2-2
    print("- 2. RESULTATS T INDEP -")
    print("m1=", r(m1), " m2=", r(m2))
    print("v1=", r(v1), " v2=", r(v2))
    print("Vp=", r(vp))
    print("---")
    print("t_obs=", r(t))
    print("ddl=", ddl)
    concl(t, "t", str(ddl), "mu_1 = mu_2")

def t_pair():
    L1 = get_list("Avt")
    L2 = get_list("Apr")
    if len(L1)!=len(L2) or len(L1)<2: return

    hyp("mu_d = 0 (Pas de diff.)", "mu_d != 0 (Difference)")

    D = [L1[i]-L2[i] for i in range(len(L1))]
    n = len(D)
    md = mean(D)
    vd = variance(D)
    sd = sqrt(vd)
    t = md/(sd/sqrt(n))
    ddl = n-1
    print("- 2. RESULTATS T PAIR -")
    print("md=", r(md))
    print("vd=", r(vd))
    print("sd=", r(sd))
    print("---")
    print("t_obs=", r(t))
    print("ddl=", ddl)
    concl(t, "t", str(ddl), "mu_d = 0")

def anova_1():
    print("Nb Groupes? ")
    try: k = int(input("? "))
    except: return
    grps, all_d = [], []
    for i in range(k):
        g = get_list("G"+str(i+1))
        grps.append(g)
        all_d += g
    N = len(all_d)
    if N==0: return

    # Hypotheses formelles pour ANOVA 1
    hyp("mu_1 = mu_2 = ... = mu_k", "Au moins 1 moy. differe")

    gm = mean(all_d)
    st = sum([(x-gm)**2 for x in all_d])
    sf = 0
    m_list = []
    for g in grps:
        if g:
            mg = mean(g)
            m_list.append(mg)
            sf += len(g)*(mg-gm)**2
    sr = st - sf

    df_t = N - 1
    df_f, df_r = k-1, N-k
    if df_f*df_r == 0: return

    cm_t = st/df_t if df_t>0 else 0
    cm_f = sf/df_f
    cm_r = sr/df_r
    F = cm_f/cm_r

    print("- 2. RESULTATS ANOVA 1 -")
    print("MoyG=", r(gm))
    print("MGrp=", ", ".join([r(x) for x in m_list]))
    print("SCT=", r(st), " CMT=", r(cm_t))
    print("SCF=", r(sf), " CMF=", r(cm_f))
    print("SCR=", r(sr), " CMR=", r(cm_r))
    print("---")
    print("F_obs=", r(F))
    print("ddl(F,R)=", df_f, ",", df_r)
    concl(F, "F", str(df_f)+";"+str(df_r), "Moy. identiques")

def anova_2():
    print("Niv. Fact. A ?")
    try: a = int(input("? "))
    except: return
    print("Niv. Fact. B ?")
    try: b = int(input("? "))
    except: return
    print("Nb repet (n) ?")
    try: n = int(input("? "))
    except: return

    cells = {}
    all_d = []
    for i in range(a):
        for j in range(b):
            vals = get_list("A"+str(i+1)+" B"+str(j+1))
            if len(vals) != n: return
            cells[(i,j)] = vals
            all_d += vals

    # Hypotheses formelles pour Anova 2
    print("\n--- 1. HYPOTHESES H0 ---")
    print("H0(A): mu_A1 = mu_A2 = ... = mu_Aa")
    print("H0(B): mu_B1 = mu_B2 = ... = mu_Bb")
    if n > 1:
        print("H0(AB): Pas d'interaction")
    print("H1: Au moins 1 moyenne differe")
    input("Recopier puis Entree >")

    gm = mean(all_d)

    mean_A = []
    for i in range(a):
        s = 0
        for j in range(b): s += sum(cells[(i,j)])
        mean_A.append(s/(b*n))

    mean_B = []
    for j in range(b):
        s = 0
        for i in range(a): s += sum(cells[(i,j)])
        mean_B.append(s/(a*n))

    sce_t = sum([(x-gm)**2 for x in all_d])
    sce_a = n * b * sum([(mA-gm)**2 for mA in mean_A])
    sce_b = n * a * sum([(mB-gm)**2 for mB in mean_B])

    df_t = (a * b * n) - 1
    df_a, df_b = a-1, b-1

    if n > 1:
        sce_sub = 0
        for i in range(a):
            for j in range(b):
                cm = mean(cells[(i,j)])
                sce_sub += n * (cm-gm)**2
        sce_ab = sce_sub - sce_a - sce_b
        sce_r = sce_t - sce_sub
        df_ab = df_a * df_b
        df_r = a * b * (n-1)
        ms_ab = sce_ab/df_ab if df_ab>0 else 0
    else:
        sce_ab, df_ab, ms_ab = 0, 0, 0
        sce_r = sce_t - sce_a - sce_b
        df_r = df_a * df_b

    if df_r == 0: return

    ms_t = sce_t/df_t if df_t>0 else 0
    ms_a = sce_a/df_a if df_a>0 else 0
    ms_b = sce_b/df_b if df_b>0 else 0
    ms_r = sce_r/df_r

    F_a = ms_a/ms_r
    F_b = ms_b/ms_r
    F_ab = ms_ab/ms_r if df_ab>0 else 0

    print("\n- 2. RESULTATS : P1 -")
    print("MoyG=", r(gm))
    print("MA=", ", ".join([r(x) for x in mean_A]))
    print("MB=", ", ".join([r(x) for x in mean_B]))
    input("Suite >")

    print("\n- P2: SC & ddl -")
    print("SCA=", r(sce_a), " ddl=", df_a)
    print("SCB=", r(sce_b), " ddl=", df_b)
    if n > 1: print("SCAB=", r(sce_ab), " ddl=", df_ab)
    print("SCR=", r(sce_r), " ddl=", df_r)
    print("SCT=", r(sce_t), " ddl=", df_t)
    input("Suite >")

    print("\n- P3: CM -")
    print("CMA=", r(ms_a))
    print("CMB=", r(ms_b))
    if n > 1: print("CMAB=", r(ms_ab))
    print("CMR=", r(ms_r))
    input("Suite >")

    concl_a2("Facteur A", F_a, df_a, df_r)
    concl_a2("Facteur B", F_b, df_b, df_r)
    if n > 1:
        concl_a2("Interaction AB", F_ab, df_ab, df_r)
    pause()

def chi2_fit():
    O = get_list("Obs")
    print("1.Theo 2.Prob")
    ch = input("? ")
    if ch == "1": T = get_list("Theo")
    else:
        P = get_list("Prob")
        s = sum(O)
        T = [p*s for p in P]
    if len(O)!=len(T): return

    hyp("Prop. obs. = Prop. theo.", "Les prop. different")

    chi2 = 0
    print("- 2. RESULTATS FIT -")
    print("Eff Theo:", ", ".join([r(x) for x in T]))
    print("---")

    for i in range(len(O)):
        if T[i] > 0:
            chi2 += ((O[i]-T[i])**2)/T[i]

    ddl = len(O)-1
    print("Chi2=", r(chi2))
    print("ddl=", ddl)
    concl(chi2, "Chi2", str(ddl), "Obs = Theo")

def chi2_indep():
    print("Nb Lignes ?")
    try: r_lines = int(input("? "))
    except: return
    rows = []
    for i in range(r_lines):
        rows.append(get_list("Lig "+str(i+1)))

    if len(rows) == 0: return

    hyp("Var. Independantes", "Liaison / Dependance")

    c = len(rows[0])
    total = sum([sum(row) for row in rows])

    chi2 = 0
    for i in range(r_lines):
        for j in range(c):
            tot_lig = sum(rows[i])
            tot_col = sum([rows[x][j] for x in range(r_lines)])
            theo = (tot_lig * tot_col) / total
            obs = rows[i][j]
            if theo > 0:
                chi2 += ((obs-theo)**2)/theo

    ddl = (r_lines-1)*(c-1)
    print("- 2. RESULTATS INDEP -")
    print("Chi2=", r(chi2))
    print("ddl=", ddl)
    concl(chi2, "Chi2", str(ddl), "Independance")

def reg_corr():
    X = get_list("X")
    Y = get_list("Y")
    if len(X)!=len(Y): return

    # Hypotheses formelles pour Correlation
    hyp("rho = 0 (Pas de lien lineaire)", "rho != 0 (Lien lineaire)")

    n = len(X)
    mx = mean(X)
    my = mean(Y)

    cov = sum([(X[i]-mx)*(Y[i]-my) for i in range(n)])/(n-1)
    vx = variance(X)
    vy = variance(Y)

    a = cov/vx
    b = my - a*mx
    r_val = cov/(sqrt(vx)*sqrt(vy))
    r2 = r_val**2

    sce_t = vy * (n - 1)
    sce_m = r2 * sce_t
    sce_r = sce_t - sce_m

    df_t = n - 1
    cm_t = sce_t / df_t if df_t > 0 else 0

    if abs(r_val) < 0.99999:
        t_corr = (r_val * sqrt(n-2)) / sqrt(1 - r2)
    else:
        t_corr = 1000

    ddl = n-2
    print("- 2. RESULTATS REG -")
    print("y = ax + b")
    print("a=", r(a), " b=", r(b))
    print("r=", r(r_val))
    print("---")
    print("SCT=", r(sce_t), " CMT=", r(cm_t))
    print("SCM=", r(sce_m))
    print("SCR=", r(sce_r))
    print("---")
    print("Test de Rho=0:")
    print("t_obs=", r(t_corr))
    print("ddl=", ddl)
    concl(t_corr, "t", str(ddl), "rho = 0")

def menu():
    while True:
        print("\n"*3)
        print("--- STAT V21 (ACADEMIQUE) ---")
        print("1.Desc   2.T-Ind")
        print("3.T-Pair 4.Anova1")
        print("5.Anova2 6.Chi2F")
        print("7.Chi2I  8.RegCor")
        print("9.THEORIE 0.Quitter")
        ch = input("Choix? ")

        if ch == "1": stat_desc()
        elif ch == "2": t_indep()
        elif ch == "3": t_pair()
        elif ch == "4": anova_1()
        elif ch == "5": anova_2()
        elif ch == "6": chi2_fit()
        elif ch == "7": chi2_indep()
        elif ch == "8": reg_corr()
        elif ch == "9": theorie()
        elif ch == "0": break

menu()
