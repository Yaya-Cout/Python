def test_requirements():
    import os

    response = os.system("pip3 install -r requirements.txt")
    if response == 0:
        assert True
    else:
        assert False
