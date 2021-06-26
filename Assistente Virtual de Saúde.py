# A proposta aqui é desenvolver um código de interação social com o objetivo de realizar uma triagem de pessoas com possíveis  problemas emocionais.

print('\33[34mBom dia!\33[m \n    Vamos conversar?\n    Eu me chamo \33[34mFay!\33[m')  # Por meio de uma abordagem humanizada, tentaremos fazer a pessoa se sentir mais a vontade para conversar.
nome = str(input('Qual o seu nome? : '))
print('\33[34m Você tem um belo nome \33[32m{}\33[m, \33[34mé um prazer te conhecer!!\33[m'.format(nome))
ps = str(input('Como você está se sentindo hoje? '))
if ps == 'um pouco triste' or ps == 'preocupado' or ps == 'muito cansado': #O objetivo aqui é tentar descobrir como o usuário está se sentindo neste dia.
    print('  \33[34mEu lamento que esteja se sentindo assim!\33[m')
    aj = str(input('  \33[34mEu gostaria muito de lhe ajudar! \n  \33[32m{}!\33[m\n \33[33mVocê gostaria de conversar com alguém amigável que vai lhe ouvir com atenção e tantar lhe ajudar?\33[m   '.format(nome)))
    if aj == 'sim':
     print('    \33[34mExelente, vou chamar uma grande amiga para falar pessoamente com você!\33[m') #aqui tentaremos direcionar o usuário para um profissonal da área.
    elif aj == 'não':
     print('     \33[34mTudo bem eu entendo, mas se precisar estarei aqui!\33[m')
else:
    print('Tudo bem eu entendo!')
print('\33[30;43mTenha um otimo dia!! {}\33[m'.format(nome))
