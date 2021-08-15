class QuestionQuatre:

    @staticmethod
    def nombreVoisinsVivants(etatActuel, x, y):

        row_length = len(etatActuel)
        col_length = len(etatActuel[0])
        nb_cellules_vivantes = 0

        voisins = [
            [x - 1, y - 1], [x - 1, y], [x - 1, y + 1],
            [x, y - 1], [x, y + 1],
            [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]
        ]

        if row_length - 1 > x and col_length - 1 > y:
            for i in voisins:
                if etatActuel[i[0]][i[1]] == 1:
                    nb_cellules_vivantes += 1

        return nb_cellules_vivantes

    @staticmethod
    def etatSuivant(etatActuel):

        row_length = len(etatActuel)
        col_length = len(etatActuel[0])
        result = [[0 for x in range(col_length)] for y in range(row_length)]

        for i in range(1, row_length - 1):
            for j in range(1, col_length - 1):
                if etatActuel[i][j] == 1:
                    nb_cellules_vivantes = QuestionQuatre.nombreVoisinsVivants(etatActuel, i, j)
                    if nb_cellules_vivantes == 2 or nb_cellules_vivantes == 3:
                        result[i][j] = 1
                elif etatActuel[i][j] == 0:
                    nb_cellules_vivantes = QuestionQuatre.nombreVoisinsVivants(etatActuel, i, j)
                    if nb_cellules_vivantes == 3:
                        result[i][j] = 1

        return result
