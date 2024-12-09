Hemolink é um aplicativo móvel desenvolvido em Python com a biblioteca Kivy. Ele facilita a gestão de doações de sangue e centros de coleta, permitindo aos usuários visualizar informações sobre estoques de sangue e localizar centros de doação.

Funcionalidades
Visualização dos níveis de estoque de sangue de diferentes tipos sanguíneos.
Listagem e localização de centros de coleta de sangue, incluindo imagens e endereços.
Interface amigável para dispositivos móveis.
Tecnologias Utilizadas
Python 3
Kivy: Para desenvolvimento da interface gráfica.
Buildozer: Para compilar o aplicativo em um APK.
Python-for-Android: Para gerar o pacote Android.
Pré-requisitos
Antes de executar o projeto, certifique-se de ter instalado:

Python 3.9+
Virtualenv (opcional, mas recomendado)
Buildozer
Android NDK e SDK (para gerar o APK)
Como Executar
Clone o repositório:

git clone https://github.com/seu-usuario/Hemolink.git
cd Hemolink

Crie um ambiente virtual e ative-o (opcional):
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instale as dependências:
pip install -r requirements.txt

Execute o aplicativo:
python main.py

Para gerar o APK do aplicativo:

Certifique-se de que Buildozer está instalado:
pip install buildozer

Configure o arquivo buildozer.spec (gerado automaticamente na primeira execução do Buildozer):
buildozer init

Compile o APK:
buildozer -v android debug
O APK estará disponível no diretório bin/.

Contribuição
Contribuições são bem-vindas! Para contribuir:

Faça um fork do repositório.
Crie uma branch para sua funcionalidade: git checkout -b minha-funcionalidade.
Faça um commit das suas alterações: git commit -m 'Minha nova funcionalidade'.
Envie para o repositório remoto: git push origin minha-funcionalidade.
Abra um Pull Request.
