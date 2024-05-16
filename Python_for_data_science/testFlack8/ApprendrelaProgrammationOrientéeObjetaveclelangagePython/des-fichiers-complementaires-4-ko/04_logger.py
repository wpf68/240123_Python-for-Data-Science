class Logger:
    def __init__(self):
        # Ouverture du fichier en écriture
        self.log_file = open("log.txt", "w")
        # Initialisation du compteur de logs
        self.log_count = 0
        # Écriture de la première ligne
        self.log_file.write("--Début log--\n")


    def __del__(self):
        # Destruction de l'instance : on écrit la dernière ligne du
        # fichier
        self.log_file.write("--Fin log: {} log(s)--\n".format(self.log_count))
        # Fermeture propre du fichier
        self.log_file.close()

    def log(self, message):
        # Écriture du message passé en paramètre
        self.log_file.write("{}\n".format(message))
        # Incrémentation du compteur de logs
        self.log_count += 1


class Test:
    def __init__(self):
        self.logger = Logger()

    def appel(self, message):
        self.logger.log(message)

test = Test()
for i in range(1, 6):
    if i == 1:
        test.appel("1er appel")
    else:
        test.appel("{}ème appel".format(string))

# $> cat log.txt
# --Début log--
# 1ème appel
# 2ème appel
# 3ème appel
# 4ème appel
# 5ème appel
# --Fin log: 5 log(s)--
