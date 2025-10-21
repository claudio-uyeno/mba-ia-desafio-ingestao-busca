import os
from search import search_prompt
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

def main():

    llm = init_chat_model(os.getenv("LLM_MODEL"), model_provider="google_genai")

    while True:
        try:
            question = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
            if question.lower() in ('sair', 'exit', 'quit'):
                print("Encerrando o chat.")
                break

            prompt = search_prompt(question)
            result = llm.invoke(prompt)

            print(f"\nResposta:\n{result.content}")

        except KeyboardInterrupt:
            print("\nChat encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"Erro ao processar a pergunta: {e}")
            continue

if __name__ == "__main__":
    main()