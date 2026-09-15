

def verificar_aprovacao():
 
    print("\n=== VERIFICACAO DE APROVACAO ===")
    
    nota = float(input("Digite a nota do participante (0 a 100): "))
    frequencia = float(input("Digite a frequencia do participante (0 a 100): "))
    
    print(f"Nota: {nota} - Frequencia: {frequencia}%")
    
    if frequencia >= 80:
        print("Frequencia OK")
        if nota >= 70:
            print("RESULTADO: APROVADO - Nota e frequencia suficientes")
        else:
            print(f"RESULTADO: REPROVADO - Frequencia OK, mas nota {nota} abaixo de 70")
    else:
        print(f"RESULTADO: REPROVADO - Frequencia {frequencia}% abaixo de 80%")


def classificar_nota():
    print("\n=== CLASSIFICACAO DE NOTA ===")
    
    nota = float(input("Digite a nota para classificar (0 a 100): "))
    
    print(f"Nota: {nota}")
    
    if nota >= 90:
        classificacao = "EXCELENTE"
    elif nota >= 70:
        classificacao = "BOM"
    elif nota >= 50:
        classificacao = "REGULAR"
    elif nota >= 30:
        classificacao = "RUIM"
    else:
        classificacao = "PESSIMO"
    
    print(f"CLASSIFICACAO: {classificacao}")



def processar_menu():
   

    print("\n=== PROCESSADOR DE MENU ===")
    print("1 - Listar cursos")
    print("2 - Cadastrar participante")
    print("3 - Calcular resultado")
    print("4 - Sair do sistema")
    
    opcao = input("Digite a opcao desejada: ")
    
    match opcao:
        case "1":
            print("OPCAO 1: Listar cursos")
        
        case "2":
            print("OPCAO 2: Cadastrar participante")
        
        case "3":
            print("OPCAO 3: Calcular resultado")
        
        case "4" | "sair":
            print("OPCAO 4: Sair do sistema")
        

        case _:
            print(f"OPCAO INVALIDA: {opcao}")


def avaliar_aluno():

  
    print("\n=== AVALIACAO DO PARTICIPANTE ===")

    nome = input("Digite o nome do participante: ")
    nota = float(input("Digite a nota do participante (0 a 100): "))
    faltas = int(input("Digite o numero de faltas: "))
    
    print(f"Participante: {nome} - Nota: {nota} - Faltas: {faltas}")
    
    dados = (nota, faltas)
    
    match dados:
 
        case (n, _) if n >= 90:
            print(f"{nome}: PARTICIPANTE DESTAQUE - Nota {n}")
        
        case (n, f) if n >= 70 and f <= 8:
            print(f"{nome}: APROVADO - Nota {n}, Faltas {f}")
        
        case (n, f) if n >= 50 and f <= 8:
            print(f"{nome}: EM RECUPERACAO - Nota {n}, Faltas {f}")
        
        case (n, f) if n < 50 or f > 8:
            print(f"{nome}: REPROVADO - Nota {n}, Faltas {f}")
        

        case _:
            print(f"{nome}: SITUACAO INDEFINIDA")



def main():

    print("=" * 50)
    print("SISTEMA DE CURSOS SIMPLES")
    print("Demonstracao de estruturas de selecao")
    print("=" * 50)
    
    while True:
        print("\n" + "-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Verificar Aprovacao (Estrutura Aninhada)")
        print("2 - Classificar Nota (Estrutura ELIF)")
        print("3 - Processar Menu (Match Case)")
        print("4 - Avaliar Participante (Match Case com Guarda)")
        print("5 - Sair")
        
        opcao = input("\nEscolha uma opcao (1-5): ")
        
        if opcao == "1":
            verificar_aprovacao()
        
        elif opcao == "2":
            classificar_nota()
        
        elif opcao == "3":
            processar_menu()
        
        elif opcao == "4":
            avaliar_aluno()
        
        elif opcao == "5":
            print("\nSaindo do sistema...")
            break
        
        else:
            print("\nOPCAO INVALIDA! Tente novamente.")
        
 
        input("\nPressione Enter para continuar...")



def verificar_multiplos_alunos():

    print("\n=== VERIFICAR MULTIPLOS PARTICIPANTES ===")
    
    continuar = "s"
    while continuar.lower() == "s":
        print("\n" + "-" * 30)
        verificar_aprovacao()
        continuar = input("\nVerificar outro participante? (s/n): ")

def classificar_multiplas_notas():

    print("\n=== CLASSIFICAR MULTIPLAS NOTAS ===")
    
    continuar = "s"
    while continuar.lower() == "s":
        print("\n" + "-" * 30)
        classificar_nota()
        continuar = input("\nClassificar outra nota? (s/n): ")



def processar_lista_alunos():

    print("\n=== PROCESSAR LISTA DE PARTICIPANTES ===")
    
    alunos = []
    continuar = "s"
    

    while continuar.lower() == "s":
        print("\n" + "-" * 30)
        nome = input("Nome do participante: ")
        nota = float(input("Nota (0 a 100): "))
        faltas = int(input("Faltas: "))
        
        alunos.append({"nome": nome, "nota": nota, "faltas": faltas})
        continuar = input("Adicionar outro participante? (s/n): ")
    

    if alunos:
        print("\n" + "-" * 30)
        print("RESULTADOS:")
        print("-" * 30)
        
        for aluno in alunos:
            dados = (aluno["nota"], aluno["faltas"])
            
            match dados:
                case (n, _) if n >= 90:
                    status = f"{aluno['nome']}: PARTICIPANTE DESTAQUE - Nota {n}"
                case (n, f) if n >= 70 and f <= 8:
                    status = f"{aluno['nome']}: APROVADO - Nota {n}, Faltas {f}"
                case (n, f) if n >= 50 and f <= 8:
                    status = f"{aluno['nome']}: EM RECUPERACAO - Nota {n}, Faltas {f}"
                case (n, f) if n < 50 or f > 8:
                    status = f"{aluno['nome']}: REPROVADO - Nota {n}, Faltas {f}"
                case _:
                    status = f"{aluno['nome']}: SITUACAO INDEFINIDA"
            
            print(status)



def menu_avancado():
  
    
    print("=" * 50)
    print("SISTEMA DE CURSOS - MENU AVANCADO")
    print("=" * 50)
    
    while True:
        print("\n" + "-" * 50)
        print("OPCOES:")
        print("-" * 50)
        print("1 - Verificar Aprovacao (Aninhada)")
        print("2 - Classificar Nota (ELIF)")
        print("3 - Processar Menu Simples (Match Case)")
        print("4 - Avaliar Participante (Match Case + Guarda)")
        print("5 - Verificar Multiplos Participantes")
        print("6 - Classificar Multiplas Notas")
        print("7 - Processar Lista de Participantes")
        print("8 - Sair")
        
        opcao = input("\nEscolha uma opcao: ")
        
        match opcao:
            case "1":
                verificar_aprovacao()
            
            case "2":
                classificar_nota()
            
            case "3":
                processar_menu()
            
            case "4":
                avaliar_aluno()
            
            case "5":
                verificar_multiplos_alunos()
            
            case "6":
                classificar_multiplas_notas()
            
            case "7":
                processar_lista_alunos()
            
            case "8" | "sair":
                print("\nSaindo do sistema...")
                break
            
            case _:
                print("\nOPCAO INVALIDA! Tente novamente.")
        
        if opcao != "8":
            input("\nPressione Enter para continuar...")



def testar_rapido():

    print("\n=== TESTE RAPIDO ===")
    print("1 - Testar Aprovacao")
    print("2 - Testar Classificacao")
    print("3 - Testar Match Case")
    print("4 - Testar Guarda")
    
    opcao = input("Escolha um teste (1-4): ")
    
    if opcao == "1":
        verificar_aprovacao()
    elif opcao == "2":
        classificar_nota()
    elif opcao == "3":
        processar_menu()
    elif opcao == "4":
        avaliar_aluno()
    else:
        print("Opcao invalida!")


if __name__ == "__main__":
    print("=" * 50)
    print("SISTEMA DE CURSOS - VERSOES DISPONIVEIS")
    print("=" * 50)
    print("1 - Menu Interativo (Main)")
    print("2 - Menu Avancado com Match Case")
    print("3 - Teste Rapido")
    print("4 - Sair")
    
    versao = input("\nEscolha uma versao (1-4): ")
    
    if versao == "1":
        main()
    elif versao == "2":
        menu_avancado()
    elif versao == "3":
        testar_rapido()
    elif versao == "4":
        print("Saindo...")
    else:
        print("Opcao invalida!")
