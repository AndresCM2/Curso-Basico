def run():
    poblacion_paises = {
      'Argentina' : 44938712,
      'llave2' : 210147125,
      'llave3' : 503724424,
    }

    for paises, poblacion in poblacion_paises.items():
        print("La llave: '" + paises + "' contiene la cantidad" + str(poblacion))

if __name__=="__main__":
    run()