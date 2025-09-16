import gradio as gr

from .api import tts

available_voices = [
    ("Female 2 🚺", "expr-voice-2-f"),
    ("Male 2 🚹", "expr-voice-2-m"),
    ("Male 3 🚹", "expr-voice-3-m"),
    ("Female 3 🚺", "expr-voice-3-f"),
    ("Male 4 🚹", "expr-voice-4-m"),
    ("Female 4 🚺", "expr-voice-4-f"),
    ("Male 5 🚹", "expr-voice-5-m"),
    ("Female 5 🚺", "expr-voice-5-f"),
]


def kitten_tts_ui():
    gr.Markdown(
        """
    # Kitten TTS Mini 0.1 (CPU - ONNX)
    """
    )

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Input")
            voice = gr.Dropdown(choices=available_voices, label="Voice")
            model_name = gr.Dropdown(
                choices=["KittenML/kitten-tts-mini-0.1", "KittenML/kitten-tts-nano-0.2", "KittenML/kitten-tts-nano-0.1"],
                value="KittenML/kitten-tts-mini-0.1",
                label="Model",
            )
            button = gr.Button("Process")
        with gr.Column():
            output_text = gr.Audio(label="Output")

    button.click(
        fn=tts,
        inputs=[model_name, input_text, voice],
        outputs=[output_text],
        api_name="kitten_tts",
    )


def extension__tts_generation_webui():
    kitten_tts_ui()

    return {
        "package_name": "extension_kitten_tts",
        "name": "Kitten tts",
        "requirements": "git+https://github.com/rsxdalv/extension_kitten_tts@main",
        "description": "A template extension for TTS Generation WebUI",
        "extension_type": "interface",
        "extension_class": "text-to-speech",
        "author": "KittenML",
        "extension_author": "rsxdalv",
        "license": "MIT",
        "website": "https://github.com/rsxdalv/extension_kitten_tts",
        "extension_website": "https://github.com/rsxdalv/extension_kitten_tts",
        "extension_platform_version": "0.0.1",
    }


if __name__ == "__main__":
    if "demo" in locals():
        locals()["demo"].close()
    with gr.Blocks() as demo:
        with gr.Tab("Kitten tts", id="kitten_tts"):
            kitten_tts_ui()

    demo.launch(
        server_port=7772,  # Change this port if needed
    )
