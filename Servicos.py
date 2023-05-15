#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importando bibliotecas
import pandas as pd


# In[50]:


#importando bases de dados
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')
clientes_df = pd.read_csv('CadastroClientes.csv',sep=';',decimal=',')
funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')


display(servicos_df)
display(funcionarios_df)
display(clientes_df)


# In[51]:


#eliminando colunas indesejaveis

funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)

display(funcionarios_df)


# In[52]:


#despesa salarial da empresa

funcionarios_df['Salário Final'] = funcionarios_df['Salario Base'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR'] - funcionarios_df['Impostos']
ST = funcionarios_df['Salário Final'].sum()
print('Despesa salarial total é de R$ {:,.2f}'.format(ST))


# In[53]:


#faturamento total

faturamento_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente','Valor Contrato Mensal']], on='ID Cliente')

faturamento_df['Faturamento Total'] = faturamento_df['Tempo Total de Contrato (Meses)'] *  faturamento_df['Valor Contrato Mensal']

#display(faturamento_df)

FT = faturamento_df['Faturamento Total'].sum()

print('Faturamento total é de R$ {:,.2f}'.format(FT))


# In[54]:


#percentual de funccionariso que fecharam contrato

funcionarios_ct = len(servicos_df['ID Funcionário'].unique())
funcionarios_tt = len(funcionarios_df['ID Funcionário'])
print('A porcentagem de funcionários que fecharam contrato é de {:.2%}'.format(funcionarios_ct/funcionarios_tt))


# In[55]:


#contratos por área

area_df = servicos_df.merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')
qtde = area_df['Area'].value_counts()
print(qtde)

qtde.plot(kind='bar', figsize=(15,5))


# In[56]:


#funcionários por área
fun_area = funcionarios_df['Area'].value_counts()
print(fun_area)

fun_area.plot(kind='bar', figsize=(15,5))


# In[57]:


#calculando o ticket medio mensal

ticket = clientes_df['Valor Contrato Mensal'].mean()
print('O ticket médio mensal é de R$ {:,.2f}'.format(ticket))

