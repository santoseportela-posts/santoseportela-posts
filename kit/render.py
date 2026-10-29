"""Renderizador de posts Santos & Portela.

Uso: python3 render.py <post.html> <saida.png> <claro|escuro>

1. Renderiza o HTML da peça (sem logo) em 1080x1350 com Chromium headless.
2. Aplica o PNG OFICIAL da logo como camada (recorte pelo alfa, sem
   distorcer, recolorir ou redesenhar), centralizado no rodapé,
   260 px de largura (24% da peça), topo em y=1165, igual aos posts anteriores.
"""
import sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

KIT = pathlib.Path(__file__).resolve().parent
W, H = 1080, 1350
LOGO_W, LOGO_TOP = 260, 1165


def render(html_path, out_path, fundo):
    html_path = pathlib.Path(html_path).resolve()
    base_png = pathlib.Path(out_path).with_suffix(".base.png")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto(html_path.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(base_png), clip={"x": 0, "y": 0, "width": W, "height": H})
        b.close()

    arte = Image.open(base_png).convert("RGBA")
    nome = "logo_fundo_claro.png" if fundo == "claro" else "logo_fundo_escuro.png"
    logo = Image.open(KIT / "logos" / nome).convert("RGBA")
    logo = logo.crop(logo.getbbox())
    h = round(logo.height * LOGO_W / logo.width)  # mantém a proporção
    logo = logo.resize((LOGO_W, h), Image.LANCZOS)
    arte.alpha_composite(logo, ((W - LOGO_W) // 2, LOGO_TOP))
    arte.convert("RGB").save(out_path, optimize=True)
    base_png.unlink()
    print("ok", out_path)


if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2], sys.argv[3])
