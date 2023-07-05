

saldo = 0
extrato = [[], []]
extrato_crono = []

limite_do_saque = 500.00
numero_de_saques = 0
maximo_de_saques = 3
ligado = True
erro = 0

while ligado:

   operacao = input(f"""

                 Bem vindo ao Big bank.
                 Estamos aqui para atendê-lo.
                 Digite:

                 D para depósito.
                 S para saque.
                 E para extrato.
                 Ou A para dar adeus.\nResposta: """)

   if operacao.upper() == "D":
      deposito = float(input("Você escolheu Depósito. Digite o valor desejado:\n"))
      if deposito > 0:
            saldo += deposito
            extrato[0].append(f"R$ {deposito:.2f}")
            extrato_crono.append(f"R$ {deposito:.2f}")
            print(f"""

                  O depósito de R$ {deposito:.2f} foi efetuado com sucesso.

                  """)
      else: print(f"""

                  Infelizmente o valor é inválido.

                  """)

   elif operacao.upper() == "S":
      saque = float(input("Você escolheu Saque. Digite o valor desejado:\n"))
      if saque > saldo:
            print(f"""

            Sentimos muito, mas no momento o valor do saldo é insuficiente.

            """)
      elif saque <= saldo:
         if saque > limite_do_saque:
                print(f"""

                Sentimos muito, mas o valor solicitado excede o valor máximo permitido em um único saque.

                """)
         elif saque <= limite_do_saque:
               if numero_de_saques == maximo_de_saques:
                    print(f"""

                    Foram executados os três saques diários gratuitos.
                    Mas não se preocupe, entre em contato com a
                    central de atendimento pelo 0800800008 ou via
                    chat, nossa equipe certamente irá encontrar a
                    melhor solução. Pense grande, seja Big.

                    """)
               else:
                    numero_de_saques += 1
                    saldo -= saque
                    extrato[1].append(f"R$ {saque:.2f}")
                    extrato_crono.append(f"R$ {-saque:.2f}")
                    print(f"""

                     O saque de R$ {saque:.2f} foi efetuado com sucesso.

                     """)

   elif operacao.upper() == "E":
      print(f"""

              Você escolheu Extrato.

              Os depósitos recebidos são de:

               {", ".join(extrato[0])}

              --|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--

              Os saques efetuados são de:

               {", ".join(extrato[1])}

              --|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--

              As transações efetuadas, em ordem cronológica:

               {", ".join(extrato_crono)}

              --|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--#--|--

              Seu saldo atual é: R$ {saldo:.2f}

              """)

   elif operacao.upper() == "A":
        print(f"""

              Você escolheu dar Adeus. Mas esperamos que seja um até logo,
              estaremos aqui sempre que precisar.

              """)
        break

   else:
      print(f"""

            Desculpe, ocorreu algum erro.
            Por favor,vamos tentar novamente.

            """)

      erro += 1
      if erro == 3:
          print(f"""

                Perdão, o erro continua se repetindo.
                Aguarde um pouco e, ao tentar novamente, verifique se está escolhendo entre as opções:
                D para depósito
                S para saque
                E para extrato
                A para dar adeus.

                """)
          operacao = "A"





