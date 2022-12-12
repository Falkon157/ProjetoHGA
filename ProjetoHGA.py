import streamlit as st

st.title('Bem vinda a sua calculadora!! Siga os passos abaixo e vou te ajudar.')

estimativa = st.selectbox('Selecione o que você quer calcular:',['Estimativa de Peso', 'Estimativa de Altura'])

genero = st.selectbox('Selecione o gênero',['Mulher', 'Homem'])

cor = st.selectbox('Selecione a cor do paciente',['Branca', 'Negra'])

idade = st.number_input('Idade do paciente',min_value=1 , max_value=120)

aj = st.number_input('Digite o AJ do paciente: ')

cb = st.number_input('Digite o CB do paciente: ')


if estimativa == 'Estimativa de Peso' and genero == 'Mulher' and cor == 'Branca' and idade < 60:



    peso = (aj * 1.01) + (cb * 2.81) - 66.04
    st.text('O peso estimado do paciente é {:.2f} kilos'.format(peso))

    dp = st.number_input('Para este caso o desvio padrão é de +- 10,60. Digite o valor do desvio padrão que você quer usar.')
    pesofinal = peso + dp
    st.text("O peso final ficou em : {:.2f} kilos".format(pesofinal))

elif estimativa == 'Estimativa de Peso' and genero == 'Mulher' and cor == 'Branca' and idade >= 60:


    peso = (aj * 1.09) + (cb * 2.68) - 65.51
    st.text('O peso estimado do paciente é {:.2f} kilos '.format(peso))

    dp = st.number_input ('Para este caso o desvio padrão é de +- 11,42. Digite o valor do desvio padrão que você quer usar.')
    pesofinal = peso + dp
    st.text("o peso final ficou em : {:.2f} kilos".format(pesofinal))


elif estimativa == 'Estimativa de Peso' and genero == 'Mulher' and cor == 'Negra' and  idade < 60:

    peso = (aj * 1.01) + (cb * 2.81) - 66.04
    st.text('o peso estimado do paciente é {:.2f} kilos'.format(peso))

    dp = st.number_input('Para este caso o desvio padrão é de +- 11,98. Digite o valor do desvio padrão que você quer usar.')
    pesofinal = peso + dp
    st.text("o peso final ficou em : {:.2f} kilos ".format(pesofinal))


elif estimativa == 'Estimativa de Peso' and genero == 'Mulher' and cor == 'Negra' and idade >= 60:

    peso = (aj * 1.09) + (cb * 2.68) - 65.51
    st.text('o peso estimado do paciente é {:.2f} kilos '.format(peso))

    dp = st.number_input('Para este caso o desvio padrão é de +- 14,52. Digite o valor do desvio padrão que você quer usar.')
    pesofinal = peso + dp
    st.text("o peso final ficou em : {:.2f} kilos".format(pesofinal))


elif estimativa == 'Estimativa de Peso' and genero == 'Homem' and cor == 'Branca'and idade < 60:

    peso = (aj * 1.19) + (cb * 3.21) - 86.82
    st.text('o peso estimado do paciente é {:.2f} kilos'.format(peso))

    dp = st.number_input('Para este caso o desvio padrão é de +- 11,42. Digite o valor do desvio padrão que você quer usar.')
    pesofinal = peso + dp
    st.text("o peso final ficou em : {:.2f} kilos".format(pesofinal))

elif estimativa == 'Estimativa de Peso' and genero == 'Homem' and cor == 'Branca'and idade >= 60:

    peso = (aj * 1.10) + (cb * 3.07) - 75.81
    st.text('o peso estimado do paciente é {:.2f} kilos '.format(peso))

    dp = st.number_input('Para este caso o desvio padrão é de +- 11,46. Digite o valor do desvio padrão que você quer usar.')
    pesofinal = peso + dp
    st.text("o peso final ficou em : {:.2f} kilos".format(pesofinal))


elif estimativa == 'Estimativa de Peso' and genero == 'Homem' and cor == 'Negra'and idade < 60:

    peso = (aj * 1.09) + (cb * 3.14) - 83.72
    st.text('o peso estimado do paciente é {:.2f} kilos '.format(peso))

    dp = st.number_input('Para este caso o desvio padrão é de +- 11,30. Digite o valor do desvio padrão que você quer usar.')
    pesofinal = peso + dp
    st.text("o peso final ficou em : {:.2f} kilos".format(pesofinal))


elif estimativa == 'Estimativa de Peso' and genero == 'Homem' and cor == 'Negra' and idade >= 60:

    peso = (aj * 0.44) + (cb * 2.86) - 39.21
    st.text('o peso estimado do paciente é {:.2f} kilos '.format(peso))

    dp = st.number_input('Para este caso o desvio padrão é de +- 07,04. Digite o valor do desvio padrão que você quer usar.')
    pesofinal = peso + dp
    st.text("o peso final ficou em : {:.2f} kilos".format(pesofinal))




elif estimativa == 'Estimativa de Altura' and genero == 'Mulher' and cor == 'Branca' and idade < 60:

    estatura = 70.25 + (1.87 * aj) - (0.06 * idade) /100
    st.text('A estatura do paciente é de {:.2f} metros'.format(estatura))

    dp = st.number_input('Para este caso o desvio padrão é de +- 07,20. Digite o valor do desvio padrão que você quer usar.')
    estaturafinal = (estatura + dp)/100
    st.text("A estatura final ficou em : {:.2f} metros".format(estaturafinal))


elif estimativa == 'Estimativa de Altura' and genero == 'Mulher' and cor == 'Branca'and idade >= 60:

    estatura = 75.00 + (1.91 * aj) - (0.17 * idade)/100
    st.text('A estatura do paciente é de {:.2f} metros'.format(estatura))

    dp = st.number_input('Para este caso o desvio padrão é de +- 08,32. Digite o valor do desvio padrão que você quer usar.')
    estaturafinal = (estatura + dp) /100
    st.text("A estatura final ficou em : {:.2f} metros".format(estaturafinal))


elif estimativa == 'Estimativa de Altura' and genero == 'Mulher' and cor == 'Negra' and idade < 60:

    estatura = 68.10 + (1.86 * aj) - (0.06 * idade) /100
    st.text('A estatura do paciente é de {:.2f} metros'.format(estatura))

    dp = st.number_input('Para este caso o desvio padrão é de +- 07,60. Digite o valor do desvio padrão que você quer usar.')
    estaturafinal = (estatura + dp) /100
    st.text("A estatura final ficou em : {:.2f} metros".format(estaturafinal))


elif estimativa == 'Estimativa de Altura' and genero == 'Mulher' and cor == 'Negra' and idade >= 60:

    estatura = 58.72 + (1.96 * aj) /100
    st.text('A estatura do paciente é de {:.2f} metros'.format(estatura))

    dp = st.number_input('Para este caso o desvio padrão é de +- 08,26. Digite o valor do desvio padrão que você quer usar.')
    estaturafinal = (estatura + dp) /100
    st.text("A estatura final ficou em : {:.2f} metros".format(estaturafinal))


elif estimativa == 'Estimativa de Altura' and genero == 'Homem' and cor == 'Branca' and idade < 60:

    estatura = 71.85 + (1.87 * aj) /100
    st.text('A estatura do paciente é de {:.2f} metros'.format(estatura))

    dp = st.number_input('Para este caso o desvio padrão é de +- 07,94. Digite o valor do desvio padrão que você quer usar.')
    estaturafinal = (estatura + dp) /100
    st.text("A estatura final ficou em : {:.2f} metros".format(estaturafinal))


elif estimativa == 'Estimativa de Altura' and genero == 'Homem' and cor == 'Branca' and idade >= 60:

    estatura = 59.01 + (2.08 * aj) /100
    st.text('A estatura do paciente é de {:.2f} metros'.format(estatura))

    dp = st.number_input('Para este caso o desvio padrão é de +- 07,84. Digite o valor do desvio padrão que você quer usar.')
    estaturafinal = (estatura + dp)
    st.text("A estatura final ficou em : {:.2f} metros".format(estaturafinal))


elif estimativa == 'Estimativa de Altura' and genero == 'Homem' and cor == 'Negra' and idade < 60:

    estatura = 73.42 + (1.79 * aj) /100
    st.text('A estatura do paciente é de {:.2f} metros'.format(estatura))

    dp = st.number_input('Para este caso o desvio padrão é de +- 07,20. Digite o valor do desvio padrão que você quer usar.')
    estaturafinal = (estatura + dp) /100
    st.text("A estatura final ficou em : {:.2f} metros".format(estaturafinal))


elif estimativa == 'Estimativa de Altura' and genero == 'Homem' and cor == 'Negra' >= 60:

    estatura = 95.79 + (1.37 * aj) /100
    st.text('A estatura do paciente é de {:.2f} metros'.format(estatura))

    dp = st.number_input('Para este caso o desvio padrão é de +- 08,44. Digite o valor do desvio padrão que você quer usar.')
    estaturafinal = (estatura + dp) /100
    st.text("A estatura final ficou em : {:.2f} metros".format(estaturafinal))

else:
    st.warning('Erro, por favor verifique os valores colocados')
