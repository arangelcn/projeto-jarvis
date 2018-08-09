# -*- coding: utf-8 -*-

import speech_recognition as sr
import time
import os
from gtts import gTTS


import wikipedia
import urllib.request
import xml.etree.ElementTree
import subprocess
import unicodedata
import datetime

wikipedia.set_lang('pt')

# var para previsão do tempo
TEMPO = {'ec':'Encoberto com Chuvas Isoladas',
         'ci':'Chuvas Isoladas',
         'c':'Chuva',
         'in':'Instável',
         'pp':'Possibilidade de Pancadas de Chuva',
         'cm':'Chuva pela Manhã',
         'cn':'Chuva à Noite',
         'pt':'Pancadas de Chuva à Tarde',
         'pm':'Pancadas de Chuva pela Manhã',
         'np':'Nublado e Pancadas de Chuva',
         'pc':'Pancadas de Chuva',
         'pn':'Parcialmente Nublado',
         'cv':'Chuvisco',
         'ch':'Chuvoso',
         't':'Tempestade',
         'ps':'Predomínio de Sol',
         'e':'Encoberto',
         'n':'Nublado',
         'cl':'Céu Claro',
         'nv':'Nevoeiro',
         'g':'Geada',
         'ne':'Neve',
         'nd':'Não Definido',
         'pnt':'Pancadas de Chuva à Noite',
         'psc':'Possibilidade de Chuva',
         'pcm':'Possibilidade de Chuva pela Manhã',
         'pct':'Possibilidade de Chuva à Tarde',
         'pcn':'Possibilidade de Chuva à Noite',
         'npt':'Nublado com Pancadas à Tarde',
         'npn':'Nublado com Pancadas à Noite',
         'ncn':'Nublado com Possibilidade de Chuva à Noite',
         'nct':'Nublado com Possibilidade de Chuva à Tarde',
         'ncm':'Nublado com Possibilidade de Chuva pela Manhã',
         'npm':'Nublado com Pancadas de Chuva pela Manhã',
         'npp':'Nublado com Possibilidade de Chuva',
         'vn':'Variação de Nebulosidade',
         'ct':'Chuva à Tarde',
         'ppn':'Possibilidade de Pancadas de Chuva à Noite',
         'ppt':'Possibilidade de Pancadas de Chuva à Tarde',
         'ppm':'Possibilidade de Pancadas de Chuva pela Manhã'}


#Definicao do bot
#bot = ChatBot('Jarvis', read_only=True)

#definicao dicionario
dict_cmds = {}

#definicao keywords para pesquisa
os_comandos = ['abrir', 'executar', 'gerenciar', 'fechar', 'cancelar', 'criar', 'gerar', 'escrever']
wikipedia_keywords = ['o que é', 'quem foi', 'quem é', 'definição de', 'defina']
google_keywords = ['pesquise por', 'pesquisar por']

#-------------------------------

# Funcao resposável pela fala
def speak(audioString):
    #os.system("mpg123 -q audio.mp3")
    os.system("espeak -s 175 -p 5 -vpt-br '"+audioString+"' &")


#-------------------------------

# Funcao resposável pelo reconhecimento de voz
def recordAudio():
    #data = input("comando: ")

    data = None
    # Record Audio
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("ouvindo")
        audio = r.listen(source)
        # Speech recognition using Google Speech Recognition
    data = ""

    try:
        # Uses the default API key
        data = r.recognize_google(audio, language='pt')
        #data = r.recognize_sphinx(audio)
        print("You said: " + data)
        if data.lower() in "jarvis" or data.lower() in "garvis":
            speak("Sim senhor!")

    except sr.UnknownValueError:
        print("nao reconheceu")
    except sr.RequestError as e:
        print("nao reconheceu")

    return data.lower()

#-------------------------------

# Funcao para abrir programa
def abre_programa(text):

    if "google chrome" in text or "navegador" in text:
        speak("abrindo programa")
        os.system("google-chrome-stable &")

    if "spotify" in text:
        speak("abrindo programa")
        os.system("spotify &")

    if "netbeans" in text:
        speak("abrindo programa")
        os.system("netbeans &")

    if "whatsapp" in text:
        speak("abrindo programa")
        os.system("WhatsApp &")

    if "python" in text:
        speak("abrindo programa")
        os.system("/usr/lib/pycharm-community/bin/pycharm.sh &")

    if "terminal" in text:
        speak("abrindo programa")
        os.system("deepin-terminal &")

    if "calendário" in text:
        speak("abrindo programa")
        os.system("dde-calendar &")

    if "atom" in text:
        speak("abrindo programa")
        os.system("atom &")

    if "gerenciador de arquivos" in text:
        speak("abrindo programa")
        os.system("nautilus &")

    if "android studio" in text:
        speak("abrindo programa")
        os.system("android-studio &")

    if "monitor" in text:
        speak("abrindo programa")
        os.system("deepin-system-monitor &")

    if "editor de texto" in text:
        speak("abrindo programa")
        os.system("gedit &")

#-------------------------------


# Funcao para fechar programa
def fecha_programa(text):

    if "google chrome" in text:
        speak("fechando")
        os.system("killall chrome")

    if "spotify" in text:
        speak("fechando")
        os.system("killall spotify")

    if "netbeans" in text:
        speak("fechando")
        os.system("killall netbeans")

    if "whatsapp" in text:
        speak("fechando")
        os.system("killall WhatsApp")

    if "python" in text:
        speak("fechando")
        os.system("killall pycharm.sh")

    if "terminal" in text:
        speak("fechando")
        os.system("killall deepin-terminal")

    if "monitor" in text:
        time.sleep(2)
        speak("O processo deve ser encerrado manualmente")

    if "calendário" in text:
        speak("fechando")
        os.system("killall dde-calendar")

    if "atom" in text:
        speak("fechando")
        os.system("killall atom")

    if "android studio" in text:
        speak("fechando")
        os.system("killall android-studio")

    if "gerenciador de arquivos" in text:
        speak("fechando")
        os.system("killall nautilus")

    if "editor de texto" in text:
        speak("fechando")
        os.system("killall gedit")

#------------------------------------------------------

# Funcao para gerenciar memória do sistema
def gerencia_memoria():
    time.sleep(2)
    speak("Analizando processos e uso de memória")

    print(linha1)

#-------------------------------------------------------

# Funcao para criar arquivos:
def cria_arquivos(text):
    nome = ''
    ext = ''
    time.sleep(2)
    speak("Qual o nome do arquivo?")
    nome = recordAudio()

    if 'texto' in text:
        os.system("touch /home/arcn/" + nome + ".txt")
    if 'c' in text or 'se' in text:
        os.system("touch /home/arcn/" + nome + ".c")
    if 'python' in text:
        os.system("touch /home/arcn/" + nome + ".py")
    if 'html' in data:
        os.system("touch /home/arcn/" + nome + ".html")
    speak("Arquivo Criado")

#-----------------------------------------------------

# Funcao para gerenciar arquivos:
def gerencia_arquivos():
    time.sleep(2)
    speak("Qual a localização do arquivo")
    local = recordAudio()

    if "home" in local:
        local = "/home/arcn/"

    if "meus projetos" in local or "projetos" in local:
        local = "/home/arcn/Projetos/"

    if "imagens" in local:
        local = "/home/arcn/Pictures/"

    if "videos" in local:
        local = "/home/arcn/Videos/"

    if "download" in local or "downloads" in local:
        local = "/home/arcn/Downloads/"

    os.system("nautilus " + local + " &")

    time.sleep(2)
    speak("Qual o nome do arquivo que será modificado? ")
    nome = recordAudio()

    time.sleep(4)
    speak("Deseja editar ou excluir o arquivo? ")
    comando = recordAudio()

    if "editar" in comando:
        time.sleep(1)
        speak("Abrindo arquivo no editor")
        os.system("gedit "+local+""+nome+"* &")

    if "remover" in comando or "excluir" in comando:
        speak("Excluindo arquivo")
        os.system("rm "+local+""+nome+"*")

# Funcao para pesquisa no wikipedia
def resposta_wikipedia(text):
    if text is not None:
        speak("Pesquisando conteúdo no Wikipédia")
        results = wikipedia.search(text)
    else:
        return None

    if results is not None:
        #Pega o resultado da pesquisa
        result = wikipedia.summary(results[0], sentences=2)
        t = round(((60 * len(result.split())) / 170) + 8)
        time.sleep(1)
        speak("Alocando conteúdo no computador")
        time.sleep(3)
        #Gera o documento
        text = text.replace(' ', '-')
        arquivo = open('/home/arcn/' + text + '.txt', 'w')
        arquivo.write(result)
        speak(result)
        arquivo.close()
        os.system('gedit /home/arcn/' + text + '.txt &')
        time.sleep(t)
        speak("Deseja salvar o conteúdo?")
        time.sleep(1)
        var = recordAudio()
        if var == 'salvar conteúdo' or var== 'sim' or var== 'salvar':
            os.system('killall gedit')
            speak("Salvando o conteúdo na pasta home")
        else:
            speak("O arquivo será deletado")
            os.system('killall gedit')
            os.system('rm /home/arcn/' + text + '.txt')

    else:
        result = 'Nada encontrado'

# ---------------------------------------------------------------------------


# ---------------------  FUNÇÕES DE PREVISÃO DO TEMPO ------------------------
def getxmlcodes(args):
    # Busca do código das cidades
    codigos = []
    for query in args:
        with urllib.request.urlopen('http://servicos.cptec.inpe.br/XML/listaCidades?city={0}'.format(query)) as url:
            content = url.read().decode('iso-8859-1')

        root = xml.etree.ElementTree.fromstring(content)
        codigos.extend([ elem.text for elem in root.findall('./cidade/id') ])

    if len(codigos) == 0:
        raise ValueError("A busca não retornou nenhuma cidade")

    return codigos

def previsao(text):
    aux = [text]
    # Formatar entrada, remover acentos e substituir espaço por %20
    args = [unicodedata.normalize('NFKD', elem).encode('ascii', 'ignore').decode('ascii').lower().replace(' ', '%20')
            for elem in aux ]

    print(args)
    # Obter XML das cidades
    for codes in getxmlcodes(args):
        with urllib.request.urlopen('http://servicos.cptec.inpe.br/XML/cidade/{0}/previsao.xml'.format(codes)) as url:
            content = url.read().decode('iso-8859-1')

        # Filtrar os dados
        root = xml.etree.ElementTree.fromstring(content)
        dias = [ elem.text for elem in root.findall('previsao/dia') ]
        dias = [ datetime.datetime.strptime(elem, '%Y-%m-%d').strftime('%d/%m/%Y') for elem in dias ]
        clima = [elem.text for elem in root.findall('previsao/tempo') ]
        temperaturas = [ (ma, mi) for ma, mi in zip([elem.text for elem in root.findall('previsao/maxima') ],
                                                       [elem.text for elem in root.findall('previsao/minima') ]) ]

        iuv = [ elem.text for elem in root.findall('previsao/iuv') ]

        # Imprimir resultado
        time.sleep(3)
        speak('Previsão do tempo para {0} - {1}:'.format(root[0].text, root[1].text))
        time.sleep(4)
        speak('Clima: {0}'.format(TEMPO[clima[0]]))
        time.sleep(4)
        speak('Temperatura máxima: {0} graus'.format(temperaturas[0][0]))
        time.sleep(4)
        speak('Temperatura mínima: {0} graus'.format(temperaturas[0][1]))
        time.sleep(4)
        speak('Índice Ultra Violeta: {0}'.format(iuv[0]))
        time.sleep(4)


# ------------------------------------------------------------------------------ end previsao

# Funcção principal (análise dos dados de entrada)
def jarvis(data):

    if "abrir" in data or "executar" in data:
        abre_programa(data)

    if "fechar" in data or "cancelar" in data:
        fecha_programa(data)

    if "criar" in data or "gerar" in data or "escrever" in data:
        if "arquivo" in data:
            cria_arquivos(data)

    if "que horas são" in data:
        speak(time.ctime())

    if "onde fica" in data or "me mostre no mapa" in data or "localize" in data:
        data = data.replace('onde fica ', '')
        data = data.replace('me mostre no mapa ', '')
        data = data.replace('localize ', '')
        location = data.replace(' ', '%20')
        speak("Um segundo, processando localização" + location.replace('%20', ' ') )
        os.system("google-chrome-stable https://www.google.nl/maps/place/" + location + "/&amp;")

    if "pesquise por" in data or "pesquisar por" in data:
        data = data.replace('pesquisar por', '')
        data = data.replace('pesquise por', '')
        conteudo = data.replace(' ', '%20')
        os.system("google-chrome-stable https://www.google.com.br/search?q=" + conteudo + "&amp;")
        speak("pesquisando por " + conteudo.replace('%20', ' '))

    if "previsão do tempo" in data or "qual a previsão do tempo para" in data:
        speak("pesquisando")
        aux = data.replace('qual a previsão do tempo para ', '')
        aux = data.replace('previsão do tempo para ', '')
        aux2 = data.replace(' ', '%20')
        os.system("google-chrome-stable https://www.google.com.br/search?q=" + aux2 + "&amp;")
        previsao(aux)


    if "reiniciar" in data and "computador" in data or "máquina" in data or "sistema operacional" in data:
        speak("Reiniciando o computador")
        time.sleep(3)
        os.system("init 6")

    if "desligar" in data and "computador" in data or "máquina" in data or "sistema operacional" in data:
        speak("Até a próxima, o computador será desligado")
        time.sleep(3)
        os.system("init 0")

    if "quem foi" in data or "quem é" in data or "defina" in data or "o que é" in data or "quando ocorreu" in data or "definição de" in data or "qual é" in data:
        text = data
        for key in wikipedia_keywords:
            if text.startswith(key):
                text = text.replace(key, '')
        resposta_wikipedia(text)

    if "finalizar" in data or "encerrar" in data or "desligar" in data and "sistema de voz" in data or "processo de voz" in data:
        speak("encerrando sistema de voz, até mais Antonio")
        time.sleep(2)
        exit(0)

    if "qual minha agenda" in data or "quais meus compromissos" in data:
        speak("aqui estão seus compromissos")
        time.sleep(2)
        os.system("google-chrome-stable https://calendar.google.com/calendar/r/day?pli=1 &")

    if "gerenciar arquivos" in data or "manipular arquivos" in data:
        os.system("nautilus &")
        speak("abrindo gerenciador de arquivos")
        gerencia_arquivos()


    if "gerenciar" in data or "analizar" in data and "memória" in data or "processos" in data:
        gerencia_memoria()


# initialization

"""""          Carregar Dicionario
load_cmds()
for k, v in dict_cmds.items():
    print(k, v) 
"""

speak("iniciando sistema de voz")
time.sleep(2)
while 1:
    data = recordAudio()
    jarvis(data)
