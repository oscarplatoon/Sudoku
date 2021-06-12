import unittest
from sudoku import SudokuSolver

class SudokuSolverTest(unittest.TestCase):

    def test_solution(self):
        my_test_solver = SudokuSolver('003020600900305001001806400008102900700000008006708200002609500800203009005010300')
        my_test_solver.solve()
        solution_string = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
        solution = [int(i) for i in solution_string]
        self.assertEqual(my_test_solver.board, solution)

    def test_solution2(self):
        my_test_solver = SudokuSolver('050083017000100400304005608000030009090824500006000070009000050007290086103607204')
        my_test_solver.solve()
        solution_string = '652483917978162435314975628825736149791824563436519872269348751547291386183657294'
        solution = [int(i) for i in solution_string]
        self.assertEqual(my_test_solver.board, solution)

    def test_solution3(self):
        my_test_solver = SudokuSolver('206030000001065070047108050500000029008019406000420001000042800609300005070000013')
        my_test_solver.solve()
        solution_string = '256734198891265374347198652514683729728519436963427581135942867689371245472856913'
        solution = [int(i) for i in solution_string]
        self.assertEqual(my_test_solver.board, solution)

    def test_solution4(self):
        my_test_solver = SudokuSolver('004502178100090030000800004600450000070900012801203500400000009350060807090300620')
        my_test_solver.solve()
        solution_string = '964532178187694235235817964629451783573986412841273596416728359352169847798345621'
        solution = [int(i) for i in solution_string]
        self.assertEqual(my_test_solver.board, solution)

if __name__ == '__main__':
    unittest.main()
