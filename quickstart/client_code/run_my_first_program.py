from nada_dsl import *

def nada_main():
    # Define three parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    # Define secret inputs for two parties
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))

    # Perform a multiplication operation
    result = a * b

    # Return the result as output to the third party
    return [Output(result, "multiplication_output", party3)]
