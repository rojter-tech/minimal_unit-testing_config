import os
import sys
if __name__ == "__main__":
    print("Source was executed.")
else:
    print("Source was imported.")
this_scriptpath = os.path.abspath(__file__) # Absolut sökväg till den här filen 
                                            # (ser olika ut i Mac och Windows, men fungerar lika bra när 
                                            # man använder de inbyggda generella funktionerna)
                                            #
                                            # Exempel, output är alltså en sträng med en sökväg till filen:
                                            # I Unix blir det:
                                            # /home/user/minimal_unit-testing_config/src/utilities/__init__.py
                                            # I Windows blir det:
                                            # C:\Users\user\minimal_unit-testing_config\src\utilities\__init__.py
                                            # )
this_scriptdir = os.path.dirname(this_scriptpath) # Skalar av "topreferensen" i föregående sökväg.
                                                  #
                                                  # Vi får nu exempelvis:
                                                  # I Unix:
                                                  # /home/user/minimal_unit-testing_config/src/utilities
                                                  # I Windows:
                                                  # C:\Users\user\minimal_unit-testing_config\src\utilities
sys.path.insert(0, this_scriptdir) # Sätter in sökvägen i pythons eget referenssystem.
import utilities # Fungerar eftersom vi skapade en absolut referens i sys.path ovan.

module_import=True # Testvariabel som kan användas efter importering av src-paketet.