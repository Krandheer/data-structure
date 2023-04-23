masterD = {'TARN0380': {'T3': 500, 'C3': 500},
           'TARS0638': {'T3': 500},
           'TARS0716': {'T3': 500, 'C3': 500},
           'TKBE0035': {'T3': 500, 'C3': 500}}

sbi_master_d = {'S1AC0165008': {'T2': 100, 'T3': 500, 'T4': 500, 'C2': 100, 'C3': 500},
                'S1AC0482703': {'T2': 100, 'T3': 500, 'C2': 100, 'C3': 500},
                'S1AC0490501': {'T2': 100, 'T3': 500, 'C2': 100, 'C3': 500},
                'S1ACMU23': {'T1': 100, 'T3': 500, 'C1': 100, 'C3': 500},
                'S1ANPK14': {'T1': 100, 'T2': 200, 'T3': 500, 'C1': 100, 'C2': 200, 'C3': 500}, }

sbi_atmids = ["S1AC0165008", "S1ACMU23"]


def som_fun(atmid):
    global masterD
    if atmid in sbi_master_d:
        masterD = sbi_master_d

    print(masterD)

som_fun('TKBE0035')
