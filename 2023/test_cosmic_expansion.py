from unittest import TestCase, main

from day_11_cosmic_expansion import *

with open("data/11_sample.txt") as f:
    data_sample = f.readlines()
    data_sample = [d.strip("\n") for d in data_sample]
    print("sample start")
    helper_viz_sky(data_sample)


class TestCosmicExpansion(TestCase):
    def test_cosmic_expansion_is_rendered_correctly(self):
        actual = expand_cosmic_sky(data_sample)

        print("expanded sky")
        helper_viz_sky(actual)

        self.assertEqual(actual[3], ".............")
        self.assertEqual(actual[4], ".............")
        self.assertEqual(actual[-1], "#....#.......")

        col_2 = "".join([row[2] for row in actual])
        col_3 = "".join([row[3] for row in actual])
        self.assertEqual(col_2, "............")
        self.assertEqual(col_3, "............")

    def test_galaxy_index_is_correct(self):
        actual = create_galaxy_index(expand_cosmic_sky(data_sample))
        self.assertTupleEqual(actual["1"], (0, 4))
        self.assertTupleEqual(actual["2"], (1, 9))
        self.assertTupleEqual(actual["8"], (11, 0))
        self.assertTupleEqual(actual["9"], (11, 5))

    def test_distance_to_galaxy_is_counted_correctly(self):
        galaxy_index = create_galaxy_index(expand_cosmic_sky(data_sample))
        five_to_nine = count_distance_between_galaxies(
            galaxy_index["5"], galaxy_index["9"]
        )
        self.assertEqual(five_to_nine, 9)
        one_to_seven = count_distance_between_galaxies(
            galaxy_index["1"], galaxy_index["7"]
        )
        self.assertEqual(one_to_seven, 15)
        three_to_six = count_distance_between_galaxies(
            galaxy_index["3"], galaxy_index["6"]
        )
        self.assertEqual(three_to_six, 17)
        eight_to_nine = count_distance_between_galaxies(
            galaxy_index["8"], galaxy_index["9"]
        )
        self.assertEqual(eight_to_nine, 5)

    def test_solve_part_1(self):
        actual = solve_part_1(data_sample)
        self.assertEqual(actual, 374)

    def test_find_empty_spaces(self):
        actual = find_empty_spaces_in_sky(data_sample)
        self.assertEqual(actual[0], [3, 7])
        self.assertEqual(actual[1], [2, 5, 8])

    def test_custom_galaxy_expander(self):
        actual_ten = custom_galaxy_expansion_counter(data_sample, 10)
        actual_hundred = custom_galaxy_expansion_counter(data_sample, 100)

        self.assertEqual(actual_ten, 1030)
        self.assertEqual(actual_hundred, 8410)


if __name__ == "__main__":
    main()
