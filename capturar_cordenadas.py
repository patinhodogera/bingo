import matplotlib.pyplot as plt
from PIL import Image

def capturar_coordenadas(template_path):
    imagem = Image.open(template_path)
    fig, ax = plt.subplots()
    ax.imshow(imagem)

    coordenadas = []

    # Função que coleta as coordenadas quando o usuário clica
    def onclick(event):
        if event.xdata and event.ydata:
            x, y = int(event.xdata), int(event.ydata)
            coordenadas.append((x, y))
            print(f"Coordenada capturada: ({x}, {y})")
            # Marca o ponto clicado na imagem
            ax.plot(x, y, 'ro')  
            fig.canvas.draw()

            # Fecha a captura após 25 cliques (para as 25 células da cartela)
            if len(coordenadas) == 25:
                plt.close()

    # Conecta o evento de clique
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

    # Retorna as coordenadas capturadas
    return coordenadas

# Exemplo de uso: captura as coordenadas para a imagem 'template.png'
coordenadas = capturar_coordenadas("template.png")
print("Coordenadas capturadas:", coordenadas)
