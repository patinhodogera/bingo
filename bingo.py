import random
from PIL import Image, ImageDraw, ImageFont

def gerar_cartela_bingo():
    cartela = []

    # Intervalos de números para cada coluna
    intervalos = [
        range(1, 16),   # Números da coluna B
        range(16, 31),  # Números da coluna I
        range(31, 46),  # Números da coluna N
        range(46, 61),  # Números da coluna G
        range(61, 76)   # Números da coluna O
    ]

    for i, intervalo in enumerate(intervalos):
        if i == 2:  # Para a coluna N, reservamos o espaço do meio
            coluna = random.sample(intervalo, 4)
            coluna.insert(2, "")  # Espaço vazio no meio
        else:
            coluna = random.sample(intervalo, 5)
        cartela.append(coluna)

    return cartela

def criar_cartela_personalizada(cartela, template_path, output_path, icon_path):
    # Abre a imagem base
    imagem = Image.open(template_path)
    draw = ImageDraw.Draw(imagem)

    # Definindo a fonte (ajuste o caminho se necessário)
    try:
        fonte = ImageFont.truetype("BungeeTint-Regular.ttf", 28)  # Aumentei o tamanho da fonte
        fonte_topo = ImageFont.truetype("BungeeTint-Regular.ttf", 36)  # Fonte maior para o topo
    except IOError:
        fonte = ImageFont.load_default()
        fonte_topo = ImageFont.load_default()

    # Coordenadas para cada coluna (S, N, A, K, E) com altura constante para todas as linhas
    alturas = [218, 269, 320, 371, 422]  # Alturas constantes para todas as colunas

    # Coordenadas para as colunas com base nas alturas
    coordenadas = [
        [(150, y) for y in alturas],  # Coluna S
        [(225, y) for y in alturas],  # Coluna N
        [(293, y) for y in alturas],  # Coluna A
        [(365, y) for y in alturas],  # Coluna K
        [(440, y) for y in alturas]   # Coluna E
    ]

    # Letras para o topo
    letras_topo = ['B', 'I', 'N', 'G', 'O']
    coordenadas_topo = [148, 215, 292, 366, 440]  # Posições x para as letras do topo

    # Desenhando as letras do topo
    for i, letra in enumerate(letras_topo):
        x = coordenadas_topo[i]
        y = 170  # Altura para as letras do topo
        draw.text((x, y), letra, fill="orange", font=fonte_topo, anchor="mm")

    # Função para desenhar números com contorno
    def draw_text_with_outline(draw, position, text, font, outline_color, fill_color, outline_width=2):
        x, y = position
        # Desenha o contorno ao redor do texto
        for dx in [-outline_width, 0, outline_width]:
            for dy in [-outline_width, 0, outline_width]:
                if dx != 0 or dy != 0:
                    draw.text((x + dx, y + dy), text, font=font, fill=outline_color, anchor="mm")
        # Desenha o texto principal no centro
        draw.text((x, y), text, font=font, fill=fill_color, anchor="mm")

    # Preenchendo a cartela com os números e aplicando o contorno laranja
    for i, coluna in enumerate(cartela):
        for j, numero in enumerate(coluna):
            x, y = coordenadas[i][j]
            if numero:  # Ignora a célula central que é vazia
                draw_text_with_outline(draw, (x, y), str(numero).zfill(2), fonte, outline_color="orange", fill_color="black")


    # Adicionando o ícone no centro da cartela
    icon = Image.open(icon_path)
    icon = icon.resize((50, 50))  # Redimensiona o ícone para caber no espaço
    icon_x, icon_y = coordenadas[2][2]  # Posição do centro da cartela (coluna N, linha 3)
    icon_position = (icon_x - 22, icon_y - 30)  # Centralizando o ícone no espaço
    imagem.paste(icon, icon_position, icon)  # Coloca o ícone no centro

    # Salva a nova imagem com os números preenchidos e o ícone no meio
    imagem.save(output_path)
    imagem.show()

# Gerar a cartela de bingo e criar a imagem personalizada com ícone
cartela_bingo = gerar_cartela_bingo()
criar_cartela_personalizada(cartela_bingo, "template.png", "cartela_bingo_personalizada.png", "icon.png")

