def json_para_string(checklist):
    #assiduidade
    if checklist['assiduidade'] == 1:
        assiduidade = 'Chegou atrasado na atividade ou plantão (1.0).'
    else:
        assiduidade = 'Chegou pontualmente no horário (2.0).'

    #iniciativa
    if checklist['iniciativa'] == 2:
        iniciativa = 'Excelente (2.0).'
    elif checklist['iniciativa'] == 1.5:
        iniciativa = 'Satisfatório (1.5).'
    elif checklist['iniciativa'] == 1:
        iniciativa = 'Regular (1.0).'
    else:
        iniciativa = 'Insatisfatório (0.5).'
    #profissionalismo
    if checklist['profissionalismo'] == 2:
        profissionalismo = 'Excelente (2.0).'
    elif checklist['profissionalismo'] == 1.5:
        profissionalismo = 'Satisfatório (1.5).'
    elif checklist['profissionalismo'] == 1:
        profissionalismo = 'Regular (1.0).'
    else:
        profissionalismo = 'Insatisfatório (0.5).'
    
    #raciocinio_clinico
    if checklist['raciocinio_clinico'] == 2:
        raciocinio_clinico = 'Excelente (2.0).'
    elif checklist['raciocinio_clinico'] == 1.5:
        raciocinio_clinico = 'Satisfatório (1.5).'
    elif checklist['raciocinio_clinico'] == 1:
        raciocinio_clinico = 'Regular (1.0).'
    else:
        raciocinio_clinico = 'Insatisfatório (0.5).'

    #relacao_med_paciente
    if checklist['relacao_med_paciente'] == 2:
        relacao_med_paciente = 'Excelente (2.0).'
    elif checklist['relacao_med_paciente'] == 1.5:
        relacao_med_paciente = 'Satisfatório (1.5).'
    elif checklist['relacao_med_paciente'] == 1:
        relacao_med_paciente = 'Regular (1.0).'
    else:
        relacao_med_paciente = 'Insatisfatório (0.5).'
    
    return {
        'assiduidade': assiduidade,
        'iniciativa': iniciativa,
        'profissionalismo': profissionalismo,
        'raciocinio_clinico': raciocinio_clinico,
        'relacao_med_paciente': relacao_med_paciente
    }
