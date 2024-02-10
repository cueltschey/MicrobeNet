import os

names_map = """Oscillatoria
Ankistrodesmus
Microcystis
Gomphenoma
Sphaerocystis
Cosmarium
Cocconeis
Tribonema
Chlorella
Tetraedron
Ankistrodesmus
Branchionus
Chaenea
Pediastrum
Spirulina
Actinastrum
Navicula
Scenedesmus
Golenkinia
Pinnularia
Staurastrum
Phormidium
Fragilaria
Anabaenopsis
Coelosphaerium
Crucigenia
Achnanthes
Synedra
Ceratium
Pompholyx
Merismopedia
Spirogyra
Coelastrum
Raphidiopsis
Gomphosphaeria
Euglena
Euchlanis
Keratella
Diversicornis
Surirella
Characium
""".split("\n")

for file in os.listdir("/media/chasuelt/MICROBES/EMDS7/"):
    #os.rename(os.path.join("/media/chasuelt/MICROBES/EMDS7/", file), os.path.join("/media/chasuelt/MICROBES/microbe_images/", names[file.split()]))
    if not os.path.exists(os.path.join("/media/chasuelt/MICROBES/microbe_images/", names_map[int(file.split("-")[1][1:]) - 1])):
        os.mkdir(os.path.join("/media/chasuelt/MICROBES/microbe_images/", names_map[int(file.split("-")[1][1:]) - 1]))
    os.rename(os.path.join("/media/chasuelt/MICROBES/EMDS7/", file), os.path.join("/media/chasuelt/MICROBES/microbe_images/", names_map[int(file.split("-")[1][1:]) - 1], file))
