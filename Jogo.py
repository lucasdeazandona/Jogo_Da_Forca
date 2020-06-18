from Seta_Jogadores import AjustaJogadores
from ValidaPalavra import ValidacaoPalavras
from ValidaTentativasDesafiado import ValidateTentativas

print('Bem Vindo ao Jogo da Forca!')

print('Este jogo e composto por 2 jogadores, sendo um que ira colocar uma palavra, '
      'e outro que ira adivinhala!', 'S')

FimdeJogo = False
vPalavraDesafiador = ''

while not FimdeJogo:
    JogadorDesafiador, JogadorDesafiado = AjustaJogadores.GetJogadores()

    vPalavraDesafiador = ValidacaoPalavras.Valida_Palavra_Desafiador(JogadorDesafiado)
    FimdeJogo = ValidateTentativas.Validate_Tentativas_Desafiado(vPalavraDesafiador)



