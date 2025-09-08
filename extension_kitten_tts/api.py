from tts_webui.utils.manage_model_state import manage_model_state


@manage_model_state("kitten_tts")
def get_model(repo="KittenML/kitten-tts-mini-0.1"):
    from kittentts import KittenTTS

    m = KittenTTS(repo)
    return m


def tts(model_name, text, voice):
    m = get_model(model_name)
    audio = m.generate(text, voice=voice)
    return (24000, audio)
