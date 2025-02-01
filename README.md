# Renew IP Cam
Script em Python que testa faixa de IPs para uma camêra de segurança caseira. Fiz esse script pois o ISP que utilizo fornece um modem que não possibilita reserva de IP para os aparelhos conectados, então quase toda vez que falta luz ou que o serviço de internet é reiniciado os IPs são reatribuídos de forma aleatória - dessa forma, o script testa alguns IPs na faixa de IPs fornecida pelo gateway do modem até encontrar a resposta esperada pela câmera e então armazena o número num log - para não precisar fazer a busca nas próximas execuções. Desenvolvido para Linux, mas deve funcionar em Windows também com algumas adaptações.

Utiliza o protocolo RTSP (Real Time Streaming Protocol) com o ffplay (https://ffmpeg.org/ffplay.html) para reproduzir a imagem da câmera.

## Dependências

- Python 3
- ffplay/ffmpeg

