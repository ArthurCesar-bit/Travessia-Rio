# Função para mostrar a situação atual de todos os personagens
def mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro):
    print(f"Pai: {pai} | Mãe: {mae} | Filho1: {filho1} | Filho2: {filho2} | "
          f"Filha1: {filha1} | Filha2: {filha2} | Policial: {policial} | Prisioneiro: {prisioneiro}")

# Função principal para simular a travessia
def travessia():
    # Inicializando todos os personagens no lado 1 (lado inicial)
    pai = mae = filho1 = filho2 = filha1 = filha2 = policial = prisioneiro = 1

    # Mostra a situação inicial
    print("Iniciando a travessia...\n")
    mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
    
    # Processo de travessia
    while pai == 1 or mae == 1 or filho1 == 1 or filho2 == 1 or filha1 == 1 or filha2 == 1 or policial == 1:
        # O policial leva o prisioneiro
        if policial == 1 and prisioneiro == 1:
            policial = 0
            prisioneiro = 0
            print("\nPolicial e prisioneiro atravessam juntos.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)

        # O policial volta sozinho
        if policial == 0:
            policial = 1
            print("\nPolicial volta sozinho.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)

        # O policial leva filho 1
        if policial == 1 and filho1 == 1:
            policial = 0
            filho1 = 0
            print("\nPolicial e Filho 1 atravessam juntos.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)

        # Policial volta com o prisioneiro
        if policial == 0 and prisioneiro == 0:
            policial = 1
            prisioneiro = 1
            print("\nPolicial e Prisioneiro voltam.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
        
        # Pai leva filho 2
        if pai == 1 and filho2 == 1:
            pai = 0
            filho2 = 0
            print("\nPai e Filho 2 atravessam juntos.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
        
        # Pai volta sozinho
        if pai == 0:
            pai = 1
            print("\nPai volta sozinho.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)

        # Pai leva a mãe
        if pai == 1 and mae == 1:
            pai = 0
            mae = 0
            print("\nPai e Mãe atravessam juntos.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
        
        # Mãe volta sozinha
        if mae == 0:
            mae = 1
            print("\nMãe volta sozinha.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)

        # Policial leva prisioneiro
        if policial == 1 and prisioneiro == 1:
            policial = 0
            prisioneiro = 0
            print("\nPolicial e Prisioneiro atravessam juntos.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
        
        # Pai volta sozinho
        if pai == 0:
            pai = 1
            print("\nPai volta sozinho.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
        
        # Pai e mãe atravessam
        if pai == 1 and mae == 1:
            pai = 0
            mae = 0
            print("\nPai e Mãe atravessam juntos.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)

        # Mãe volta sozinha
        if mae == 0:
            mae = 1
            print("\nMãe volta sozinha.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)

        # Mãe e Filha 1 atravessam
        if mae == 1 and filha1 == 1:
            mae = 0
            filha1 = 0
            print("\nMãe e Filha 1 atravessam juntas")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
        
        # Policial e Prisioneiro voltam
        if policial == 0 and prisioneiro == 0:
            policial = 1
            prisioneiro = 1
            print("\nPolicial e Prisioneiro voltam juntos.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)

        # Policial e Filha 2 atravessam
        if policial == 1 and filha2 == 1:
            policial = 0
            filha2 = 0
            print("\nPolicial e Filha 2 atravessam juntos.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
        
        # Policial volta sozinho
        if policial == 0:
            policial = 1
            print("\nPolicial volta sozinho.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
        
        # Policial e prisioneiro voltam
        if policial == 1 and prisioneiro == 1:
            policial = 0
            prisioneiro = 0
            print("\nPolicial e Prisioneiro atravessan juntos.")
            mostrar_situacao(pai, mae, filho1, filho2, filha1, filha2, policial, prisioneiro)
        
        # Caso final: se todos estiverem do lado 2 (lado final)
        if (pai == 0 and mae == 0 and filho1 == 0 and filho2 == 0 and 
            filha1 == 0 and filha2 == 0 and policial == 0 and prisioneiro == 0):
            print("\nTodos atravessaram com sucesso!")
            break

# Chama a função de travessia
travessia()