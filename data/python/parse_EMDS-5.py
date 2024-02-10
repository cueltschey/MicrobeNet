import os


name_map = """Actinophrys
Arcella
Aspidisca
Codosiga
Colpoda
Epistylis
Euglypha
Paramecium
Rotifera
Vorticella
Noctiluca
Ceratium
Stentor
Siprostomum
Keratella Quadrala
Euglena
Gymnodinium
Gonyaulax
Phacus
Stylongchia
Synchaeta""".split("\n")


for directory in os.listdir("/media/chasuelt/MICROBES/EMDS-6/EMDS5-Original/"):
    for file in os.listdir(os.path.join("/media/chasuelt/MICROBES/EMDS-6/EMDS5-Original/", directory)):
        if file.split(".")[-1] != "png":
            continue
        try:
            new_path = os.path.join("/media/chasuelt/MICROBES/microbe_images/", name_map[int(file.split("-")[1][1:]) - 1])
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            os.rename(os.path.join("/media/chasuelt/MICROBES/EMDS-6/EMDS5-Original/", directory, file), os.path.join(new_path, file))
        except OSError as err:
            print(err)

