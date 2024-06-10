import pandas as pd

class Utils:
    @staticmethod
    def new_penguin(model, mapping):
        print("Entre com os dados de um novo penguim:")
        island = int(input("Island [0, 2]: "))
        sex = int(input("Sex [0, 1]:"))
        culmen_len = float(input("Culmen Length (mm):"))
        culmen_dep = float(input("Culmen Depth (mm):"))
        flipper_len = int(input("Flipper Length (mm):"))
        body_mass = int(input("Body Mass (g):"))
        
        data = [{'island':island, 'sex':sex, 'culmen_length_mm':culmen_len, 
                'culmen_depth_mm':culmen_dep, 'flipper_length_mm':flipper_len, 'body_mass_g':body_mass}]
        data = pd.DataFrame(data)

        pred = model.predict(data)
        
        specie = None
        for key, value in mapping['species'].items():
            if value == pred[0]:
                specie = key
                break
            
        print(f"O penguin pertence à espécie {specie}\n")
