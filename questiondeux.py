from math import sqrt


class QuestionDeux:

    @staticmethod
    def trajectoire(array):
        """
        :param array: une matrice à 2 dimensions remplies de 0 ou de 1
        :return: un float correspondant à la distance parcourue
        """
        row_length = len(array)
        col_length = len(array[0])
        ligne, diagonale, row, col = 0, 0, 0, 0

        # On récupère l'ordonnée du premier "1" pour obtenir le point de départ
        for i in range(row_length):
            if array[i][col] == 1:
                row = i

        # On cherche le point adjacent contenant un "1" à partir de ce point de départ
        # On réitère cette recherche avec le nouveau point trouvé jusqu'à la fin du tableau
        while col < col_length - 1:
            if (row > 0) and (array[row - 1][col + 1] == 1):
                diagonale += 1
                row -= 1
                col += 1
            if array[row][col + 1] == 1:
                ligne += 1
                col += 1
            if (row < row_length - 1) and (array[row + 1][col + 1] == 1):
                diagonale += 1
                row += 1
                col += 1

        # Affichage des résultats
        print("Nombre de déplacements en ligne: ", ligne)
        print("Nombre de déplacements en diagonale: ", diagonale)

        return sqrt(2) * diagonale + ligne
