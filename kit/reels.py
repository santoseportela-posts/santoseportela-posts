"""Gera um Reels 1080x1920 (30 fps, MP4 H.264 + AAC silencioso) no padrão Santos & Portela.

Uso:
  python3 kit/reels.py roteiro.json saida.mp4             # vídeo completo
  python3 kit/reels.py roteiro.json pasta/ --stills 2,6,10 # só quadros de conferência (JPEG)
  python3 kit/reels.py roteiro.json saida.mp4 --capa       # só a capa (saida_capa.jpg)
O modo completo também grava saida_capa.jpg (1080x1920, 1ª cena completa), usada como cover_url
na publicação para o Reels não aparecer no perfil com a capa vazia.

roteiro.json:
{ "fundo": "escuro" | "claro",
  "cenas": [ {"kicker": "Você sabia?", "linhas": ["linha 1", "linha 2"], "em": "itálico dourado", "sub": "apoio", "dur": 4.5} ],
  "final_dur": 2.5 }
A logo é o PNG oficial (recortado pelo alfa), aplicado como imagem, nunca redesenhado.
"""
import json, os, pathlib, subprocess, sys
from playwright.sync_api import sync_playwright

KIT = pathlib.Path(__file__).resolve().parent
W, H, FPS = 1080, 1920, 30


def abrir(p, roteiro):
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    pg.add_init_script("window.ROTEIRO = " + json.dumps(roteiro, ensure_ascii=False) + ";")
    pg.goto((KIT / "reels.html").as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(300)
    return b, pg


def main():
    roteiro = json.load(open(sys.argv[1], encoding="utf-8"))
    saida = sys.argv[2]
    with sync_playwright() as p:
        b, pg = abrir(p, roteiro)
        total = pg.evaluate("window.TOTAL")
        if "--stills" in sys.argv:
            os.makedirs(saida, exist_ok=True)
            for t in [float(x) for x in sys.argv[sys.argv.index("--stills") + 1].split(",")]:
                pg.evaluate(f"setT({t})")
                pg.screenshot(path=f"{saida}/t{t:05.2f}.jpg", type="jpeg", quality=92)
            b.close(); print("stills ok"); return
        # Capa do Reels: quadro com a 1ª cena já completa (o 1º quadro do vídeo é só o fundo vazio).
        c0 = roteiro["cenas"][0]
        t_capa = min(3.0, float(c0.get("dur", 4.5)) - 0.6)
        pg.evaluate(f"setT({t_capa})")
        capa = saida[:-4] + "_capa.jpg"
        pg.screenshot(path=capa, type="jpeg", quality=92)
        print("capa", capa, f"t={t_capa}s")
        if "--capa" in sys.argv:
            b.close(); return
        tmp = saida[:-4] + ".tmp.mp4"
        ff = subprocess.Popen([
            "ffmpeg", "-y", "-loglevel", "error",
            "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
            "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
            "-map", "0:v", "-map", "1:a", "-shortest",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", tmp], stdin=subprocess.PIPE)
        n = int(round(total * FPS))
        for i in range(n):
            pg.evaluate(f"setT({i / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        ff.stdin.close()
        rc = ff.wait(); b.close()
        if rc != 0:
            sys.exit("ffmpeg falhou")
        os.replace(tmp, saida)
        print("ok", saida, f"{total:.1f}s", n, "quadros")


if __name__ == "__main__":
    main()
