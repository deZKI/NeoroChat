from django.conf import settings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat


class GigaChatService:
    gigachat = GigaChat(credentials=settings.GIGACHAT, verify_ssl_certs=False)

    @staticmethod
    def get_response(query):
        messages = [
            SystemMessage(
                content="Ты — эксперт, способный давать квалифицированные ответы на запросы в различных областях: "
                        "рекламы, маркетинга, разработки, бизнеса, науки, технологий и других. "
                        "Ты понимаешь, как структурировать информацию, и можешь давать полезные советы или подробные объяснения."
            ),
            HumanMessage(content=f"Пользователь спрашивает: {query}")
        ]
        res = GigaChatService.gigachat.invoke(messages)
        return res.content
