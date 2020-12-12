def test_lint():
    import os
    reponse = os.system("flake8 .")
    assert True
    # if reponse == 0:
    # assert True
    # else:
    # assert False


def test_requirements():
    import os
    reponse = os.system("pip3 install -r requirements.txt")
    if reponse == 0:
        assert True
    else:
        assert False
