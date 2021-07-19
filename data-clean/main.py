import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/clean/', methods=['POST'])
def clean():
        data = request.get_json()
        df = pd.DataFrame([data])
                
        numerico = [
                  "email", 8, 18, 11, 15, 5, 4, 14, 9, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2
        ]

        df.columns = numerico

        labels = [
                  'email',
                  'PPI',
                  'ProgramasSociais',
                  #'ModalidadeEnsino',
                  'Beneficiario',
                  #'QtdDependentes',
                  #'EscolaridadePai',
                  #'EscolaridadeMae',
                  'RendaPerCapita',
                  'AtividadeRemunerada',
                  'SituacaoFinanceira',
                  'QtdResponsaveisFinanceiros',
                  'CondicaoTrabalho',
                  'CondicaoRenda',
                  'MoraCidadeCampus',
                  'CondMoradia',
                  'TipoTransporte',
                  'NConducoes',
                  'DoencaCronica',
                  'Deficiencia',
                  'FDoencaCronica',
                  'FMedicacao',
                  'Medicacao',
            ]

        nomes_ordenados = df.columns.to_list()[1:]
        nomes_ordenados.sort()
        nomes_ordenados = [df.columns.to_list()[0]] + nomes_ordenados

        df = df [nomes_ordenados]
        df.columns = labels

        condicoes = [
              'Desempregado',
              'Trabalhador Informal',
              'Trabalhador Autônomo',
              'Aposentado',
              'Empregado CLT',
              #'Pescador/agricultor familiar',
              'Beneficiário INSS',
              'Funcionário Público'
        ]

        rotulos = [
              'Desempregado',
              'Informal',
              'Autonomo',
              'Aposentado',
              'CLT',
              #'PescAgriF',
              'INSS',
              'FuncionarioPublico'
        ]

        for rotulo, cond in zip(rotulos, condicoes):
          df[rotulo] = df['CondicaoTrabalho'].map(lambda x: 'sim' if cond in x else 'nao')

        df['MoraCidadeCampus'] = df['MoraCidadeCampus'].apply(lambda x: x.split(',')[0].lower())

        df['TipoTransporte'] = df['TipoTransporte'].apply(lambda x: ''.join(x.split()[1]).capitalize())

        df['AteDois'] = df['QtdResponsaveisFinanceiros'].apply(lambda x: 'sim' if ' '.join(x.split()[:-1]) == '1' or ' '.join(x.split()[:-1]) == '2' else 'nao')

        df[['TipoTransporte', 'QtdResponsaveisFinanceiros', 'MoraCidadeCampus', 'AteDois']].head()

        binario = [
                  'PPI',
                  'ProgramasSociais',
                  #'Beneficiario',
                  #'AtividadeRemunerada',
                  'MoraCidadeCampus',
                  'DoencaCronica',
                  'Medicacao',
                  'Deficiencia',
                  'FDoencaCronica',
                  'FMedicacao',
                  'AteDois',
                  'Desempregado',
                  'Informal',
                  'Autonomo',
                  'Aposentado',
                  'CLT',
                  #'PescAgriF',
                  'INSS',
                  'FuncionarioPublico'
        ]

        df_binario = pd.DataFrame()

        for elemento in binario:
          df_binario[elemento] = df[elemento].replace(['sim', 'nao'], [1, 0]).astype(int)

        df_binario['AtividadeRemunerada'] = df['AtividadeRemunerada'].replace(['Sim', 'Nao'], [1, 0]).astype(int)

        modalidade_map = {
            'Graduação': 1,
            'Médio Integrado EJA': 2,
            'Médio Técnico Integrado': 4,
            'Técnico Subsequente': 3,
        }

        transporte_map = {
            'Pé': 1,
            'Próprio': 1,
            'Público': 2,
            'Alternativo': 3
        }

        escolaridade_map = {
            'Desconheço': 4,
            'Não se aplica': 4,
            'Sem escolaridade': 4,
            'Ensino fundamental': 3,
            'Ensino médio': 2,
            'Ensino superior': 1,
        }

        moradia_map = {
            'Própria': 1,
            'Cedida': 2,
            'Financiada': 3,
            'Alugada': 4,
            'Outros': 4
        }

        categorias = df['RendaPerCapita'].astype('category').cat.categories.tolist()
        valores = [3 , 2, 9, 8, 7, 6, 5, 4, 10, 1]
        renda_percapita_map = {k: v for k, v in zip(categorias, valores)}

        categorias = df['SituacaoFinanceira'].astype('category').cat.categories.tolist()
        valores = [4 , 2, 2, 1, 4, 5, 1]
        situacao_fin_map = {k: v for k, v in zip(categorias, valores)}

        # categorias = df['QtdDependentes'].astype('category').cat.categories.tolist()
        # valores = [2, 3, 4, 5, 1]
        # dependentes_map = {k: v for k, v in zip(categorias, valores)}

        categorias = df['NConducoes'].astype('category').cat.categories.tolist()
        valores = [2, 3, 1]
        conducoes_map = {k: v for k, v in zip(categorias, valores)}

        categorias = df['CondicaoRenda'].astype('category').cat.categories.tolist()
        valores = [1, 2, 3]
        cond_renda_map = {k: v for k, v in zip(categorias, valores)}

        labels = ['CondMoradia', 'TipoTransporte', 'RendaPerCapita', 'SituacaoFinanceira', 'NConducoes', 'CondicaoRenda']
        # "ModalidadeEnsino", "EscolaridadeMae", "EscolaridadePai", "QtdDependentes"
        label_encode = df[labels].copy()

        label_encode['CondMoradia'].replace(moradia_map, inplace=True)
        label_encode['TipoTransporte'].replace(transporte_map, inplace=True)
        #label_encode['EscolaridadePai'].replace(escolaridade_map, inplace=True)
        #label_encode['EscolaridadeMae'].replace(escolaridade_map, inplace=True)
        label_encode['SituacaoFinanceira'].replace(situacao_fin_map, inplace=True)
        label_encode['RendaPerCapita'].replace(renda_percapita_map, inplace=True)
        #label_encode['QtdDependentes'].replace(dependentes_map, inplace=True)
        label_encode['NConducoes'].replace(conducoes_map, inplace=True)
        label_encode['CondicaoRenda'].replace(cond_renda_map, inplace=True)
        #label_encode['ModalidadeEnsino'].replace(modalidade_map, inplace=True)

        qtd = pd.DataFrame()
        qtd_res = ['ResFin_1', 'ResFin_2', 'ResFin_3', 'ResFin_4ouMais']
        opcs = [
        '1 membro',
        '2 membros',
        '3 membros',
        '4 ou mais membros'
        ]

        df['QtdResponsaveisFinanceiros'].replace(opcs, qtd_res)

        for iqtd in qtd_res:
          qtd[iqtd] = df['QtdResponsaveisFinanceiros'].map(lambda x: int(1) if iqtd in x else int(0))

        dados_limpos = pd.concat([df_binario, label_encode, qtd], axis=1)

        dados = dados_limpos.columns.to_list()
        dados_limpos = dados_limpos[dados[:2] + [dados[16]] + dados[2:16] + dados[16+1:]]
        print(df)
        return jsonify(
                res = "teste"
        )

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
        
