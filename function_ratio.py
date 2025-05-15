import pandas as pd

def calculate_metabolite_ratios(data):
    missing_columns = []
    calculated_ratios = []
    skipped_ratios = []
    successful_ratios = []

    
    # Create a new DataFrame to store the ratios
    ratios_data = pd.DataFrame(index=data.index)
    
    # Проверяем наличие колонок перед расчетами
    def check_columns(required_cols, ratio_name):
        missing = [col for col in required_cols if col not in data.columns]
        if missing:
            missing_columns.extend(missing)
            skipped_ratios.append((ratio_name, missing))
            return False
        else:
            successful_ratios.append((ratio_name, required_cols))  # Добавляем удачные расчеты
            return True

    
    # Аргининовые соотношения
    if check_columns(['Arginine', 'Ornitine', 'Citrulline'], 'Arg/Orn+Cit'):
        ratios_data['Arg/Orn+Cit'] = data['Arginine']/(data['Ornitine']+data['Citrulline'])
        calculated_ratios.append('Arg/Orn+Cit')
    
    if check_columns(['Arginine', 'Ornitine'], 'Arg/Orn'):
        ratios_data['Arg/Orn'] = data['Arginine']/data['Ornitine']
        calculated_ratios.append('Arg/Orn')
    
    if check_columns(['Arginine', 'ADMA'], 'Arg/ADMA'):
        ratios_data["Arg/ADMA"] = data['Arginine']/data['ADMA']
        calculated_ratios.append('Arg/ADMA')
    
    if check_columns(['Arginine', 'Homoarginine', 'ADMA'], '(Arg+HomoArg)/ADMA'):
        ratios_data['(Arg+HomoArg)/ADMA'] = (data['Arginine']+data['Homoarginine'])/data['ADMA']
        calculated_ratios.append('(Arg+HomoArg)/ADMA')
    
    # Acylcarnitines
    if check_columns(['C0', 'C16', 'C18'], 'C0/(C16+C18)'):
        ratios_data['C0/(C16+C18)'] = data['C0']/(data['C16']+data['C18'])
        calculated_ratios.append('C0/(C16+C18)')
    
    if check_columns(['C16', 'C18', 'C2'], '(C16+C18)/C2'):
        ratios_data['(C16+C18)/C2'] = (data['C16']+data['C18'])/data['C2']
        calculated_ratios.append('(C16+C18)/C2')
    
    if check_columns(['C6', 'C8', 'C10', 'C2'], '(C6+C8+C10)/C2'):
        ratios_data['(C6+C8+C10)/C2'] = (data['C6']+data['C8']+data['C10'])/data['C2']
        calculated_ratios.append('(C6+C8+C10)/C2')
    
    if check_columns(['C3', 'C2'], 'C3/C2'):
        ratios_data['C3/C2'] = data['C3']/data['C2']
        calculated_ratios.append('C3/C2')
    
    # Tryptophan metabolism
    if check_columns(['Tryptophan', 'Kynurenine'], 'Trp/Kyn'):
        ratios_data['Trp/Kyn'] = data['Tryptophan']/data['Kynurenine']
        calculated_ratios.append('Trp/Kyn')
    
    if check_columns(['Tryptophan', 'Kynurenine', 'Quinolinic acid'], 'Trp/(Kyn+QA)'):
        ratios_data['Trp/(Kyn+QA)'] = data['Tryptophan']/(data['Kynurenine']+data['Quinolinic acid'])
        calculated_ratios.append('Trp/(Kyn+QA)')
    
    if check_columns(['Kynurenine', 'Quinolinic acid'], 'Kyn/Quin'):
        ratios_data['Kyn/Quin'] = data['Kynurenine']/data['Quinolinic acid']
        calculated_ratios.append('Kyn/Quin')
    
    if check_columns(['Quinolinic acid', 'HIAA'], 'Quin/HIAA'):
        ratios_data['Quin/HIAA'] = data['Quinolinic acid']/data['HIAA']
        calculated_ratios.append('Quin/HIAA')
    
    # Amino acids
    if check_columns(['Aspartic acid', 'Asparagine'], 'Aspartate/Asparagine'):
        ratios_data['Aspartate/Asparagine'] = data['Aspartic acid']/data['Asparagine']
        calculated_ratios.append('Aspartate/Asparagine')
    
    if check_columns(['Glutamine', 'Glutamic acid'], 'Glutamine/Glutamate'):
        ratios_data['Glutamine/Glutamate'] = data['Glutamine']/data['Glutamic acid']
        calculated_ratios.append('Glutamine/Glutamate')
    
    if check_columns(['Glycine', 'Serine'], 'Glycine/Serine'):
        ratios_data['Glycine/Serine'] = data['Glycine']/data['Serine']
        calculated_ratios.append('Glycine/Serine')
    
    if check_columns(['Glutamic acid', 'Serine', 'Glycine'], 'GSG_index'):
        ratios_data['GSG_index'] = data['Glutamic acid']/(data['Serine']+data['Glycine'])
        calculated_ratios.append('GSG_index')
    
    if check_columns(['Phenylalanine', 'Tyrosin'], 'Phe/Tyr'):
        ratios_data['Phe/Tyr'] = data['Phenylalanine']/data['Tyrosin']
        calculated_ratios.append('Phe/Tyr')
    
    if check_columns(['Phenylalanine', 'Tyrosin'], 'Phe+Tyr'):
        ratios_data['Phe+Tyr'] = data['Phenylalanine']+data['Tyrosin']
        calculated_ratios.append('Phe+Tyr')
    
    if check_columns(['Summ Leu-Ile', 'Valine', 'Phenylalanine', 'Tyrosin'], 'BCAA/AAA'):
        ratios_data['BCAA'] = data['Summ Leu-Ile']+data['Valine']
        ratios_data['BCAA/AAA'] = (data['Valine']+data['Summ Leu-Ile'])/(data['Phenylalanine']+data['Tyrosin'])
        calculated_ratios.append('BCAA/AAA')
    
    # Betaine_choline metabolism
    if check_columns(['Betaine', 'Choline'], 'Betaine/choline'):
        ratios_data['Betaine/choline'] = data['Betaine']/data['Choline']
        calculated_ratios.append('Betaine/choline')
    
    if check_columns(['Kynurenine', 'Tryptophan'], 'Kyn/Trp'):
        ratios_data['Kyn/Trp'] = data['Kynurenine']/data['Tryptophan']
        calculated_ratios.append('Kyn/Trp')
    
    if check_columns(['C14', 'C14-1', 'C14-2', 'C14-OH', 'C16', 'C16-1', 'C16-1-OH', 'C16-OH', 'C18', 'C18-1', 'C18-1-OH', 'C18-2', 'C18-OH'], 'СДК'):
        ratios_data['СДК'] = data['C14']+data['C14-1']+data['C14-2']+data['C14-OH']+data['C16']+data['C16-1']+data['C16-1-OH']+data['C16-OH']+data['C18']+data['C18-1']+data['C18-1-OH']+data['C18-2']+data['C18-OH']
        calculated_ratios.append('СДК')
    
    if check_columns(['Alanine', 'Valine'], 'Alanine / Valine'):
        ratios_data['Alanine / Valine'] = data['Alanine']/data['Valine']
        calculated_ratios.append('Alanine / Valine')
    
    if check_columns(['Tryptamine', 'Indole-3-acetic acid'], 'Tryptamine / IAA'):
        ratios_data['Tryptamine / IAA'] = data['Tryptamine']/data['Indole-3-acetic acid']
        calculated_ratios.append('Tryptamine / IAA')
    
    if check_columns(['C2', 'C0'], 'С2/С0'):
        ratios_data['С2/С0'] = data['C2']/data['C0']
        calculated_ratios.append('С2/С0')
    
    if check_columns(['C2', 'C3', 'C0'], '(C2+C3)/C0'):
        ratios_data['(C2+C3)/C0'] = (data['C2']+data['C3'])/data['C0']
        calculated_ratios.append('(C2+C3)/C0')
    
    if check_columns(['Kynurenic acid', 'Kynurenine'], 'Kynurenic acid / Kynurenine'):
        ratios_data['Kynurenic acid / Kynurenine'] = data['Kynurenic acid']/data['Kynurenine']
        calculated_ratios.append('Kynurenic acid / Kynurenine')
    
    if check_columns(['Methionine', 'Taurine'], 'Methionine + Taurine'):
        ratios_data['Methionine + Taurine'] = data['Methionine']+data['Taurine']
        calculated_ratios.append('Methionine + Taurine')
    
    if check_columns(['Valine', 'Alanine'], 'Valine / Alanine'):
        ratios_data['Valine / Alanine'] = data['Valine']/data['Alanine']
        calculated_ratios.append('Valine / Alanine')
    
    if check_columns(['Riboflavin', 'Pantothenic'], 'Riboflavin / Pantothenic'):
        ratios_data['Riboflavin / Pantothenic'] = data['Riboflavin']/data['Pantothenic']
        calculated_ratios.append('Riboflavin / Pantothenic')
    
    if check_columns(['ADMA', 'NMMA'], 'ADMA / NMMA'):
        ratios_data['ADMA / NMMA'] = data['ADMA']/data['NMMA']
        calculated_ratios.append('ADMA / NMMA')
    
    if check_columns(['DMG', 'Choline'], 'DMG / Choline'):
        ratios_data['DMG / Choline'] = data['DMG']/data['Choline']
        calculated_ratios.append('DMG / Choline')
    
    if check_columns(['TMAO', 'Betaine', 'C0', 'Choline'], 'TMAO Synthesis'):
        ratios_data['TMAO Synthesis'] = data['TMAO']/(data['Betaine']+data['C0']+data['Choline'])
        calculated_ratios.append('TMAO Synthesis')
    
    if check_columns(['TMAO', 'Choline'], 'TMAO Synthesis (direct)'):
        ratios_data['TMAO Synthesis (direct)'] = data['TMAO']/data['Choline']
        calculated_ratios.append('TMAO Synthesis (direct)')
    
    if check_columns(['Proline', 'Phenylalanine'], 'DLD (NBS)'):
        ratios_data['DLD (NBS)'] = data['Proline']/data['Phenylalanine']
        calculated_ratios.append('DLD (NBS)')
    
    if check_columns(['Methionine', 'Phenylalanine'], 'MTHFR Deficiency (NBS)'):
        ratios_data['MTHFR Deficiency (NBS)'] = data['Methionine']/data['Phenylalanine']
        calculated_ratios.append('MTHFR Deficiency (NBS)')
    
    # Ratio of Non-Essential to Essential AAs
    non_essential = ['Alanine', 'Arginine', 'Asparagine', 'Aspartic acid', 'Glutamine', 
                    'Glutamic acid', 'Glycine', 'Proline', 'Serine', 'Tyrosin']
    essential = ['Histidine', 'Summ Leu-Ile', 'Lysine', 'Methionine', 
                'Phenylalanine', 'Threonine', 'Tryptophan', 'Valine']
    
    if check_columns(non_essential + essential, 'Ratio of Non-Essential to Essential AAs'):
        ratios_data['Ratio of Non-Essential to Essential AAs'] = (
            data[non_essential].sum(axis=1) / data[essential].sum(axis=1))
        calculated_ratios.append('Ratio of Non-Essential to Essential AAs')

    if check_columns(['Proline', 'Citrulline'], 'Ratio of Pro to Cit'):
        ratios_data['Ratio of Pro to Cit'] = data['Proline']/data['Citrulline']
        calculated_ratios.append('Ratio of Pro to Cit')

    # Sum calculations
    all_aas = non_essential + essential
    if check_columns(all_aas, 'Sum of AAs'):
        ratios_data['Sum of AAs'] = data[all_aas].sum(axis=1)
        calculated_ratios.append('Sum of AAs')

    if check_columns(essential, 'Sum of Essential Aas'):
        ratios_data['Sum of Essential Aas'] = data[essential].sum(axis=1)
        calculated_ratios.append('Sum of Essential Aas')

    if check_columns(non_essential, 'Sum of Non-Essential AAs'):
        ratios_data['Sum of Non-Essential AAs'] = data[non_essential].sum(axis=1)
        calculated_ratios.append('Sum of Non-Essential AAs')

    glucogenic = ['Alanine', 'Arginine', 'Asparagine', 'Aspartic acid', 'Glutamine',
                 'Glutamic acid', 'Glycine', 'Histidine', 'Methionine', 'Proline',
                 'Serine', 'Threonine', 'Valine']
    if check_columns(glucogenic, 'Sum of Solely Glucogenic AAs'):
        ratios_data['Sum of Solely Glucogenic AAs'] = data[glucogenic].sum(axis=1)
        calculated_ratios.append('Sum of Solely Glucogenic AAs')

    if check_columns(['Summ Leu-Ile', 'Lysine'], 'Sum of Solely Ketogenic AAs'):
        ratios_data['Sum of Solely Ketogenic AAs'] = data['Summ Leu-Ile'] + data['Lysine']
        calculated_ratios.append('Sum of Solely Ketogenic AAs')

    # NBS and other ratios
    if check_columns(['Valine', 'Phenylalanine'], 'Valinemia (NBS)'):
        ratios_data['Valinemia (NBS)'] = data['Valine']/data['Phenylalanine']
        calculated_ratios.append('Valinemia (NBS)')

    if check_columns(['Carnosine', 'Histidine'], 'Carnosine Synthesis'):
        ratios_data['Carnosine Synthesis'] = data['Carnosine']/data['Histidine']
        calculated_ratios.append('Carnosine Synthesis')

    if check_columns(['Citrulline', 'Ornitine'], 'Cit Synthesis'):
        ratios_data['Cit Synthesis'] = data['Citrulline']/data['Ornitine']
        calculated_ratios.append('Cit Synthesis')

    if check_columns(['Citrulline', 'Phenylalanine'], 'CPS Deficiency (NBS)'):
        ratios_data['CPS Deficiency (NBS)'] = data['Citrulline']/data['Phenylalanine']
        calculated_ratios.append('CPS Deficiency (NBS)')

    if check_columns(['Homoarginine', 'Arginine', 'Lysine'], 'HomoArg Synthesis'):
        ratios_data['HomoArg Synthesis'] = data['Homoarginine']/(data['Arginine']+data['Lysine'])
        calculated_ratios.append('HomoArg Synthesis')

    if check_columns(['Methionine-Sulfoxide', 'Methionine'], 'Met Oxidation'):
        ratios_data['Met Oxidation'] = data['Methionine-Sulfoxide']/data['Methionine']
        calculated_ratios.append('Met Oxidation')

    if check_columns(['Citrulline', 'Arginine'], 'NO-Synthase Activity'):
        ratios_data['NO-Synthase Activity'] = data['Citrulline']/data['Arginine']
        calculated_ratios.append('NO-Synthase Activity')

    if check_columns(['Ornitine', 'Arginine'], 'Orn Synthesis'):
        ratios_data['Orn Synthesis'] = data['Ornitine']/data['Arginine']
        calculated_ratios.append('Orn Synthesis')

    if check_columns(['Ornitine', 'Citrulline'], 'OTC Deficiency (NBS)'):
        ratios_data['OTC Deficiency (NBS)'] = data['Ornitine']/data['Citrulline']
        calculated_ratios.append('OTC Deficiency (NBS)')

    if check_columns(['Homoarginine', 'ADMA'], 'Ratio of HArg to ADMA'):
        ratios_data['Ratio of HArg to ADMA'] = data['Homoarginine']/data['ADMA']
        calculated_ratios.append('Ratio of HArg to ADMA')

    if check_columns(['Homoarginine', 'TotalDMA (SDMA)'], 'Ratio of HArg to SDMA'):
        ratios_data['Ratio of HArg to SDMA'] = data['Homoarginine']/data['TotalDMA (SDMA)']
        calculated_ratios.append('Ratio of HArg to SDMA')

    if check_columns(['TotalDMA (SDMA)', 'ADMA', 'Arginine'], 'Sum of Asym. and Sym. Arg Methylation'):
        ratios_data['Sum of Asym. and Sym. Arg Methylation'] = (data['TotalDMA (SDMA)']+data['ADMA'])/data['Arginine']
        calculated_ratios.append('Sum of Asym. and Sym. Arg Methylation')

    if check_columns(['TotalDMA (SDMA)'], 'Symmetrical Arg Methylation'):
        ratios_data['Symmetrical Arg Methylation'] = data['TotalDMA (SDMA)']
        calculated_ratios.append('Symmetrical Arg Methylation')

    if check_columns(['Histamine', 'Histidine'], 'Histamine Synthesis'):
        ratios_data['Histamine Synthesis'] = data['Histamine']/data['Histidine']
        calculated_ratios.append('Histamine Synthesis')

    # Carnitines
    if check_columns(['C5', 'C3'], '2MBG (NBS)'):
        ratios_data['2MBG (NBS)'] = data['C5']/data['C3']
        calculated_ratios.append('2MBG (NBS)')

    if check_columns(['C0', 'C2', 'C3', 'C16', 'C18', 'C18-1', 'Citrulline'], 'Carnitine Uptake Defect (NBS)'):
        ratios_data['Carnitine Uptake Defect (NBS)'] = (data['C0']+data['C2']+data['C3']+data['C16']+data['C18']+data['C18-1'])/data['Citrulline']
        calculated_ratios.append('Carnitine Uptake Defect (NBS)')

    if check_columns(['C16', 'C18-1', 'C2'], 'CPT-2 Deficiency (NBS)'):
        ratios_data['CPT-2 Deficiency (NBS)'] = (data['C16']+data['C18-1'])/data['C2']
        calculated_ratios.append('CPT-2 Deficiency (NBS)')

    if check_columns(['C4', 'C8'], 'EMA (NBS)'):
        ratios_data['EMA (NBS)'] = data['C4']/data['C8']
        calculated_ratios.append('EMA (NBS)')

    if check_columns(['C4', 'C2'], 'IBD Deficiency (NBS)'):
        ratios_data['IBD Deficiency (NBS)'] = data['C4']/data['C2']
        calculated_ratios.append('IBD Deficiency (NBS)')

    if check_columns(['C5', 'C2'], 'IVA (NBS)'):
        ratios_data['IVA (NBS)'] = data['C5']/data['C2']
        calculated_ratios.append('IVA (NBS)')

    if check_columns(['C16-OH', 'C16'], 'LCHAD Deficiency (NBS)'):
        ratios_data['LCHAD Deficiency (NBS)'] = data['C16-OH']/data['C16']
        calculated_ratios.append('LCHAD Deficiency (NBS)')

    if check_columns(['C3', 'C2'], 'MA (NBS)'):
        ratios_data['MA (NBS)'] = data['C3']/data['C2']
        calculated_ratios.append('MA (NBS)')

    if check_columns(['C16', 'C3'], 'MC Deficiency (NBS)'):
        ratios_data['MC Deficiency (NBS)'] = data['C16']/data['C3']
        calculated_ratios.append('MC Deficiency (NBS)')

    if check_columns(['C8', 'C2'], 'MCAD Deficiency (NBS)'):
        ratios_data['MCAD Deficiency (NBS)'] = data['C8']/data['C2']
        calculated_ratios.append('MCAD Deficiency (NBS)')

    if check_columns(['C8', 'C10'], 'MCKAT Deficiency (NBS)'):
        ratios_data['MCKAT Deficiency (NBS)'] = data['C8']/data['C10']
        calculated_ratios.append('MCKAT Deficiency (NBS)')

    if check_columns(['C3', 'C0'], 'MMA (NBS)'):
        ratios_data['MMA (NBS)'] = data['C3']/data['C0']
        calculated_ratios.append('MMA (NBS)')

    if check_columns(['C3', 'C16'], 'PA (NBS)'):
        ratios_data['PA (NBS)'] = data['C3']/data['C16']
        calculated_ratios.append('PA (NBS)')

    if check_columns(['C2', 'C0'], 'Ratio of Acetylcarnitine to Carnitine'):
        ratios_data['Ratio of Acetylcarnitine to Carnitine'] = data['C2']/data['C0']
        calculated_ratios.append('Ratio of Acetylcarnitine to Carnitine')

    # Ratio of AC-OHs to ACs (complex ratio)
    ac_ohs = ['C5-OH', 'C14-OH', 'C16-1-OH', 'C16-OH', 'C18-1-OH', 'C18-OH']
    acs = ['C0', 'C10', 'C10-1', 'C10-2', 'C12', 'C12-1', 'C14', 'C14-1', 'C14-2',
          'C16', 'C16-1', 'C18', 'C18-1', 'C18-2', 'C2', 'C3', 'C4', 'C5', 'C5-1',
          'C5-DC', 'C6', 'C6-DC', 'C8', 'C8-1']
    
    if check_columns(ac_ohs + acs, 'Ratio of AC-OHs to ACs'):
        ratios_data['Ratio of AC-OHs to ACs'] = (
            data[ac_ohs].sum(axis=1) / data[acs].sum(axis=1))
        calculated_ratios.append('Ratio of AC-OHs to ACs')

    if check_columns(['C5', 'C0'], 'SBCAD Deficiency (NBS)'):
        ratios_data['SBCAD Deficiency (NBS)'] = data['C5']/data['C0']
        calculated_ratios.append('SBCAD Deficiency (NBS)')

    if check_columns(['C4', 'C3'], 'SCAD Deficiency (NBS)'):
        ratios_data['SCAD Deficiency (NBS)'] = data['C4']/data['C3']
        calculated_ratios.append('SCAD Deficiency (NBS)')

    # Sum of ACs
    all_acs = ac_ohs + acs
    if check_columns(all_acs, 'Sum of ACs'):
        ratios_data['Sum of ACs'] = data[all_acs].sum(axis=1)
        calculated_ratios.append('Sum of ACs')

    # Sum of MUFA-ACs
    mufa_acs = ['C16-1-OH', 'C18-1-OH', 'C10-1', 'C12-1', 'C14-1', 'C16-1', 'C18-1', 'C8-1', 'C5-1']
    if check_columns(mufa_acs, 'Sum of MUFA-ACs'):
        ratios_data['Sum of MUFA-ACs'] = data[mufa_acs].sum(axis=1)
        calculated_ratios.append('Sum of MUFA-ACs')

    # Sum of PUFA-ACs
    pufa_acs = ['C10-2', 'C14-2', 'C18-2']
    if check_columns(pufa_acs, 'Sum of PUFA-ACs'):
        ratios_data['Sum of PUFA-ACs'] = data[pufa_acs].sum(axis=1)
        calculated_ratios.append('Sum of PUFA-ACs')

    if check_columns(['C16', 'C16-OH'], 'TFP Deficiency (NBS)'):
        ratios_data['TFP Deficiency (NBS)'] = data['C16']/data['C16-OH']
        calculated_ratios.append('TFP Deficiency (NBS)')

    if check_columns(['C14-1', 'C16'], 'VLCAD Deficiency (NBS)'):
        ratios_data['VLCAD Deficiency (NBS)'] = data['C14-1']/data['C16']
        calculated_ratios.append('VLCAD Deficiency (NBS)')
    
    # В конце функции возвращаем не только данные, но и информацию о пропущенных колонках
    return data, ratios_data, list(set(missing_columns)), skipped_ratios, calculated_ratios,successful_ratios