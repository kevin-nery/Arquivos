import os
import csv

def ler_planilha(arquivo_csv):
    codigos = []
    
    try:
        with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for linha in reader:
                codigos.append(linha[0]) 
    except Exception as e:
        print(f"Erro ao abrir o arquivo CSV: {e}")
    
    return codigos

def mover_arquivos(pasta_origem, pasta_destino, codigos):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    arquivos = os.listdir(pasta_origem)
    
    for arquivo in arquivos:
        nome_arquivo = os.path.splitext(arquivo)[0]
        
        if nome_arquivo in codigos:
            origem = os.path.join(pasta_origem, arquivo)
            destino = os.path.join(pasta_destino, arquivo)
            
            try:
                os.rename(origem, destino)
                print(f"Arquivo '{arquivo}' movido com sucesso para '{pasta_destino}'.")
            except Exception as e:
                print(f"Erro ao mover o arquivo '{arquivo}': {e}")

pasta_origem = r'C:\Users\kevin.nery\Documents\Arquivos\Processados' # Insira aqui o caminho da pasta das chaves, como no exemplo
pasta_destino = r'C:\Users\kevin.nery\Documents\Arquivos\XML' # Insira aaui o caminho da pasta de destino das chaves, commo no exemplo
arquivo_csv = r'C:\Users\kevin.nery\Documents\Arquivos\xmls.csv' # Insira aqui o caminho do arquivo .csv, como no exemplo

codigos = ler_planilha(arquivo_csv)

mover_arquivos(pasta_origem, pasta_destino, codigos)
