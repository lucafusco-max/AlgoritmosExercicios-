
titulo = "Cálculo na loja de roupas" 
descricao = "Um cliente comprou duas camisetas, cada uma por: " 
cont = " e recebeu um desconto de: " 
pergunta = "Quanto ele pagou?" 
resposta = "Ele pagou: " 
preco = 40.00 
quantidade = 2 
desconto = 15.00 
 
subtotal = preco * quantidade 
valor_final = subtotal - desconto 
 
print(f""" 
{titulo} 
{descricao}R$ {preco:.2f}{cont}R$ {desconto:.2f} 
{pergunta} 
{resposta}R$ {valor_final:.2f} 
""") 
