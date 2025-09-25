import streamlit  as st

generos = {
    
    "Sertanejo" : {
        "Barões Da Pisadinha" : 'https://www.youtube.com/watch?v=y_HY1jZlUP0&list=RDy_HY1jZlUP0&start_radio=1',
        "Gustavo Lima" : "https://www.youtube.com/watch?v=14C28JSO-sg&list=RD14C28JSO-sg&start_radio=1"
    
    },
    "Eletronica" : {
        "Alok" : "https://www.youtube.com/watch?v=czNEZdZggbY",
        "Marshmello" : "https://www.youtube.com/watch?v=ALZHF5UqnU4&list=RDALZHF5UqnU4&start_radio=1"
    
    },
    "Rap" : {
        "Snoop Dogg" : "https://www.youtube.com/watch?v=GtUVQei3nX4&list=RDGtUVQei3nX4&start_radio=1",
        "Eminem" : "https://www.youtube.com/watch?v=XbGs_qK2PQA&list=RDXbGs_qK2PQA&start_radio=1"

    },
    "Trap" : {
        "Matuê" : "https://www.youtube.com/watch?v=rGHJ0mqean4&list=RDrGHJ0mqean4&start_radio=1",
        "Teto" : "https://www.youtube.com/watch?v=iDJM3HTdjck&list=RDiDJM3HTdjck&start_radio=1"
    
    }

}



st.sidebar.title("Playlists do Skyline")
st.sidebar.image("SKYLINE.PNG")
genero = st.sidebar.selectbox("Selecione um genero musical",generos.keys())
artista = st.sidebar.selectbox("Selecione o artista", generos[genero].keys())

st.title(artista)

video, sobre = st.tabs(["Video", "Sobre Artista"])

with video:
    st.video(generos[genero][artista])

    with sobre:
        if artista == "Matuê":
            st.markdown('''Matheus Brasileiro Aguiar (Fortaleza, 11 de outubro de 1993), mais conhecido como Matuê, é um rapper, cantor, compositor, guitarrista e empresário brasileiro. Ficou
conhecido com o single "Anos Luz", lançado em 2017 e pelo álbum "Máquina do Tempo" lançado em 2020. É considerado um dos símbolos do trap brasileiro.[1][2]
                     
Foi o único artista de hip hop em 2023 a ter 10 músicas com mais de 100 milhões de streams nas plataformas digitais.[3]

Em setembro de 2024 lançou seu segundo álbum, chamado 333 conquistando com ele a maior estreia de um álbum da história do Spotify Brasil, contando com 16.8 milhões de reproduções nas primeiras 24 horas de lançamento, além de debutar em primeiro lugar no Spotify Global.
                    ''')
        elif artista == "Teto":
            st.markdown('''
Clériton Sávio Santos Silva (Jacobina, 19 de outubro de 2001), mais conhecido como Teto, é um rapper, cantor e compositor brasileiro.
Ficou conhecido por meio das prévias de suas músicas que foram lançadas não oficialmente em vários canais do YouTube, alcançando milhões de visualizações e ganhando fama em redes sociais como o TikTok e Instagram.[1][2]
                    ''')
            
        elif artista == "Alok":
            st.markdown('''
Alok Achkar Peres Petrillo (Goiânia, 26 de agosto de 1991) é um DJ e produtor musical brasileiro,[5] mais conhecido por seu sucesso mundial de 2016 "Hear Me Now".[6] É atualmente o 4.º melhor DJ do mundo segundo a revista britânica DJ Mag.[7]
                    ''')
            
        elif artista == "Marshmello":
            st.markdown('''
Christopher Comstock (nascido em 19 de maio de 1992), mais conhecido profissionalmente como Marshmello, é um produtor de música eletrônica e DJ norte-americano. Suas músicas "Silence" (com Khalid),
 "Wolves" (com Selena Gomez), "Friends" (com Anne-Marie), "Happier" (com Bastille) e "Alone" receberam certificações multiplatina em vários países,
alcançando o Top 40 da Billboard Hot 100.[1] Seu estilo musical combina batidas orientadas para o groove, com forte uso de sintetizadores e baixos típicos da música eletrônica de dança. Marshmello também é conhecido por popularizar o future bass.[2][3]
                    ''')
            
        elif artista == "Barões Da Pisadinha":
            st.markdown('''
Os Barões da Pisadinha é uma banda musical brasileira de piseiro e tecnobrega formada por Rodrigo Barão e Felipe Barão em dezembro de 2015, nas cidades de Heliópolis e Ribeira do Amparo, ambas na Bahia.
O grande sucesso da banda é a música "Tá Rocheda", o grupo ganhou notoriedade nacional quando o jogador Neymar dançou a música e publicou em seu Instagram.[2]
                    ''')
            
        elif artista == "Gustavo Lima":
            st.markdown('''
Nivaldo Batista Lima (Presidente Olegário, 3 de setembro de 1989), mais conhecido pelo nome artístico Gusttavo Lima, é um cantor, compositor, produtor musical e empresário brasileiro.[2][3]

Gusttavo Lima possui uma fortuna avaliada em mais de 1 bilhão de reais, consolidando-se como um dos artistas mais ricos do Brasil.[4][5]
                    ''')
            
        elif artista == "Eminem":
            st.markdown('''
Marshall Bruce Mathers III (St. Joseph, 17 de outubro de 1972) mais conhecido pelo seu nome artístico Eminem, é um rapper, compositor, produtor musical e ator americano.
[2] Adquiriu rápida popularidade em 1999 com o lançamento do disco The Slim Shady LP, o qual venceu o Grammy Award de Melhor Álbum de Rap do ano.
[3] O seu próximo trabalho, The Marshall Mathers LP, se tornou o álbum solo mais vendido na história dos Estados Unidos.   
[4] Tal fato o tornou conhecido no mundo inteiro, e ajudou para a divulgação de sua gravadora, a Shady Records, e do seu grupo, o D12.
                        
                    ''')
            
        elif artista == "Snoop Dogg":
             st.markdown('''
Calvin Cordozar Broadus, Jr. (Long Beach, 20 de outubro de 1971), mais conhecido pelo seu nome artístico Snoop Dogg (anteriormente Snoop Doggy Dogg),
[a] é um rapper, compositor, produtor musical e ator estadunidense.[5] Enraizado no hip-hop da Costa Oeste, ele é amplamente considerado um dos maiores e mais influentes rappers de todos os tempos.                    
[6][7][8] Conhecido por suas letras arrastadas e características—que frequentemente usam rimas melódicas, repetições, jogo de palavras,                 
frases lacônicas, síncopes e aliterações—sua música frequentemente aborda o estilo de vida e a cultura da Costa Oeste e questões sociais como violência armada e estabilidade para os jovens.[9][10]
''')