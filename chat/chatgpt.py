import openai
from kivymd.uix.screen import MDScreen

class Gpt(MDScreen):
    def __init__(self, **kwargs):
        super(Gpt, self).__init__(**kwargs)
        self.k = ""  # Déclarer k comme un attribut de la classe

    def chat_gpt_function(self):
        openai.api_key = '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'
      
        prompt = self.ids.user_input.text

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ])
            # Stocker la réponse générée dans l'attribut k
        self.k = completion['choices'][0]['message']['content']

    def on_send_message(self):
        self.chat_gpt_function()
        # Utiliser self.k pour mettre à jour le texte du label
        self.ids.label_id.text = self.k
        self.ids.user_input.text = ''

    def on_enter(self, *args):
        pass
