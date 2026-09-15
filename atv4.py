1615
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade não pode ser negativa. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro para a idade.")


while True:
    resposta = input("Você possui autorização? (Digite 'sim' ou 'nao'): ").strip().lower()
    if resposta in ['sim', 's', 'yes', 'y']:
        tem_autorizacao = True
        break
    elif resposta in ['nao', 'não', 'n', 'no']:
        tem_autorizacao = False
        break
    else:
        print("Resposta inválida! Digite 'sim' ou 'nao'.")



if idade < 12:

    mensagem = "Acesso não permitido"
    status = "negado"
    
elif idade >= 12 and tem_autorizacao:

    mensagem = "Entrada liberada"
    status = "permitido"
    
else:

    mensagem = "Apresente uma autorização"
    status = "pendente"



print("\n" + "=" * 50)
print("           RESULTADO DA CLASSIFICAÇÃO")
print("=" * 50)


print(f"Idade informada:        {idade} anos")
print(f"Possui autorização:     {'Sim' if tem_autorizacao else 'Não'}")
print("-" * 50)

print(f"Status:                 {mensagem.upper()}")


if status == "negado":
    print("Motivo: Idade mínima para entrada é 12 anos.")
elif status == "permitido":
    print("Motivo: Idade e autorização verificadas com sucesso.")
else:
    print("Motivo: É necessário apresentar uma autorização para entrar.")

print("=" * 50)


print("\n[TESTES RÁPIDOS]")
print("-" * 50)

print("Caso 1 - Idade: 11, Autorização: Não")
if 11 < 12:
    print("  Resultado: Acesso não permitido ✓")
else:
    print("  Resultado: ERRO no teste!")

print("Caso 2 - Idade: 15, Autorização: Sim")
if 15 >= 12 and True:
    print("  Resultado: Entrada liberada ✓")
else:
    print("  Resultado: ERRO no teste!")


print("Caso 3 - Idade: 14, Autorização: Não")
if 14 >= 12 and False:
    print("  Resultado: ERRO no teste!")
else:
    print("  Resultado: Apresente uma autorização ✓")

print("-" * 50)



print("\n[EXPLICAÇÃO DA ESTRUTURA DE SELEÇÃO]")
print("-" * 50)
print("A estrutura if-elif-else organiza as três saídas da seguinte forma:")
print()
print("  1. if idade < 12:")
print("     → Captura todos os menores de idade (qualquer status de autorização)")
print()
print("  2. elif idade >= 12 and tem_autorizacao:")
print("     → Captura apenas as pessoas com idade suficiente E autorização")
print()
print("  3. else:")
print("     → Captura o caso restante: pessoas com idade suficiente SEM autorização")
print()
print("Vantagens desta abordagem:")
print("  - Cobertura completa de todos os casos possíveis")
print("  - Código limpo e legível")
print("  - Fácil manutenção e expansão futura")
print("-" * 50)
