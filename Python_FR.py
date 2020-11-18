def main():
    import sys
    print("Bienvenue dans Python en Français")

    def deuxpoints(cmd, instances):
        lastcmd = ""
        while True:
            for loop in range(instances):
                print("... ")
            cmd2points = input()
            cmd2points = "\n    " + cmd2points
            if lastcmd == "\n    " and cmd2points == "\n    ":
                break
            if cmd2points[-1:] == ":":
                deuxpoints(cmd, instances+1)
            lastcmd = cmd2points
            cmd += cmd2points
        return cmd
    while True:
        cmd = input(">>> ")
        try:
            if cmd[-1:] == ":":
                cmd = deuxpoints(cmd, 1)
                exec(cmd)
            else:
                exec(cmd)
                try:
                    if "print" in cmd:
                        pass
                    else:
                        exec("print("+str(cmd)+")")
                except Exception:
                    pass
        except AssertionError:
            print("L'instruction asset à échoué")
            print(sys.exc_info()[1])
        except AttributeError:
            print("La référance d'attribut ou l'afféctation à échoué")
            print(sys.exc_info()[1])
        except OverflowError:
            print("Le résultat dd l'opération arithmétique est trop grand")
            print(sys.exc_info()[1])
        except FloatingPointError:
            print("Erreur non utilisé actuellement")
            print(sys.exc_info()[1])
        except BufferError:
            print("Erreur du tampon")
            print(sys.exc_info()[1])
        except IndexError:
            print("L'index n'est pas valide")
            print(sys.exc_info()[1])
        except KeyError:
            print("La clé n'est pas valide")
            print(sys.exc_info()[1])
        except EOFError:
            print("Input() à atteint une condiion de fin de fichier")
            print(sys.exc_info()[1])
        # except GeneratorExit:
        #     pass
        except ModuleNotFoundError:
            print("Le module n'a pas été trouvé")
            print(sys.exc_info())[1]
        except ImportError:
            print("Erreur d'importation")
            print(sys.exc_info())[1]
        except KeyboardInterrupt:
            print("\nArret")
        except MemoryError:
            print("Il n'y a pas assez de mémoire !")
            print(sys.exc_info()[1])
        except UnboundLocalError:
            print("La variable est locale !")
            print(sys.exc_info()[1])
        except NameError:
            print("La variable n'existe pas !")
            print(sys.exc_info()[1])
        except NotImplementedError:
            print("Erreur non connue")
            print(sys.exc_info()[1])
        except RecursionError:
            print("Profondeur de récursivité maximale dépassée")
            print(sys.exc_info()[1])
        except ReferenceError:
            print("Un proxy de référance faible et utilisé pour accéder à un\
                 attribut du référent après qu'il a été récupéré")
            print(sys.exc_info()[1])
        except RuntimeError:
            print("Erreur non connue")
            print(sys.exc_info()[1])
        except StopIteration:
            print("next() indique qu'aucun n'autre element n'est produit par\
                 l'itérateur")
            print(sys.exc_info()[1])
        except StopAsyncIteration:
            print("anext() à arrété l'ittération")
            print(sys.exc_info()[1])
        except TabError:
            print("Il y a des incohérente de tabulations et d'espaces")
            print(sys.exc_info()[1])
        except IndentationError:
            print("Erreur d'indentation")
            print(sys.exc_info()[1])
        except SyntaxError:
            print("Erreur de syntaxe")
            print(sys.exc_info()[1])
        except SystemError:
            print("Erreur interne")
            print(sys.exc_info()[1])
        except SystemExit:
            print("Arret")
            print(sys.exc_info()[1])
        except TypeError:
            print("Immposible d'ajouter deux classes différantes ou vous avez\
                 oublier d'ajouter le.s paramètre de la fonction")
            print(sys.exc_info()[1])
        except UnicodeEncodeError:
            print("Erreur lors de l'encodage")
            print(sys.exc_info()[1])
        except UnicodeDecodeError:
            print("Erreur lors du décodage")
            print(sys.exc_info()[1])
        except UnicodeTranslateError:
            print("Erreur lors de la traduction")
            print(sys.exc_info()[1])
        except UnicodeError:
            print("Une erreur lié à l'unicode s'est produite !")
            print(sys.exc_info()[1])
        except ValueError:
            print("La valeur de la fonction est inapropriée mais le type est\
                 bon")
            print(sys.exc_info()[1])
        except ZeroDivisionError:
            print("Impossible de diviser par zéro")
            print(sys.exc_info()[1])
        except EnvironmentError:
            print("Erreur d'environnement")
            print(sys.exc_info()[1])
        except IOError:
            print("Erreur d'entrée/sortie, aucun fichier/dossier de ce type")
            print(sys.exc_info()[1])
        # except WindowsError:
        #     print("Erreur de Windows")
        except ArithmeticError:
            print("Erreur d'arithmétique")
            print(sys.exc_info()[1])
        except Warning:
            print("Attention : " + sys.exc_info())
        except BaseException:
            print(sys.exc_info())
        # print ("%s" % sys.exc_info()[1])
        # print (sys.exc_info())


if __name__ == "__main__":
    main()
