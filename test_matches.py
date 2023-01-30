from matches import matches


class TestMatches:
    def test_all_intersection(self):
        assert matches(1, 5, 0, 1, 4, 8) == 0

    def test_non_intersection_small_hole(self):  # спичка 3 соединит 1 и 2
        assert matches(1, 2, 9, 10, 12, 20) == 3

    def test_non_intersection_small_hole_2(self):  # можно либо спичкой 1 соединить спички 2 и 3,
        # либо спичкой 3 соединить 1 и 2 - выбран наименьший № спички
        assert matches(1, 4, 9, 10, 12, 20) == 1

    def test_non_intersection_small_hole_3(self):  # три одинаковых спички на одинаковых расстояниях
        assert matches(5, 6, 7, 8, 3, 4) == 2

    def test_non_intersection_big_holes(self):  # ни одна из спичек не может соединить все три
        assert matches(1, 2, 9, 10, 12, 14) == -1

    def test_first_with_second_big_hole(self):  # спичка 3 может соединить 1 и 2
        assert matches(5, 6, 7, 8, 1, 2) == 3

    def test_second_with_third_big_hole(self):  # спичку 1 двигаем к пересекающимся 2 и 3
        assert matches(10, 17, 2, 5, 0, 3) == 1

    def test_second_with_third_small_hole(self):  # можно подвинуть спичку 3 или соединить 2 и 3 спичкой 1 -
        # выбран наименьщий № спички
        assert matches(0, 3, 2, 5, 8, 10) == 1

    def test_wrong_conditions(self):
        assert matches(5, 6, 7, 8, -1, 4) == -1

    def test_wrong_conditions_2(self):
        assert matches(5, 101, 7, 8, 3, 4) == -1

    def test_wrong_conditions_3(self):
        assert matches(5, 6, 17, 8, 3, 4) == -1
