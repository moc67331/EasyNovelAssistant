﻿import tkinter as tk
import webbrowser


class HelpMenu:

    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="ヘルプ", menu=self.menu)
        self.menu.configure(postcommand=self.on_menu_open)

    def on_menu_open(self):
        self.menu.delete(0, tk.END)

        sample_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="サンプル原典", menu=sample_menu)

        cmd = lambda: self._show_url("https://kakuyomu.jp/works/16818093074043995181")
        sample_menu.add_command(label="最新AI Claude 3で長編小説執筆支援【GPT-4を超えた!?】", command=cmd)

        cmd = lambda: self._show_url("https://kakuyomu.jp/works/16818093074043995181/episodes/16818093074305285059")
        sample_menu.add_command(label="↑ のプロンプトまとめ", command=cmd)

        cmd = lambda: self._show_url("https://rentry.org/gpt0721")
        sample_menu.add_command(label="5ch プロンプトまとめ", command=cmd)

        reference_menu = tk.Menu(self.menu, tearoff=False)

        self.menu.add_cascade(label="参照", menu=reference_menu)

        cmd = lambda: self._show_url("https://github.com/LostRuins/koboldcpp")
        reference_menu.add_command(label="LostRuins/KoboldCpp", command=cmd)

        self._show_hf_url(reference_menu, "Sdff-Ltba/LightChatAssistant-TypeB-2x7B-GGUF")
        self._show_hf_url(reference_menu, "mmnga/Vecteus-v1-gguf")
        self._show_hf_url(reference_menu, "mmnga/Ninja-v1-NSFW-128k-gguf")
        self._show_hf_url(reference_menu, "mmnga/Ninja-v1-128k-gguf")
        self._show_hf_url(reference_menu, "Aratako/LightChatAssistant-4x7B-GGUF")

        self._show_hf_url(reference_menu, "Aratako/SniffyOtter-7B-Novel-Writing-NSFW-GGUF")
        self._show_hf_url(reference_menu, "Aratako/Antler-7B-Novel-Writing-GGUF")

        self._show_hf_url(reference_menu, "Sdff-Ltba/LightChatAssistant-2x7B-GGUF")

        self._show_hf_url(reference_menu, "TFMC/Japanese-Starling-ChatV-7B-GGUF")
        self._show_hf_url(reference_menu, "umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf")
        self._show_hf_url(reference_menu, "Elizezen/SniffyOtter-7B-GGUF")

        self._show_hf_url(reference_menu, "andrewcanis/c4ai-command-r-v01-GGUF")
        self._show_hf_url(reference_menu, "dranger003/c4ai-command-r-plus-iMat.GGUF")
        self._show_hf_url(reference_menu, "pmysl/c4ai-command-r-plus-GGUF")

        reference_menu.add_separator()
        self._show_hf_url(reference_menu, "kaunista/kaunista-style-bert-vits2-models")
        self._show_hf_url(reference_menu, "RinneAi/Rinne_Style-Bert-VITS2")

        self.menu.add_separator()
        cmd = lambda: self._show_url("https://github.com/Zuntan03/EasyNovelAssistant")
        self.menu.add_command(label="EasyNovelAssistant", command=cmd)

    def _show_hf_url(self, menu, hf_name):
        cmd = lambda: self._show_url(f"https://huggingface.co/{hf_name}")
        menu.add_command(label=hf_name, command=cmd)

    def _show_url(self, url):
        webbrowser.open(url)
