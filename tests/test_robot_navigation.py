import pytest

from src.Mission import Mission
from src.Plateau import Plateau


def test_mission_control_success():
    # Test complete mission execution with sample input.
    """
        5 5
        1 2 N
        LMLMLMLMM
        3 3 E
        MMRMMRRMRM
    """
    plateau = Plateau(5, 5)
    mission = Mission(plateau)
    mission.deploy_robot(1, 2, "N", "LMLMLMLMM")
    mission.deploy_robot(3, 3, "E", "MMRMMRMRRM")
    results = mission.execute()
    expected_output = ["1 3 N", "5 1 E"]
    assert results == expected_output


def test_mission_control_failure_robot_out_of_bound():
    plateau = Plateau(5, 5)
    mission = Mission(plateau)
    mission.deploy_robot(1, 2, "N", "MMMMMMM")
    with pytest.raises(RuntimeError, match="attempted to move out of bounds. Direction: N, Target: \(1, 6\)"):
        mission.execute()


def test_mission_control_failure_robot_invalid_position():
    plateau = Plateau(5, 5)
    mission = Mission(plateau)
    with pytest.raises(ValueError, match="Initial x position -1 is below 0 \(min bound\)."):
        mission.deploy_robot(-1, 2, "N", "MMMMMMM")
    with pytest.raises(ValueError, match="Initial x position 6 exceeds plateau max_x 5"):
        mission.deploy_robot(6, 2, "N", "MMMMMMM")
    with pytest.raises(ValueError, match="Initial y position -2 is below 0 \(min bound\)."):
        mission.deploy_robot(1, -2, "N", "MMMMMMM")
    with pytest.raises(ValueError, match="Initial y position 6 exceeds plateau max_y 5"):
        mission.deploy_robot(1, 6, "N", "MMMMMMM")


def test_mission_control_failure_invalid_instruction():
    """
        5 5
        1 2 N
        XO
    """
    plateau = Plateau(5, 5)
    mission = Mission(plateau)
    with pytest.raises(ValueError, match="Invalid instruction: X"):
        mission.deploy_robot(1, 2, "N", "XO")


def test_invalid_grid_size_input():
    # Invalid x grid size
    with pytest.raises(ValueError, match="Plateau max_x must be non-negative. Got: -5"):
        Plateau(-5, 5)
    # Invalid y grid size
    with pytest.raises(ValueError, match="Plateau max_y must be non-negative. Got: -5"):
        Plateau(5, -5)


if __name__ == '__main__':
    pytest.main()
