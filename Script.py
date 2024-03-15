def Talesv1():
           while True:
                print('''
                                 a        c
                                ----    -----
                                 b        d    ''')
                pergunta=str(input('Aonde é o x?: ').upper())
                # se X está na posicao a
                print('='*50)
                if pergunta=='A':
                    a='x'
                    b=int(input('Digite o valor B: '))
                    c=int(input('Digite o valor C:'))
                    d=int(input('Digite o valor D: '))
                    print()
                    # mostrar o calculo
                    print(f'''
                                {a}       {c}
                                -----    ------
                                {b}       {d}
                                                ''')
                    

                    # calculo
                    multiplicacao1=a*d
                    multiplicacao2=b*c
                    print(f'{d}{a} = {multiplicacao2}')
                    print(f'{a} = {multiplicacao2} / {d}')
                    print(f'{a} = {multiplicacao2/d}')
                if pergunta=='B':
                    a=int(input('Digite o valor A: '))
                    b='x'
                    c=int(input('Digite o valor C:'))
                    d=int(input('Digite o valor D: '))
                    print()
                    # mostrar o calculo
                    print(f'''
                                {a}       {c}
                                -----    ------
                                {b}       {d}
                                                ''')
                    

                    # calculo
                    multiplicacao1=c*b
                    multiplicacao2=a*d
                    print(f'{c}{b}= {multiplicacao2}')
                    print(f'{b} = {multiplicacao2} / {c}')
                    print(f'{b} = {multiplicacao2/c}')
                if pergunta=='C':
                    a=int(input('Digite o valor A: '))
                    b=int(input('Digite o valor B: '))
                    c='x'
                    d=int(input('Digite o valor D: '))
                    print()
                    # mostrar o calculo
                    print(f'''
                                {a}       {c}
                                -----    ------
                                {b}       {d}
                                                ''')
                    

                    # calculo
                    multiplicacao1=0
                    multiplicacao2=a*d
                    print(f'{b}{c}= {multiplicacao2}')
                    print(f'{c} = {multiplicacao2} / {b}')
                    print(f'{c} = {multiplicacao2/b}')
                if pergunta=='D':
                    a=int(input('Digite o valor A: '))
                    b=int(input('Digite o valor B: '))
                    c=int(input('Digite o valor C:'))
                    d='X'
                    print()
                    # mostrar o calculo
                    print(f'''
                                {a}       {c}
                                -----    ------
                                {b}       {d}
                                                ''')
                    

                    # calculo
                    multiplicacao1=d*a
                    multiplicacao2=b*c
                    print(f'{a}{d}= {multiplicacao2}')
                    print(f'{d} = {multiplicacao2} / {a}')
                    print(f'{d} = {multiplicacao2/a}')
                while True:
                    conti=str(input('Quer continuar?[S/N]')).upper()
                    if conti in "SN":
                        break
                if conti=='N':
                    break        
def Talesv2():
        while True:
            print(f''' 
                                     a       c
                                    ----    -----
                                     b        d               
                  ''')
            resposta=str(input('Aonde está o X?: ')).upper()
            if resposta=='A':
                a=int(input('Digite o valor de A: X+ '))
                b=int(input('Digite o valor de B: '))
                c=int(input('Qual o valor de C:'))
                d=int(input('Qual o valor de D: '))
                # formula
                print(f'''
                                {a}       {c}
                                -----    ------
                                {b}       {d}
                                                ''')
                
                # calculo
                calculo1=c*b
                calculo2=calculo1/d
                print(f'{d}.(X+{a}) = {calculo1}')
                print(f'X+{a} = {calculo1} / {d}')
                print(f'X+{a} = {calculo2}')
                print(f'X = {calculo2} - {a}')
                print(f'X = {calculo2-a}')
            if resposta=='B':
                a=int(input('Digite o valor de A: '))
                b=int(input('Digite o valor de B: X+'))
                c=int(input('Qual o valor de C:'))
                d=int(input('Qual o valor de D: '))
                # formula
                print(f'''
                                {a}       {c}
                                -----    ------
                                {b}       {d}
                                                ''')
                # calculo
                calculo1=a*d
                calculo2=calculo1/c
                print(f'{c}.(X+{b}) = {calculo1}')
                print(f'X+{b} = {calculo1} / {c}')
                print(f'X+{b} = {calculo2}')
                print(f'X = {calculo2} - {b}')
                print(f'X = {calculo2-b}')
            if resposta=='C':
                a=int(input('Digite o valor de A: '))
                b=(int(input('Digite o valor de B: ')))
                c=(int(input('Qual o valor de C: X+')))
                d=int(input('Qual o valor de D: '))
                # formula
                print(f'''
                                {a}       {c}
                                -----    ------
                                {b}       {d}
                                                ''')
                # calculo
                calculo1=a*d
                calculo2=calculo1/b
                print(f'{b}.(X+{c}) = {calculo1}')
                print(f'X+{c} = {calculo1}/{b}')
                print(f'X+{c} = {calculo2}')
                print(f'X = {calculo2} - {c}')
                print(f'X = {calculo2-c}')
            if resposta=='D':
                a=int(input('Digite o valor de A: '))
                b=(int(input('Digite o valor de B: ')))
                c=(int(input('Qual o valor de C: ')))
                d=int(input('Qual o valor de D: X+ '))
                # formula
                print(f'''                 {a}        {c}
                            ----    -----
                            {b}        {d}''')
                # formula
                print(f'''
                                {a}       {c}
                                -----    ------
                                {b}       {d}
                                                ''')
                # calculo
                calculo1=b*c
                calculo2=calculo1/a
                print(f'{a}.(X+{d}) = {calculo1}')
                print(f'X+{d} = {calculo1}/{a}')
                print(f'X+{d} = {calculo2}')
                print(f'X = {calculo2} - {d}')
                print(f'X = {calculo2-d}')
            while True:
                    conti=str(input('Quer continuar?[S/N]')).upper()
                    if conti in "SN":
                        break
            if conti=='N':
                break      
while True:
    print(''' exemplo 1:
                                10     2
                                -----  -----  
                                4       X   
        ''')
    print(''' exemplo 2:
                            4      X+2  
                            -----  -----      
                            2       6           
        ''')
    calculo=int(input('Qual a forma do calculo?: [1/2] '))
    if calculo==2:
        Talesv2()
    if calculo==1:
        Talesv1()
    while True:
         resp=str(input('Sair do Script?[S/N]')).upper()
         if resp in 'SN':
              break
    if resp=='S':
        break
print('\033[31mVolte sempre\033[m')
print('\033[32m\033[1mScript By: AnarK Death\033[m')