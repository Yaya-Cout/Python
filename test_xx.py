def test_requirements():
    import os
    reponse = os.system("pip3 install -r requirements.txt")
    if reponse == 0:
        assert True
    else:
        assert False
