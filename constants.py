# Список всех возможных соотношений, которые может рассчитывать функция
all_possible_ratios = [
    # Аргининовые соотношения
    'Arg/Orn+Cit', 'Arg/Orn', 'Arg/ADMA', '(Arg+HomoArg)/ADMA',
    
    # Acylcarnitines
    'C0/(C16+C18)', '(C16+C18)/C2', '(C6+C8+C10)/C2', 'C3/C2',
    
    # Tryptophan metabolism
    'Trp/Kyn', 'Trp/(Kyn+QA)', 'Kyn/Quin', 'Quin/HIAA',
    
    # Amino acids
    'Aspartate/Asparagine', 'Glutamine/Glutamate', 'Glycine/Serine',
    'GSG_index', 'Phe/Tyr', 'Phe+Tyr', 'BCAA/AAA',
    
    # Betaine_choline metabolism
    'Betaine/choline', 'Kyn/Trp', 'СДК', 'Alanine / Valine',
    'Tryptamine / IAA', 'С2/С0', '(C2+C3)/C0',
    'Kynurenic acid / Kynurenine', 'Methionine + Taurine',
    'Valine / Alanine', 'Riboflavin / Pantothenic', 'ADMA / NMMA',
    'DMG / Choline', 'TMAO Synthesis', 'TMAO Synthesis (direct)',
    'DLD (NBS)', 'MTHFR Deficiency (NBS)',
    
    # Ratio of Non-Essential to Essential AAs
    'Ratio of Non-Essential to Essential AAs', 'Ratio of Pro to Cit',
    
    # Sum calculations
    'Sum of AAs', 'Sum of Essential Aas', 'Sum of Non-Essential AAs',
    'Sum of Solely Glucogenic AAs', 'Sum of Solely Ketogenic AAs',
    
    # NBS and other ratios
    'Valinemia (NBS)', 'Carnosine Synthesis', 'Cit Synthesis',
    'CPS Deficiency (NBS)', 'HomoArg Synthesis', 'Met Oxidation',
    'NO-Synthase Activity', 'Orn Synthesis', 'OTC Deficiency (NBS)',
    'Ratio of HArg to ADMA', 'Ratio of HArg to SDMA',
    'Sum of Asym. and Sym. Arg Methylation', 'Symmetrical Arg Methylation',
    'Histamine Synthesis',
    
    # Carnitines
    '2MBG (NBS)', 'Carnitine Uptake Defect (NBS)', 'CPT-2 Deficiency (NBS)',
    'EMA (NBS)', 'IBD Deficiency (NBS)', 'IVA (NBS)', 'LCHAD Deficiency (NBS)',
    'MA (NBS)', 'MC Deficiency (NBS)', 'MCAD Deficiency (NBS)',
    'MCKAT Deficiency (NBS)', 'MMA (NBS)', 'PA (NBS)',
    'Ratio of Acetylcarnitine to Carnitine', 'Ratio of AC-OHs to ACs',
    'SBCAD Deficiency (NBS)', 'SCAD Deficiency (NBS)', 'Sum of ACs',
    'Sum of MUFA-ACs', 'Sum of PUFA-ACs', 'TFP Deficiency (NBS)',
    'VLCAD Deficiency (NBS)'
]

all_possible_ratios_zebra = [
    # Аргининовые соотношения
    'Arg/Orn+Cit', 'Arg/Orn', 'Arg/ADMA', '(Arg+HomoArg)/ADMA',
    
    # Acylcarnitines
    'C0/(C16+C18)', '(C16+C18)/C2', '(C6+C8+C10)/C2', 'C3/C2',
    
    # Tryptophan metabolism
    'Trp/Kyn', 'Trp/(Kyn+QA)', 'Kyn/Quin', 'Quin/HIAA',
    
    # Amino acids
    'Aspartate/Asparagine', 'Glutamine/Glutamate', 'Glycine/Serine',
    'GSG_index', 'Phe/Tyr', 'Phe+Tyr', 'BCAA/AAA',
    
    # Betaine_choline metabolism
    'Betaine/choline', 'Kyn/Trp', 'СДК', 'Alanine / Valine',
    'Tryptamine / IAA', 'С2/С0', '(C2+C3)/C0',
    'Kynurenic acid / Kynurenine', 'Methionine + Taurine',
    'Valine / Alanine', 'Riboflavin / Pantothenic', 'ADMA / NMMA',
    'DMG / Choline', 'TMAO Synthesis', 'TMAO Synthesis (direct)',
    'DLD (NBS)', 'MTHFR Deficiency (NBS)',
    
    # Ratio of Non-Essential to Essential AAs
    'Ratio of Non-Essential to Essential AAs', 'Ratio of Pro to Cit',
    
    # Sum calculations
    'Sum of AAs', 'Sum of Essential Aas', 'Sum of Non-Essential AAs',
    'Sum of Solely Glucogenic AAs', 'Sum of Solely Ketogenic AAs',
    
    # NBS and other ratios
    'Valinemia (NBS)', 'Carnosine Synthesis', 'Cit Synthesis',
    'CPS Deficiency (NBS)', 'HomoArg Synthesis', 'Met Oxidation',
    'NO-Synthase Activity', 'Orn Synthesis', 'OTC Deficiency (NBS)',
    'Ratio of HArg to ADMA', 'Ratio of HArg to SDMA',
    'Sum of Asym. and Sym. Arg Methylation', 'Symmetrical Arg Methylation',
    'Histamine Synthesis',
    
    # Carnitines
    '2MBG (NBS)', 'Carnitine Uptake Defect (NBS)', 'CPT-2 Deficiency (NBS)',
    'EMA (NBS)', 'IBD Deficiency (NBS)', 'IVA (NBS)', 'LCHAD Deficiency (NBS)',
    'MA (NBS)', 'MC Deficiency (NBS)', 'MCAD Deficiency (NBS)',
    'MCKAT Deficiency (NBS)', 'MMA (NBS)', 'PA (NBS)',
    'Ratio of Acetylcarnitine to Carnitine', 'Ratio of AC-OHs to ACs',
    'SBCAD Deficiency (NBS)', 'SCAD Deficiency (NBS)', 'Sum of ACs',
    'Sum of MUFA-ACs', 'Sum of PUFA-ACs', 'TFP Deficiency (NBS)',
    'VLCAD Deficiency (NBS)',

    #дополнительные отношения нейромедиаторов
    'DOPA / Dopamine','Dopamine / Norepinephrine',
    'Norepinephrine / Epinephrine',
    'Metanephrine / Epinephrine','Normetanephrine / Norepinephrine',
    'Dopamine / Serotonin','Glutamine / Glutamic acid'
]   

