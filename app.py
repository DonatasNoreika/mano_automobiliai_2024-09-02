from garazas import Garazas

garazas = Garazas()

if __name__ == "__main__":
    while True:
        veiksmas = int(input("1 - įvesti automobilį\n2 - įvesti elektromobilį\n3 - peržiūrėti\n0 - išeiti\n"))
        match veiksmas:
            case 1:
                garazas.prideti_auto()
            case 2:
                garazas.prideti_elektromobili()
            case 3:
                garazas.atvaizduoti_auto()
            case 0:
                break
