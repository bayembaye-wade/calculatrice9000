class Calculatrice:
    def __init__(self):
        self.historique = []

    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Division par zéro")

    def afficher_historique(self):
        if not self.historique:
            print("Historique vide.")
        else:
            print("Historique des opérations :")
            for operation in self.historique:
                print(operation)

    def effacer_historique(self):
        self.historique = []
        print("Historique effacé.")

    def calculatrice(self):
        while True:
            try:
                # Demander à l'utilisateur de saisir une expression mathématique
                expression = input("Entrez une expression mathématique ou 'q' pour quitter : ")

                # Quitter si l'utilisateur le souhaite
                if expression.lower() == 'q':
                    break

                # Évaluer l'expression et ajouter le résultat à l'historique
                resultat = eval(expression)
                print(f"Le résultat de l'expression {expression} est : {resultat}")

                # Ajouter l'expression à l'historique
                self.historique.append(f"{expression} = {resultat}")

            except (ValueError, ZeroDivisionError, SyntaxError) as e:
                print(f"Erreur : {e}")
            except Exception as e:
                print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
calculatrice = Calculatrice()
calculatrice.calculatrice()

# Afficher l'historique
calculatrice.afficher_historique()

# Effacer l'historique
calculatrice.effacer_historique()