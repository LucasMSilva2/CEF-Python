from cefpython3 import cefpython as cef
import os

S_CURRENT_DIR = os.path.dirname(__file__)

# Configuração do CEF Python
cef.Initialize()

# Classe para manipulação de eventos do navegador
class BrowserHandler(object):
    def OnLoadEnd(self, browser, **_):
        # Executa um script JavaScript após o carregamento da página
        browser.ExecuteJavascript("alert('A página foi carregada com sucesso!');")
    
    def OnBeforeClose(self, browser, **_):
        # Ao fechar a janela, encerra o loop de eventos
        cef.QuitMessageLoop()

# Criando a janela do navegador e definindo o manipulador de eventos
window_info = cef.WindowInfo()
window_info.SetAsChild(0, [0, 0, 800, 600])  # Defina as dimensões da janela aqui
browser = cef.CreateBrowserSync(url="file://"+os.path.join(S_CURRENT_DIR, "../d010/android.html") ,window_title="Exemplo CEF Python")
handler = BrowserHandler()
browser.SetClientHandler(handler)

# Loop de eventos do CEF Python
cef.MessageLoop()

# Finalização do CEF Python
cef.Shutdown()