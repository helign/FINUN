import Marynova_ZBPI211c as mar
import pytest
import math

#TEST 1

@pytest.mark.parametrize('n', range(30))
def test_fact(n):
    #Verify the output of `fact` function#
    output = mar.fact(n)
    assert output == math.factorial(n)

#TEST 2

import random
    
test_inputs = []
for i in range(30):    
      test_inputs.append(random.sample(range(100), 4))
test_expectations = []
for j in test_inputs:
      test_expectations.append([x for x in j if x % 2 == 0])
EVEN_TEST=list(zip(test_inputs, test_expectations))

@pytest.mark.parametrize("test_lists",EVEN_TEST)
def test_filter_even(test_lists):
    #Verify the output of `filter_even` function
    output = mar.filter_even(test_lists[0])
    assert output == test_lists[1]

#TEST 3

test_inputs = []
for i in range(30):    
      test_inputs.append(random.sample(range(100), 4))
test_expectations = []
for j in test_inputs:
      test_expectations.append([x**2 for x in j])
SQUARE_TEST=list(zip(test_inputs, test_expectations))

@pytest.mark.parametrize("test_lists", SQUARE_TEST)
def test_square(test_lists):
    output = mar.square(test_lists[0])
    assert output == test_lists[1]    

#TEST 4
list_sample = [x+10 for x in range(30)]
BIN_TEST = []
for i in range(len(list_sample)):
    BIN_TEST.append([list_sample,list_sample[i],i])

@pytest.mark.parametrize("test_lists",BIN_TEST)
def test_bin_search_found(test_lists):
    output = mar.bin_search(test_lists[0],test_lists[1])
    assert output == test_lists[2]
    
def test_bin_search_not_found():
    output = mar.bin_search([2,5,7,9,11,17,222],12)
    assert output == -1
    
#TEST 5

def palindrome_number_generator():
    yield 0    
    lower = 1
    while True:
        higher = lower*10
        for i in range(lower, higher):    
            s = str(i)
            yield int(s+s[-2::-1])
        for i in range(lower, higher):    
            s = str(i)
            yield int(s+s[::-1])
        lower = higher


def palindromes(lower, upper):
    all_palindrome_numbers = palindrome_number_generator()
    for p in all_palindrome_numbers:
        if p >= lower:
            break
    palindrome_list = [p]
    for p in all_palindrome_numbers:
        if p >= upper:
            break
        palindrome_list.append(p)
    return palindrome_list

TEST_PALINDROME = palindromes(121,454)

@pytest.mark.parametrize("test_lists",TEST_PALINDROME)
def test_is_palindrome(test_lists):
    output = mar.is_palindrome(str(test_lists))
    assert output == True
    
def test_is_palindrome_punctuation():
    output = mar.is_palindrome("Madam, I'm Adam")
    assert output == True
    
def test_is_palindrome_case():
    output = mar.is_palindrome("А роза упала на лапу Азора")
    assert output == True
    
def test_is_palindrome_not():
    output = mar.is_palindrome("Some Text That Is not Palindrome")
    assert output == False
    
#TEST 6

def test_calculate():
    path_file_input="test_input_file_1.txt"
    path_file_expected="test_output_file_1.txt"
    output = mar.calculate(path_file_input)
    expected = ""
    with open(path_file_expected, mode='r') as f:
        expected = f.read()
    assert output == expected

#TEST 7

def test_substring_slice():
    path_file_input_1="test_import_file_2_1.txt"
    path_file_input_2="test_import_file_2_2.txt"
    path_file_expected="test_output_file_2.txt"
    output = mar.substring_slice(path_file_input_1,path_file_input_2)
    expected = ""
    with open(path_file_expected, mode='r') as f:
        expected = f.read()
    assert output == expected

#8
def test_decode_ch():
    input_str="NOTiFICaTiON"
    expected_str="АзотКислородТитанФторЙодКальцийТитанКислородАзот"
    output = mar.decode_ch(input_str)
    assert output == expected_str

#9

def test_Student():
    tc = mar.Student("Ivan","Ivanov")
    pc = mar.Student("Leha","Levo")
    assert tc.greeting() == "Hello, I am Student"
    assert tc.mean_grade() == 4
    assert tc.is_otlichnik() == "NO"
    assert str(tc) == "Ivan Ivanov"
    assert tc + pc == "Ivan is friends with Leha"

#10

def get_MyError(name):
    if name!="Bikini":
        raise mar.MyError("So full of youth!")
    else:
        return "Username is properly set."

def test_username_MyError():
    """test for invalid username"""
    with pytest.raises(mar.MyError) as e:
        assert get_MyError("Nick")
        assert str(e.value) == "Username is properly set"

        