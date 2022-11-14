from main import vend
from tud_test_base import set_keyboard_input, get_display_output


def test1():
    set_keyboard_input(["0", "0", "2", "50", "n"])
    vend()
    output = get_display_output()
    assert output == ["Refunded: ",
                      "1.0 $ :  7",
                      "20.0 $ :  2",
                      "Thank you, have a nice day!"]


def test2():
    set_keyboard_input(["5", "10"])
    vend()
    output = get_display_output()
    assert output ==["Please enter a valid row and column."]


def test3():
    set_keyboard_input(["4", "4", "1", "100", "100", "100", "100", "100", "50", "20", "20", "n"])
    vend()
    output = get_display_output()
    assert output == ["Thank you, have a nice day!"]


def test4():
    set_keyboard_input(["3", "0", "3", "5893804115457289", "y", "1", "4", "2", "50", "n", "20", "n"])
    vend()
    output = get_display_output()
    assert output == ["Refunded: ", "0.2 $ :  2", "1.0 $ :  4", "20.0 $ :  2", "Thank you, have a nice day!"]
