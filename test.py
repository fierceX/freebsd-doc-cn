import polib
import argparse
import deepl
from openai import OpenAI
import os


class DeepL:
    def __init__(self) -> None:
        self.translator = deepl.Translator(os.environ.get("API_KEY"))
    def translation(self,msg,target_lang='zh',glossary=None):
        result = self.translator.translate_text(msg,target_lang=target_lang,split_sentences='nonewlines',glossary=glossary)
        return result.text

class ChatGPT:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=os.environ.get("API_KEY"))
    def translation(self,msg):
        message = [
            {
                "role": "system",
                "content": f"你是一位技术译员，精通中文和英文，并且是一位计算机和freebsd专家，熟练掌握asciidoc格式的规范，知道如何处理相关标签以及计算机和 freebsd 术语。\n 请将下面的文本翻译为中文，正确处理 asciidoc 标签以及和 freebsd 以及计算机相关的术语，直接返回译文。",
            },
            {
                "role": "user",
                "content": msg
            }
        ]
        chat_completion = self.client.chat.completions.create(
            messages=message,
            model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content


cl = ChatGPT()
print(cl.translation('This chapter covers the basic commands and functionality of the FreeBSD operating system.  Much of this material is relevant for any UNIX(R)-like operating system.  New FreeBSD users are encouraged to read through this chapter carefully.'))