# Rotina diária: post do Instagram @_santoseportelalicitacoes

Executada todos os dias, perto das 8h (horário de Brasília), por uma tarefa agendada.
Publicação **automática, sem aprovação prévia**, conforme autorizado pelo cliente em 29/10/2026.

## Fontes obrigatórias
1. Instruções do projeto "GABRIEL - DIRETOR CRIATIVO" e a `Base_Mestre_FINAL_Gabriel_Santos_Portela.docx`.
   Use **somente** os fatos e números oficiais listados nas instruções do projeto (Seção 1).
2. Este repositório: `kit/` (render.py, base.css, arcos.js, logos oficiais) e `posts/historico.json`.

## Regras fixas de formato (aprovadas pelo cliente)
- 1080×1350 (4:5), JPEG. Instagram não aceita 3:4 via API.
- Fundo do site: `body.escuro` ou `body.claro` (base.css). Alternar escuro/claro em relação ao último post.
- Arcos do site via `data-arcos`: coluna | canto | diagonal | s | trio | ancora.
  Não repetir a composição de nenhum dos últimos 3 posts. "coluna" (com arco dourado) no máximo 1x por semana.
- **Sem barras, filetes, linhas, ícones, listas, caixas, selos ou CTA na arte.**
- Texto: headline (serifada, 2ª parte em itálico dourado via `<em>`) + no máximo 1 subheadline curta. Nada mais.
- Logo: nunca escrever/desenhar. O `render.py` aplica o PNG oficial no rodapé automaticamente.
- Fonte provisória: TeX Gyre Pagella (até o cliente enviar a The Seasons).

## Pilares (girar; não repetir o pilar do dia anterior)
1. Expertise e números oficiais (R$ 9,8 bi+, 28 mil+ processos, 115+ clientes, 17 anos, 123 órgãos, 36 clientes há 10+ anos).
2. O que fazemos pelos clientes (captação nacional, gestão completa, inteligência competitiva, atuação jurídica, Key Account, resumo executivo).
3. Como licitações ajudam empresas a faturar mais (receita recorrente, contratos, previsibilidade, expansão de território) — sem prometer vitória nem inventar números.
4. Sobre licitações (Lei 14.133/2021, erros que custam contrato: documento, prazo, preço, habilitação).
5. Sobre a assessoria (método Estratégia → Execução → Segurança, dois lados do balcão, certificações).
6. Segmentos (um por vez: Limpeza, Obras, Tecnologia, Saúde, Alimentação, Transporte, Segurança, Mobiliário, Medicamentos, Engenharia).
Público: donos, sócios, CEOs e diretores de empresas de médio e grande porte e empreendedores.

## Passo a passo
1. Ler `posts/historico.json` (últimos 10). Escolher pilar, mecanismo, composição e fundo que não repitam.
2. Processo Gabriel: tese → 5 conceitos → filtro de clichê → headline. Não repetir headline nem ideia já usada.
3. Escrever `posts/AAAA-MM-DD_slug.html` (modelo: `posts/2026-10-29_9-8-bilhoes.html`).
4. Renderizar: `python3 kit/render.py posts/X.html /tmp/X.png escuro|claro`, converter para JPEG qualidade 90
   em `posts/X.jpg` e **abrir a imagem para conferir** (texto cortado, sobreposição com arcos ou logo, ortografia).
5. QA de 15 itens da Base Mestre. Qualquer NÃO relevante: refazer. Nunca número, cliente ou prova inventados.
6. Legenda: gancho, 2–4 frases, CTA "O próximo contrato começa com uma conversa. Fale com nosso time: (11) 93624-7039." e 3–5 hashtags.
7. Acrescentar a entrada em `posts/historico.json`, commit e push para `main`.
8. Aguardar ~60 s. URL da imagem:
   `https://raw.githubusercontent.com/santoseportela-posts/santoseportela-posts/main/posts/X.jpg`
9. Publicar com Windsor.ai: connector `instagram`, action `create_image_post`, account `17841467778795999`,
   params `{image_url, caption}`. Se falhar, tentar 1 vez após 2 min. Não publicar duas vezes no mesmo dia.
10. Atualizar o status no histórico (publicado / falhou + motivo), commit e push.
11. Enviar ao cliente uma mensagem curta com a headline, a imagem e o resultado da publicação.
