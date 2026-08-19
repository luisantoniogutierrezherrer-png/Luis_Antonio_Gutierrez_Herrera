print("Buscador de información rápida")
opcion = input("Escribe el nombre de un artista, película o serie: ").strip().lower()

match opcion:
    case "interstellar":
        print("Interstellar: película de ciencia ficción dirigida por Christopher Nolan sobre viajes en el tiempo.")
    
    case "breaking bad":
        print("Breaking Bad: Serie de televisión sobre un profesor de química que decide producir metanfetaminas.")
    
    case "daft punk":
        print("Daft Punk: Dúo francés de música electrónica famoso por sus cascos robóticos y éxitos globales.")
    
    case "shrek":
        print("Shrek: Película animada sobre un ogro que rescata a una princesa para recuperar su pantano.")
    
    case _:
        print("Lo siento, no tengo información sobre esa selección en la base de datos.")