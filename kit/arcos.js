/* Arcos do site santoseportela.com.br — mesmo desenho (quarto de anel: raio 200, miolo 110)
   usado em todas as seções do site, cada uma com uma composição diferente.
   Uso no post: <body class="escuro" data-arcos="coluna"> + <script src="../arcos.js"></script>
   Composições: coluna | canto | diagonal | s | trio | ancora
   Cada composição define uma zona livre para o texto (--text-top, --text-w) e nunca
   invade a faixa da logo (x 380–700, y 1140–1310). */
(function () {
  const Q = "M0 0 A200 200 0 0 1 200 200 L110 200 A110 110 0 0 0 0 90 Z";
  // [x, y, tamanho, rotação, espelhar, dourado] em coordenadas da peça 1080x1350
  const k = 1.15, ox = 390, oy = 250, s = 200 * k;
  const C = (X, Y, r, g) => [ox + X * k, oy + Y * k, s, r, false, !!g];
  const L = {
    // composição do topo do site (hero), com o único arco dourado
    coluna:   { top: 150, w: 690, arcs: [C(400,0,90), C(400,210,0), C(190,420,270), C(400,420,180,true), C(400,630,90), C(190,630,0)] },
    // um arco grande saindo do canto superior direito (seções Contato / História)
    canto:    { top: 470, w: 888, arcs: [[740, -200, 520, 0, false]] },
    // canto superior direito + canto inferior esquerdo (Trajetória / Equipe)
    diagonal: { top: 400, w: 800, arcs: [[800, -110, 390, 0, true], [-110, 1020, 330, 180, false]] },
    // "S" vertical à direita (seção Resumo executivo)
    s:        { top: 330, w: 640, arcs: [[790, 150, 330, 0, true], [790, 497, 330, 90, false]] },
    // três arcos iguais em linha no topo (Atuação / Certificações)
    trio:     { top: 520, w: 888, arcs: [[-40, -150, 330, 270], [375, -150, 330, 270], [790, -150, 330, 270]] },
    // um arco âncora na lateral esquerda, à meia altura (Quem somos)
    ancora:   { top: 260, w: 888, arcs: [[-150, 780, 400, 0, false]] },
  };
  const nome = document.body.dataset.arcos;
  const lay = L[nome];
  if (!lay) return;
  const escuro = document.body.classList.contains("escuro");
  const cor = escuro ? "#1A3557" : "#E9E1D3";
  const ouro = "#B07A3C";
  let g = "";
  const ky = 1350 / 1440;
  for (const [x, y0, t, r, flip, gold] of lay.arcs) {
    const y = y0 * ky;
    const f = flip ? " translate(200 0) scale(-1 1)" : "";
    g += `<path d="${Q}" fill="${gold ? ouro : cor}" transform="translate(${x} ${y}) scale(${t / 200})${f} rotate(${r} 100 100)"/>`;
  }
  const svg = `<svg class="arcos" viewBox="0 0 1080 1350" width="1080" height="1350" style="position:absolute;inset:0;z-index:0">${g}</svg>`;
  document.body.insertAdjacentHTML("afterbegin", svg);
  document.documentElement.style.setProperty("--text-top", Math.round(lay.top * 1350 / 1440) + "px");
  document.documentElement.style.setProperty("--text-w", lay.w + "px");
})();
