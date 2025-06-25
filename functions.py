# Funcão de exibição de membros da equipe
def mostrar_equipe():
    equipe = []
    quantidade = int(input("Quantos membros tem a equipe? "))

    for i in range(quantidade):
        nome = input(f"Digite o nome do membro {i + 1}: ")
        funcao = input(f"Digite a função de {nome}: ")
        equipe.append({"nome": nome, "funcao": funcao})
    print("\n--- Equipe do Projeto ---")
    for membro in equipe:
        print(f"{membro['nome']} - {membro['funcao']}")

# Função de adição de posts
def posts_blog():
    posts = []
    quantidade = int(input("Quantos posts deseja inserir? "))

    for i in range(quantidade):
        titulo = input(f"Digite o título do post {i + 1}: ")
        autor = input(f"Digite o nome do autor do post {i + 1}: ")
        data = input(f"Digite a data do post {i + 1} (dd/mm/aaaa): ")
        posts.append({"título": titulo, "autor": autor, "data": data})
    print("\n--- Posts do Blog ---")
    for post in posts:
        print(f"Título: {post['título']} | Autor: {post['autor']} | Data: {post['data']}")


mostrar_equipe()
posts_blog()
