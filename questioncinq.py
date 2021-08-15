class QuestionCinq:

    @staticmethod
    def moyenne_diag(M):
        """
        :param M: une matrice carrée de nombres décimaux
        :return: une liste à deux éléments contenant la moyenne des deux diagonales principales de la matrice
        """
        length = len(M)
        result = []
        total_diag1, total_diag2 = 0, 0

        for i in range(length):
            total_diag1 += M[i][i]
            total_diag2 += M[length - 1 - i][i]

        result.append(total_diag1 / length)
        result.append(total_diag2 / length)

        return result

    @staticmethod
    def is_local_maxima(M, x, y):

        voisins = [
            [x - 1, y - 1], [x - 1, y], [x - 1, y + 1],
            [x, y - 1], [x, y + 1],
            [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]
        ]

        for voisin in voisins:
            if M[x][y] < M[voisin[0]][voisin[1]]:
                return False

        return True

    @staticmethod
    def maxima(M):
        """
        :param M: une matrice carrée de nombres décimaux
        :return: la liste des coordonnées des éléments de la matrice qui sont des maxima locaux
        """
        length = len(M)
        result = []

        for i in range(1, length - 1):
            for j in range(1, length - 1):
                if QuestionCinq.is_local_maxima(M, i, j):
                    result.append([i, j])

        return result
