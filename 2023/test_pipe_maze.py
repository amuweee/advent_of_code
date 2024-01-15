from unittest import TestCase, main

from day_10_pipe_maze import *

with open("data/10_sample.txt") as f:
    data_sample = f.readlines()

with open("data/10_sample_2.txt") as f:
    data_sample_2 = f.readlines()

with open("data/10_sample_3.txt") as f:
    data_sample_3 = f.readlines()

with open("data/10_sample_4.txt") as f:
    data_sample_4 = f.readlines()

# 7-F7- ..45.
# .FJ|7 .236.
# SJLL7 01.78
# |F--J 14567
# LJ.LJ 23...


class TestPipeMaze(TestCase):
    def test_data_is_mapped_correctly(self):
        actual = parse_map_to_2d_array(data_sample)
        self.assertListEqual(actual[0], ["7", "-", "F", "7", "-"])
        self.assertListEqual(actual[3], ["|", "F", "-", "-", "J"])

    def test_pipe_index_is_constructed_correctly(self):
        all_pipes = pipes_constructor(parse_map_to_2d_array(data_sample))
        pipe_index = convert_pipes_list_to_pipe_index(all_pipes)
        # .
        self.assertListEqual(pipe_index["1.0"].connected_pipes_pos, [])
        # S
        # self.assertListEqual(pipe_index["2.0"].connected_pipes_pos, ["3.0", "2.1"])
        # |
        self.assertListEqual(pipe_index["1.3"].connected_pipes_pos, ["0.3", "2.3"])
        # -
        self.assertListEqual(pipe_index["3.2"].connected_pipes_pos, ["3.3", "3.1"])
        # L
        self.assertListEqual(pipe_index["3.2"].connected_pipes_pos, ["3.3", "3.1"])
        # J
        self.assertListEqual(pipe_index["1.2"].connected_pipes_pos, ["0.2", "1.1"])
        # 7
        self.assertListEqual(pipe_index["2.4"].connected_pipes_pos, ["3.4", "2.3"])
        # F
        self.assertListEqual(pipe_index["3.1"].connected_pipes_pos, ["4.1", "3.2"])

    def test_distance_to_start_is_correct(self):
        all_pipes = pipes_constructor(parse_map_to_2d_array(data_sample))
        pipe_index = convert_pipes_list_to_pipe_index(all_pipes)
        pipe_index = add_distance_from_start(pipe_index)

        self.assertEqual(pipe_index["2.0"].distance, 0)
        self.assertEqual(pipe_index["4.0"].distance, 2)
        self.assertEqual(pipe_index["2.4"].distance, 8)
        self.assertEqual(pipe_index["3.4"].distance, 7)
        self.assertEqual(pipe_index["4.4"].distance, 0)

    def test_part_1(self):
        pipe_index = construct_pipes_with_distances(data_sample)
        actual = solve_part_1(pipe_index)
        self.assertEqual(actual, 8)

    def test_part_2(self):
        actual_1 = solve_part_2(pipe_index_1)
        self.assertEqual(actual_1, 1)
        actual_2 = solve_part_2(pipe_index_2)
        self.assertEqual(actual_2, 4)
        actual_3 = solve_part_2(pipe_index_3)
        self.assertEqual(actual_3, 8)
        actual_4 = solve_part_2(pipe_index_4)
        self.assertEqual(actual_4, 10)

if __name__ == "__main__":
    # add viz
    pipe_index_1 = construct_pipes_with_distances(data_sample)
    pipe_index_2 = construct_pipes_with_distances(data_sample_2)
    pipe_index_3 = construct_pipes_with_distances(data_sample_3)
    pipe_index_4 = construct_pipes_with_distances(data_sample_4)
    print("PIPES 1")
    helper_viz_draw_loop_with_box(pipe_index_1)
    print("PIPES 2")
    helper_viz_draw_loop_with_box(pipe_index_2)
    print("PIPES 3")
    helper_viz_draw_loop_with_box(pipe_index_3)
    print("PIPES 4")
    helper_viz_draw_loop_with_box(pipe_index_4)

    main()
