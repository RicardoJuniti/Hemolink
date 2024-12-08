import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import threading
#from gpt4all import GPT4All  #Chatbot
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle,Line
from kivy.uix.scrollview import ScrollView
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
# Caminho do seu modelo
#model_path = "C:/Users/ricar/Downloads/Meta-Llama-3-8B-Instruct.Q4_0.gguf"

Window.orientation = 'portrait'
Window.size = (1080, 2200)
class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        layout = FloatLayout()

        # Cor de fundo
        with self.canvas.before:
            self.logo_image = Image(source='Modelo de fundo com logo.png', allow_stretch=True, keep_ratio=False)
            self.logo_image.size = self.size
            self.add_widget(self.logo_image)

        # Botões
        buttonLogin = Button(
            text="LOG IN",
            size_hint=(0.4, 0.08),
            pos_hint={'x': 0.05, 'y': 0.05},
            background_normal='',
            background_color=(0.827, 0.827, 0.827, 1),
            color=(0, 0, 0, 1),  # Texto preto
            font_size=30,
            bold=True
        )
        buttonLogin.bind(on_press=self.go_to_screen1)


        buttonRegister = Button(
            text="REGISTER",
            size_hint=(0.4, 0.08),
            pos_hint={'right': 0.95, 'y': 0.05},
            background_normal='',
            background_color=(1, 0, 0, 1),  # Vermelho
            color=(1, 1, 1, 1),  # Texto branco
            font_size=30,
            bold=True
        )

        layout.add_widget(buttonRegister)  
        layout.add_widget(buttonLogin)
        self.add_widget(layout)

    def go_to_screen1(self, instance):
        self.manager.current = 'screen1'
# Tela Home
class TelaHome(Screen):
    def __init__(self, **kwargs):
        super(TelaHome, self).__init__(**kwargs)
        layout = FloatLayout()

        # Cor de fundo
        with self.canvas.before:
            self.logo_image = Image(source='fundohome.png', allow_stretch=True, keep_ratio=False)
            self.logo_image.size = self.size
            self.add_widget(self.logo_image)
        
        # Lista de tipos de sangue e imagens

        # Lista de imagens dos centros de coleta
        scroll_view2 = ScrollView(
            size_hint=(1, 0.2),
            pos_hint={'center_x': 0.51, 'y': 0.58},
            do_scroll_x=True,
            do_scroll_y=False
        )
        
        # Layout horizontal para os ícones
        title_label2 = Label(
            text="Centros de coleta:",
            font_size=30,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.13, 'y': 0.75}  # Posição acima do ScrollView
        )
        self.add_widget(title_label2)
        icon_layout2 = GridLayout(
            cols=10,  # Número de colunas (ajustável)
            size_hint = (None,None),  # Define largura manualmente
            height=10,
            row_default_height=300,
            row_force_default=True,
            spacing=10
        )
        icon_layout2.bind(minimum_width=icon_layout2.setter('width'))

        class IconButton(ButtonBehavior, Image):
            """Um botão que também exibe uma imagem."""
            pass
        imagens2 = ["centro_coleta1.png","centro_coleta2.png","centro_coleta3.png","centro_coleta4.png"]  # Caminhos das imagens
        for img_path in imagens2:
            # Adicionar como botão interativo com imagem
            btn = IconButton(source=img_path, allow_stretch=True, keep_ratio=True, size_hint=(None, None))
            btn.size = (300, 300)  # Tamanho padrão, mas será ajustado
            btn.bind(on_press=self.go_to_screen4)
            icon_layout2.add_widget(btn)
        max_height = 300  # Altura máxima permitida para o ScrollView
        image_size = 300  # Altura de cada imagem (ajuste conforme necessário)
        spacing = 10  # Espaçamento entre imagens
        total_width = len(imagens2) * (image_size + spacing)  # Largura total do layout
        icon_layout2.width = total_width
        scroll_view2.height = min(max_height, image_size + spacing)  # Limita altura ao máximo permitido
        # Adicionando o layout ao ScrollView
        scroll_view2.add_widget(icon_layout2)

        # Adicionando o ScrollView ao layout principal
        self.add_widget(scroll_view2)


        # Botões
        buttonChat = Button(
            size_hint=(0.2, 0.145),
            pos_hint={'center_x': 0.1, 'y': 0.02},
            background_normal='image 10.png',
            background_down='image 10.png'
        )
        buttonChat.bind(on_press=self.go_to_screen2)
        

        buttonHome = Button(
            size_hint=(0.25, 0.14),
            pos_hint={'center_x': 0.49, 'y': 0.02},
            background_normal='homeicon.png',
            background_down='homeicon.png'
        )

        buttonforms = Button(
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.9, 'y': 0.04},
            background_normal='adicionar.png',
            background_down=''
        )
        buttonforms.bind(on_press=self.go_to_screen4)
        

        layout.add_widget(buttonforms)  
        layout.add_widget(buttonChat)
        layout.add_widget(buttonHome)
        self.add_widget(layout)
        scroll_view = ScrollView(
            size_hint=(1, 0.26),
            pos_hint={'center_x': 0.51, 'y': 0.2},
            do_scroll_x=True,
            do_scroll_y=False
        )
        
        # Layout horizontal para os ícones
        title_label = Label(
            text="Promoções:",
            font_size=30,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.09, 'y': 0.5}  # Posição acima do ScrollView
        )
        self.add_widget(title_label)
        icon_layout = GridLayout(
            cols=10,  # Número de colunas (ajustável)
            size_hint = (None,None),  # Define largura manualmente
            height=10,
            row_default_height=300,
            row_force_default=True,
            spacing=10
        )
        icon_layout.bind(minimum_width=icon_layout.setter('width'))
        def show_highlighted_image(img_path):
            popup_content = Image(source=img_path, allow_stretch=True, keep_ratio=True)
            popup = Popup(
                title="Promoção em Destaque",
                content=popup_content,
                size_hint=(0.8, 0.8),  # Tamanho do popup
                auto_dismiss=True
            )
            popup.open()
        class IconButton(ButtonBehavior, Image):
            """Um botão que também exibe uma imagem."""
            pass
        imagens = ["Ad1.png", "Ad2.png", "Ad3.png", "Ad4.png","Ad5.png","Ad6.png","Ad7.png","Ad8.png"]  # Caminhos das imagens
        for img_path in imagens:
            # Adicionar como botão interativo com imagem
            btn = IconButton(source=img_path, allow_stretch=True, keep_ratio=True, size_hint=(None, None))
            btn.size = (300, 300)  # Tamanho padrão, mas será ajustado
            btn.bind(on_press=lambda instance, path=img_path: show_highlighted_image(path))
            icon_layout.add_widget(btn)
        max_height = 350  # Altura máxima permitida para o ScrollView
        image_size = 350  # Altura de cada imagem (ajuste conforme necessário)
        spacing = 10  # Espaçamento entre imagens
        total_width = len(imagens) * (image_size + spacing)  # Largura total do layout
        icon_layout.width = total_width
        scroll_view.height = min(max_height, image_size + spacing)  # Limita altura ao máximo permitido
        # Adicionando o layout ao ScrollView
        scroll_view.add_widget(icon_layout)

        # Adicionando o ScrollView ao layout principal
        self.add_widget(scroll_view)


    def go_to_screen2(self, instance):
        self.manager.current = 'screen2'
    def go_to_screen3(self, instance):
        self.manager.current = 'screen3'
    def go_to_screen4(self, instance):
        self.manager.current = 'screen4'


# Tela 2
class TelaChat(Screen):
    def __init__(self, **kwargs):
        super(TelaChat, self).__init__(**kwargs)
        #self.model = GPT4All(model_path)
        layout = FloatLayout()
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Cor branca (R, G, B, A), onde A (alpha) é opacidade
            self.rect = Rectangle(size=self.size, pos=self.pos)

        with self.canvas.before:
            self.logo_image = Image(source='fundo branco.png', allow_stretch=True, keep_ratio=False)
            self.logo_image.size = self.size
            self.add_widget(self.logo_image)
        self.bind(size=self.update_rect, pos=self.update_rect)
        # Título da Tela 2
        layout.add_widget(Label(text='Tela 2', font_size=32, pos_hint={'center_x': 0.5, 'top': 0.9}, size_hint=(1, 0.2)))
    
        # Botões
        buttonChat = Button(
            size_hint=(0.2, 0.145),
            pos_hint={'center_x': 0.1, 'y': 0.02},
            background_normal='image 10.png',
            background_down='image 10.png'
        )
        buttonHome = Button(
            size_hint=(0.25, 0.14),
            pos_hint={'center_x': 0.49, 'y': 0.02},
            background_normal='homeicon.png',
            background_down='homeicon.png'
        )
        buttonHome.bind(on_press=self.go_to_screen1)

        buttonforms = Button(
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.9, 'y': 0.04},
            background_normal='adicionar.png',
            background_down='adicionar.png'
        )
        buttonforms.bind(on_press=self.go_to_screen4)
        

        # Caixa de entrada de texto
        self.text_input = TextInput(hint_text="Digite sua dúvida aqui", size_hint=(0.6, 0.06), pos_hint={'x': 0.15, 'top': 0.22})
        layout.add_widget(self.text_input)

        # Caixa de saída
        self.output_prompt = TextInput(hint_text="As respostas geradas podem ser imprecisas, por isso é recomendável consultar um banco de saúde ou profissionais da área para obter informações precisas e atualizadas", size_hint=(0.7, 0.7), pos_hint={'center_x': 0.5, 'top': 0.95}, multiline=True, readonly=True,font_size=30)
        layout.add_widget(self.output_prompt)

        # Botão para enviar
        buttonEnter = Button(size_hint=(0.12, 0.1), pos_hint={'x':0.75, 'top': 0.245},background_normal='enviar.png')
        buttonEnter.bind(on_press=self.generate_output)
        layout.add_widget(buttonEnter)

        self.label = Label(text='', font_size=24, pos_hint={'center_x': 0.5, 'top': 0.5}, size_hint=(1, 0.1))
        layout.add_widget(self.label)
        layout.add_widget(buttonHome)
        layout.add_widget(buttonChat)
        layout.add_widget(buttonforms)
        self.add_widget(layout)
        scroll_view = ScrollView(
            size_hint=(1, 0.3),
            pos_hint={'center_x': 0.5, 'y': 0.3},
            do_scroll_x=True,
            do_scroll_y=False
        )

    def go_to_screen1(self, instance):
        self.manager.current = 'screen1'
    def go_to_screen3(self, instance):
        self.manager.current = 'screen3'
    def go_to_screen4(self, instance):
        self.manager.current = 'screen4'

    def generate_output(self, instance):
        # Obtém o texto digitado na caixa de input
        user_input = self.text_input.text
        if not user_input:
            # Se estiver vazio, exibe uma mensagem de alerta na caixa de saída
            self.output_prompt.text += "Por favor, insira um texto válido.\n"
            return
        # Exibe o texto do usuário
        self.output_prompt.text = f"Você: {user_input}\n"
        self.output_prompt.text += "Chatbot: ...\n"
        
        # Cria uma thread para chamar a API do chatbot
        threading.Thread(target=self.call_chatbot_api, args=(user_input,)).start()

    def call_chatbot_api(self, user_input):
        # Carrega o modelo
        #model = GPT4All(model_path)
        

        # Gera a resposta do modelo
        prompt = "Você é um assistente virtual português brasileiro especializado em saúde. Responda de forma objetiva, educada e em um parágrafo curto, somente em português sobre questões relacionadas à doação de sangue."
        #resposta = model.generate(prompt + user_input)
        resposta = "Você pode doar sangue após realizar uma tatuagem, desde que tenha decorrido pelo menos seis meses desde a data da procedura. Isso porque o processo de cicatrização e cura das lesões causadas pela tatuagem pode levar alguns meses para ser concluído, e é importante garantir que seu sangue esteja livre de qualquer substância ou agente potencialmente prejudicial à saúde dos pacientes receptores."
        respostacurta = resposta.split("\n\n")[0]
    
        respadicional =  "\n**Lembre-se**: As respostas podem ser imprecisas. É sempre recomendável consultar um banco de sangue ou um médico para informações mais precisas sobre sua saúde."
        resptotal = respostacurta +respadicional
        # Agenda a atualização da interface
        Clock.schedule_once(lambda dt: self.update_output(resptotal))

    def update_output(self, chatbot_reply):
        # Atualiza a caixa de prompt com a resposta do chatbot
        self.output_prompt.text += f"Chatbot: {chatbot_reply}\n"
        # Faz a caixa rolar automaticamente para o final
        self.output_prompt.cursor = (0, 0)
    def update_rect(self, instance, value):
        # Atualiza a posição e o tamanho do Rectangle (fundo branco)
        self.rect.pos = instance.pos
        self.rect.size = instance.size   
class TelaPdf(Screen):
    def __init__(self, **kwargs):
        super(TelaPdf, self).__init__(**kwargs)
        layout = FloatLayout()
        
        self.file_chooser = FileChooserIconView(
            size_hint=(0.9, 0.7),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            filters=['*.pdf']  # Filtra apenas arquivos PDF
        )
        layout.add_widget(self.file_chooser)

        # Botão de Enviar
        enviar_button = Button(
            text="Enviar",
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.3, 'y': 0.05},
            background_color=(0, 1, 0, 1)
        )
        enviar_button.bind(on_press=self.enviar_arquivo)
        layout.add_widget(enviar_button)


        # Botão para voltar à tela anterior
        button_back = Button(size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5, 'y': 0.05}, text="Voltar")
        button_back.bind(on_press=self.voltar)
        layout.add_widget(button_back)

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'screen1'

    def enviar_arquivo(self, instance):
        # Obtém o caminho do arquivo selecionado
        arquivo_selecionado = self.file_chooser.selection
        if arquivo_selecionado:
            # Simula o envio do arquivo (substituir por lógica real de envio)
            self.status_label.text = f"Arquivo enviado: {arquivo_selecionado[0]}"
        else:
            self.status_label.text = "Por favor, selecione um arquivo PDF."
class Telacentro(Screen):
    def __init__(self, **kwargs):
        super(Telacentro, self).__init__(**kwargs)
        layout = FloatLayout()

        # Definindo o fundo da tela
        with self.canvas.before:
            self.logo_image = Image(source='fundo branco.png', allow_stretch=True, keep_ratio=False)
            self.logo_image.size = self.size
            self.add_widget(self.logo_image)

        # Título
        title_labelcentro = Label(
            text="Centros de Coleta:",
            font_size=40,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.9}  # Ajusta o título no topo
        )
        self.add_widget(title_labelcentro)

        # ScrollView para exibir os centros de coleta
        scroll_viewcentros = ScrollView(
            size_hint=(1, 0.7),
            pos_hint={'center_x': 0.5, 'y': 0.15},
            do_scroll_x=False,
            do_scroll_y=True
        )

        # Layout para os ícones com texto à direita
        layoutcentro = GridLayout(
            cols=1,  # Colocando apenas uma coluna
            size_hint=(None, None),
            width=Window.width,
            height=2000,  # Define uma altura fixa maior para garantir que a rolagem funcione corretamente
            row_default_height=150,
            row_force_default=True,
            spacing=10
        )

        # Função para exibir uma imagem destacada
        def show_highlighted_image(img_path, description):
            # Layout para o conteúdo do popup
            box_layout = BoxLayout(orientation='horizontal')
            img_popup = Image(source=img_path, allow_stretch=True, keep_ratio=True)
            label_popup = Label(text=description, size_hint=(0.5, 1), text_size=(None, None), halign='left', valign='top')
            box_layout.add_widget(img_popup)
            box_layout.add_widget(label_popup)

            popup = Popup(
                title="Detalhes do Centro de Coleta",
                content=box_layout,
                size_hint=(0.8, 0.8),
                auto_dismiss=True
            )
            popup.open()
            # Botões
        buttonChat = Button(
            size_hint=(0.2, 0.145),
            pos_hint={'center_x': 0.1, 'y': 0.02},
            background_normal='image 10.png',
            background_down='image 10.png'
        )
        buttonChat.bind(on_press=self.go_to_screen2)
        

        buttonHome = Button(
            size_hint=(0.25, 0.14),
            pos_hint={'center_x': 0.49, 'y': 0.02},
            background_normal='homeicon.png',
            background_down='homeicon.png'
        )
        buttonHome.bind(on_press=self.go_to_screen1)

        buttonforms = Button(
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.9, 'y': 0.04},
            background_normal='adicionar.png',
            background_down=''
        )
        buttonforms.bind(on_press=self.go_to_screen4)
        layout.add_widget(buttonforms)  
        layout.add_widget(buttonChat)
        layout.add_widget(buttonHome)
        self.add_widget(layout)
   
        
        
        # Imagens, descrições e horários de funcionamento dos centros de coleta
        centros = [
            {"img": "centro_coleta1.png", "name": "Hospital Estadual Mário Covas", "address": "Rua Dr. Henrique Calderazzo 321.", "hours": "Seg a sab 07:30 às 13:00"},
            {"img": "centro_coleta2.png", "name": "GSH Santo andré", "address": "Av. Dom Pedro II, 877 - Jardim, Santo André - SP, 09080-001.", "hours": "Seg a sab 07:00 às 12:00"},
            {"img": "centro_coleta3.png", "name": "a+ Medicina Diagnóstica", "address": "Av. Dom Pedro II, 293 - Jardim, Santo André - SP, 09080-110", "hours": "Seg a sex:06:30 às 22:00 ; sex a dom::06:30 às 12:00 "},
            {"img": "centro_coleta4.png", "name": "Centro De Ref Em Saude Da Mulher Criança E Adolescente", "address": "R. Luís Lacava, 229 - Vila Bocaina, Mauá - SP, 09310-080.", "hours": "Seg a qui: 08:00 às 17:00"},
        ]
        # Layout vertical para exibir os itens
        main_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,  # Permite definir altura manualmente
            spacing=15  # Espaçamento entre os itens
        )
        main_layout.bind(minimum_height=main_layout.setter('height'))  # Ajusta a altura total do layout

        for centro in centros:
            # Layout para exibir a imagem e o texto ao lado
            box_layout = BoxLayout(
                orientation='horizontal',  # Coloca a imagem à esquerda e o texto à direita
                size_hint_y= None,
                height=515,  # Altura de cada item (ajuste conforme necessário)
                spacing=50  # Espaço entre imagem e texto
            )

            # Botão com imagem
            btn = Button(
                size_hint=(None, None),
                size=(500, 300),
                background_normal=centro["img"],
                background_down=centro["img"]
            )

            # Texto descritivo ao lado da imagem, com nome do centro, endereço e horário
            label = Label(
                text=f"{centro['name']}\n{centro['address']}\n{centro['hours']}",
                size_hint=(None, 1),
                width=Window.width - 300,  # Largura do texto
                halign='left',
                valign='middle',
                color=(0, 0, 0, 1),
                text_size=(Window.width - 300, 450),  # Define que o texto deve quebrar para caber
                font_size = 30
            )
            label.bind(size=label.setter('text_size'))  # Faz o texto se ajustar automaticamente

            # Adiciona o botão e o texto no layout horizontal
            box_layout.add_widget(btn)
            box_layout.add_widget(label)

            # Adiciona o layout horizontal ao layout principal
            main_layout.add_widget(box_layout)

        # Cria um ScrollView para permitir rolagem
        scroll_view = ScrollView(size_hint=(1, 0.7),  # Permite definir altura manualmente
            height=Window.height - 100,  # Altura total da janela menos a altura da linha preta
            pos_hint={"x": 0, "y": 0.2}  # Move o ScrollView para começar acima da linha preta
)
        scroll_view.add_widget(main_layout)

        # Adiciona o ScrollView à tela
        self.add_widget(scroll_view)

 

    def voltar(self, instance):
        self.manager.current = 'screen1'  # Altere para o nome correto da tela anterior
    def go_to_screen2(self, instance):
        self.manager.current = 'screen2'
    def go_to_screen3(self, instance):
        self.manager.current = 'screen3'
    def go_to_screen4(self, instance):
        self.manager.current = 'screen4'
    def go_to_screen1(self, instance):
        self.manager.current = 'screen1'

# Aplicativo Principal
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='screenlogin'))
        sm.add_widget(TelaHome(name='screen1'))
        sm.add_widget(TelaChat(name='screen2'))
        sm.add_widget(TelaPdf(name='screen3'))
        sm.add_widget(Telacentro(name='screen4'))
      
        return sm


# Rodando o Aplicativo
if __name__ == '__main__':
    MyApp().run()
