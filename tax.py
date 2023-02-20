
def calculateTax(amount, interest, purpose):
    # amount   ---> suma de bani
    # interest ---> procentul impozat
    # purpose  ---> scopul sumei de bani
    
    tax = amount * (interest / 100)
    
    # se va crea un dictionar deoarece acesta poate contine mai multe valori, iar fiecare valoare poate fi accesata printr-o singura cheie.
    result = {
        "amount"    : amount,
        "interest"  : interest,
        "tax"       : tax,
        "purpose"   : purpose
    }
    return result