import openai

# Pega aquí tu clave de Azure OpenAI
openai.api_key = "TU_API_KEY"

def chat_with_copilot():
    print("Escribe 'salir' para terminar la conversación.")
    wwhile True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Copilot: ¡Hasta luego!")
            break

        # Aquí se hace la llamada al modelo
        response = openai.ChatCompletion.create(
            model="gpt-4",  # o el modelo que tengas habilitado en Azure
            messages=[{"role": "user", "content": user_input}]
        )

        # Mostrar mi respuesta
        print("Copilot:", response["choices"][0]["message"]["content"])

chat_with_copilot()
