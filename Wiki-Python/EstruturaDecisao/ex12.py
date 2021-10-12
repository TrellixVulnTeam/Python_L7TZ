vhora = int(input('Digite o valor de sua hora trabalhada : '))
qhoras = int(input("Digite o quantidade de horas trabalhadas : "))
v_sal = (vhora * qhoras)
print("o salario é : ", v_sal)
if v_sal <=900:
    print ("(-) IR : CATEGORIA ISENTO : --")
    inss = (v_sal*10)/100
    print ("(-) INSS :              ", inss)
    sind = (v_sal*3)/100
    print ("(-) SINDICATO :         ", sind)
    fgts = (v_sal*11)/100
    print ("FGTS :                  ", fgts)
    descontos = (inss + sind)
    n_sal = (v_sal-descontos)
    print ("(-) DESCONTOS :         ",descontos)
    print ("SAlARIO :               ", n_sal)
if v_sal > 900 and v_sal <=1500:
    inss = (v_sal * 10) / 100
    print("(-) INSS :              ", inss)
    sind = (v_sal * 3) / 100
    print("(-) SINDICATO :         ", sind)
    fgts = (v_sal * 11) / 100
    print("FGTS :                  ", fgts)
    ir = (v_sal*5)/100
    print("(-) IR                  ", ir)
    descontos = (inss + sind + ir)
    n_sal = (v_sal - descontos)
    print("(-) DESCONTOS :         ", descontos)
    print("SAlARIO :               ", n_sal)
if v_sal > 1500 and v_sal <=2500:
    inss = (v_sal * 10) / 100
    print("(-) INSS :              ", inss)
    sind = (v_sal * 3) / 100
    print("(-) SINDICATO :         ", sind)
    fgts = (v_sal * 11) / 100
    print("FGTS :                  ", fgts)
    ir = (v_sal*5)/100
    print("(-) IR                  ", ir)
    descontos = (inss + sind + ir)
    n_sal = (v_sal - descontos)
    print("(-) DESCONTOS :         ", descontos)
    print("SAlARIO :               ", n_sal)
if v_sal > 2500:
    inss = (v_sal * 10) / 100
    print("(-) INSS :              ", inss)
    sind = (v_sal * 3) / 100
    print("(-) SINDICATO :         ", sind)
    fgts = (v_sal * 11) / 100
    print("FGTS :                  ", fgts)
    ir = (v_sal*5)/100
    print("(-) IR                  ", ir)
    descontos = (inss + sind + ir)
    n_sal = (v_sal - descontos)
    print("(-) DESCONTOS :         ", descontos)
    print("SAlARIO :               ", n_sal)
