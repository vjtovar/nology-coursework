import sys
sys.path.insert(1, './code')
from adventure_game import intro_scene, choice_1
from tud_test_base import set_keyboard_input, get_display_output
import pytest
import sqlite3
import requests
import os


def test_file_exists():
    assert os.path.exists('./code/adventure_game.py')
    assert os.path.exists('./test.log')

def test_file_contents():
    with open('./test.log', 'r') as f:
        contents = f.read()
    assert "This is a Debug msg" in contents    


def test_get_name():  
    set_keyboard_input(["Val"]) 
    intro_scene()
    output = get_display_output()
    assert output == ["What is your name adventurer: ", f"""
                        ☠️☠️☠️ Val, you are lost on a deserted island! ☠️☠️☠️
    """, """
                Your airplane had an engine blow out and you crash landed on an island. 
                You wake up washed ashore and realize you are alone, the only survivor, 
                with only the clothes on your back and a desire to survive.
    """]
    assert set_keyboard_input != "", "You didn't key in any name"



def test_directions():
    set_keyboard_input(["North","South", "East", "West"])
    choice_1()
    output = get_display_output()
    assert "What direction would you like to go? (North, South, East, or West): " in output

    



