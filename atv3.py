
import locale 
 
try: 
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') 
except: 
    try: 
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252') 
    except:  
        def formatar_real_alternativo(valor): 
            return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") 
        formatar_real = formatar_real_alternativo 
    else: 
        def formatar_real(valor): 
            return locale.currency(valor, grouping=True, symbol='R$ ').replace('R$ ', '').strip() 
else: 
    def formatar_real(valor): 
        return locale.currency(valor, grouping=True, symbol='R$ ') 
 
print("=" * 50) 
print("         SISTEMA DE VENDAS") 
print("=" * 50) 
 
nome_cliente = input("Nome do comprador: ") 
produto = input("Nome do item: ") 
preco = float(input("Valor unitario (R$): ")) 
quantidade = int(input("Numero de unidades: ")) 
percentual_desconto = float(input("Desconto aplicado (%): ")) 
 
subtotal = preco * quantidade 
valor_desconto = subtotal * (percentual_desconto / 100) 
total_final = subtotal - valor_desconto 
valor_medio = total_final / quantidade 
 
print("\n" + "=" * 50) 
print("         RESUMO DA VENDA") 
print("=" * 50) 
 
print(f"Comprador:        {nome_cliente}") 
print(f"Item:             {produto}") 
print(f"Unidades:         {quantidade} unidade(s)") 
print(f"Valor unitario:   R$ {formatar_real(preco)}") 
print("-" * 50) 
print(f"Valor inicial:    R$ {formatar_real(subtotal)}") 
print(f"Desconto:         {percentual_desconto:.0f}% (R$ {formatar_real(valor_desconto)})") 
print("-" * 50) 
print(f"VALOR FINAL:      R$ {formatar_real(total_final)}") 
print(f"\nCusto medio por unidade: R$ {formatar_real(valor_medio)}") 
 
print("\n" + "=" * 50) 
print("          VENDA REALIZADA COM SUCESSO!") 
print("=" * 50) 
 
print("Conferindo informacoes", end="... ") 
print("Concluido!", end="\n\n")

