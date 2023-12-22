import unittest

from day_08_haunted_wasteland import (
    Node,
    create_network_dict,
    find_next_node,
    solve_part_1,
    solve_part_2
)

with open("data/08_sample.txt") as f:
    sample_data = f.readlines()

# LLR
#
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)

instructions: str = sample_data[0].strip("\n")
all_network: list[str] = sample_data[2:]


class TestWastelandNavigation(unittest.TestCase):
    def test_node_is_constructed_correctly(self):
        actual_1 = Node(all_network[0])
        actual_2 = Node(all_network[1])
        actual_3 = Node(all_network[2])

        self.assertEqual(actual_1.location, "AAA")
        self.assertEqual(actual_1.left, "BBB")
        self.assertEqual(actual_1.right, "BBB")

        self.assertEqual(actual_2.location, "BBB")
        self.assertEqual(actual_2.left, "AAA")
        self.assertEqual(actual_2.right, "ZZZ")

        self.assertEqual(actual_3.location, "ZZZ")
        self.assertEqual(actual_3.left, "ZZZ")
        self.assertEqual(actual_3.right, "ZZZ")

    def test_node_destination_is_correct(self):
        node = Node(all_network[1])
        self.assertEqual(node.find_next("L"), "AAA")
        self.assertEqual(node.find_next("R"), "ZZZ")

    def test_network_dict_is_correct(self):
        actual = create_network_dict(all_network)
        self.assertEqual(actual["BBB"].location, "BBB")
        self.assertEqual(actual["BBB"].left, "AAA")
        self.assertEqual(actual["BBB"].right, "ZZZ")

    def test_correct_next_location_is_returned(self):
        network = create_network_dict(all_network)
        self.assertEqual(find_next_node(network, "BBB", "R"), "ZZZ")
        self.assertEqual(find_next_node(network, "AAA", "R"), "BBB")
        self.assertEqual(find_next_node(network, "BBB", "L"), "AAA")

    def test_part_1_is_correct(self):
        actual = solve_part_1(instructions, all_network)
        self.assertEqual(actual, 6)

    def test_node_destination_suffix(self):
        actual_1 = Node(all_network[0])
        actual_2 = Node(all_network[1])

        self.assertEqual(actual_1.location_suffix, "A")
        self.assertEqual(actual_1.left_suffix, "B")
        self.assertEqual(actual_1.right_suffix, "B")

        self.assertEqual(actual_2.location_suffix, "B")
        self.assertEqual(actual_2.left_suffix, "A")
        self.assertEqual(actual_2.right_suffix, "Z")

    def test_node_destination_suffix_is_correct(self):
        node = Node(all_network[1])
        self.assertEqual(node.find_next_suffix("L"), "A")
        self.assertEqual(node.find_next_suffix("R"), "Z")

    def test_part_2_is_correct(self):
        with open("data/08_sample_2.txt") as f:
            sample_data_2 = f.readlines()

        instructions: str = sample_data_2[0].strip("\n")
        all_network: list[str] = sample_data_2[2:]

        actual = solve_part_2(instructions, all_network)
        self.assertEqual(actual, 6)

if __name__ == "__main__":
    unittest.main()
