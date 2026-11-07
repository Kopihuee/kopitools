from kopitools import Registry, RegistryError
import sys

general = Registry(sys.argv)
chat = Registry(sys.argv, entry_point="chat")
talk = Registry(sys.argv, entry_point="talk")

general.option(
    name="--num-ctx",
    receives=int,
    default=8192,
    attribute="num_ctx",
)

chat.option(
    name="--stream",
    receives=None,
    default=False,
    attribute="stream",
)

talk.option(
    name="--voice-model",
    receives=str,
    default="af_heart",
    attribute="voice_model",
)

general_args = general.collect()
chat_args = chat.collect()
talk_args = talk.collect()

if general_args is not None:
    print(general_args.get_all())

if chat_args is not None:
    print(chat_args.get_all())

if talk_args is not None:
    print(talk_args.get("voice_model"))
