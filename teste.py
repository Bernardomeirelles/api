import pandas as pd

# Dados organizados novamente para exportação
data = [
    ["Craft", "N/A", "Outros", "Cosmel", "Cosmel", "N", "R$15,00", "R$15,00", "OK", "-"],
    ["Craft", "N/A", "Outros", "CDB", "CDB", "N", "R$7,00", "R$13,00", "OK", "-"],
    ["Cerveja", "600ml", "Ambev", "Brahma", "Cerveja Brahma 600ml", "N", "R$13,00", "R$13,00", "OK", "-"],
    ["Cerveja", "600ml", "Ambev", "Original", "Cerveja Original 600ml", "N", "R$15,00", "R$15,00", "OK", "-"],
    ["Cerveja", "600ml", "Ambev", "Spaten", "Cerveja Spaten 600ml", "S", "-", "R$15,00", "Alerta", "Spaten deve custar pelo menos R$2 a menos que Heineken"],
    ["Cerveja", "600ml", "Heineken", "Heineken", "Heineken 600ml", "N", "R$20,00", "R$20,00", "Alerta", "Spaten deve custar pelo menos R$2 a menos que Heineken"],
    ["Cerveja", "600ml", "Ambev", "Amstel", "Cerveja Amstel 600ml", "N", "R$15,00", "R$15,00", "OK", "-"],
    ["Cerveja", "600ml", "Ambev", "Petra", "Cerveja Petra 600ml", "N", "R$13,00", "R$13,00", "OK", "-"],
    ["Cerveja", "600ml", "Ambev", "Itaipava", "Cerveja Itaipava 600ml", "N", "R$12,00", "R$12,00", "OK", "-"],
    ["Cerveja", "600ml", "Ambev", "Skol", "Cerveja Skol 600ml", "N", "R$13,00", "R$13,00", "OK", "-"],
    ["Cerveja", "Lata 350ml", "N/A", "N/A", "Cerveja lata", "N", "R$5,00", "R$5,00", "OK", "-"],
    ["Cerveja", "Long Neck", "Ambev", "Corona", "Corona", "S", "-", "R$10,00", "OK", "-"],
    ["Cerveja", "Long Neck", "Heineken", "Heineken", "Heineken", "S", "-", "R$10,00", "OK", "-"],
    ["Cerveja", "Long Neck", "Ambev", "Budweiser", "Budweiser", "S", "-", "R$9,00", "OK", "-"],
    ["Cerveja", "350ml", "N/A", "N/A", "Cerveja sem álcool 350ml", "N", "R$7,00", "R$7,00", "OK", "-"],
    ["Drink pronto", "Long Neck", "Outros", "Beats", "BEATS (Long Neck)", "S", "-", "R$10,00", "OK", "-"],
    ["Drink pronto", "Long Neck", "Outros", "Ice Cabaré", "Ice Cabaré (Long Neck)", "N", "R$11,00", "R$11,00", "OK", "-"],
    ["Sem álcool", "Lata 350ml", "Coca-Cola", "Guaraná Antarctica", "Guaraná Antarctica (Lata)", "S", "-", "R$7,00", "OK", "-"],
    ["Sem álcool", "Lata 350ml", "Coca-Cola", "Guaraná Antarctica Zero", "Guaraná Antarctica Zero (Lata)", "S", "-", "R$6,00", "OK", "-"],
    ["Sem álcool", "Lata 350ml", "Coca-Cola", "Coca-Cola", "Coca-Cola (Lata)", "S", "-", "R$8,00", "OK", "-"],
    ["Sem álcool", "Lata 350ml", "Coca-Cola", "Fanta", "Fanta (Lata)", "N", "R$7,00", "R$7,00", "OK", "-"],
    ["Sem álcool", "1L", "Coca-Cola", "Guaraná Antarctica", "Guaraná Antarctica 1L", "N", "R$10,00", "R$9,00", "OK", "-"],
    ["Sem álcool", "1L", "Coca-Cola", "Coca-Cola", "Coca-Cola 1L", "N", "R$10,00", "R$10,00", "OK", "-"],
    ["Sem álcool", "1L", "Coca-Cola", "Fanta", "Fanta 1L", "N", "R$10,00", "R$10,00", "OK", "-"],
    ["Sem álcool", "1,5L", "Coca-Cola", "Guaraná Antarctica", "Guaraná Antarctica 1,5L", "S", "-", "R$10,00", "OK", "-"],
    ["Sem álcool", "1,5L", "Coca-Cola", "Coca-Cola", "Coca-Cola 1,5L", "N", "R$13,00", "R$15,00", "OK", "-"],
    ["Sem álcool", "1,5L", "Coca-Cola", "Fanta", "Fanta 1,5L", "N", "R$13,00", "R$16,00", "OK", "-"],
    ["Sem álcool", "2L", "Coca-Cola", "Guaraná Antarctica", "Guaraná Antarctica 2L", "N", "R$16,00", "R$15,00", "OK", "-"],
    ["Sem álcool", "2L", "Coca-Cola", "Coca-Cola", "Coca-Cola 2L", "N", "R$16,00", "R$20,00", "OK", "-"],
    ["Sem álcool", "2L", "Coca-Cola", "Fanta", "Fanta 2L", "N", "R$15,00", "R$12,00", "OK", "-"],
    ["Sem álcool", "2L", "Coca-Cola", "Kitubaína", "Kitubaína 2L", "N", "R$12,00", "R$12,00", "OK", "-"],
    ["Sem álcool", "N/A", "N/A", "N/A", "Água Mineral Sem Gás", "N", "R$4,00", "R$4,00", "OK", "-"],
    ["Sem álcool", "N/A", "N/A", "N/A", "Água Mineral Com Gás", "N", "R$5,00", "R$5,00", "OK", "-"],
    ["Sem álcool", "N/A", "N/A", "N/A", "Copo Especial (limão e gelo)", "N", "R$1,00", "R$1,00", "OK", "-"],
]

columns = ["Categoria", "Embalagem", "Fabricante", "Marca", "Nome do item", "Status", "Preço antigo", "Preço novo", "Status Golden Rules", "Regra Golden Rule"]
df = pd.DataFrame(data, columns=columns)

# Exportar para CSV
file_path = "/mnt/data/Comparacao_Cardapio.csv"
df.to_csv(file_path, index=False)

file_path