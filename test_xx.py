def lint():
    import os
    reponse = os.system("flake8 .")
    if reponse == 0:
        return True
    else:
        return False


def tests():
    assert lint()
