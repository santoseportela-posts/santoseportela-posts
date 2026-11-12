# Rotinas diárias do Instagram @santoseportela.franquia

Pedido do cliente em 12/11/2026: **publicação automática, como a da Santos & Portela**, com
**1 post de feed e 1 Reels por dia**, todos os dias, para atrair consultores, especialistas, profissionais
e analistas de licitações, empresários e investidores a se tornarem franqueados. Mostrar os resultados da
marca e o que o franqueado recebe. Publicação **sem aprovação prévia** (autorizada pelo cliente em 12/11/2026).

- **Post de feed:** no ar por volta das 10h (America/Sao_Paulo).
- **Reels:** no ar por volta das 19h.
Os horários ficam fora dos posts da @_santoseportelalicitacoes (8h, 12h30, 17h).

## Fontes obrigatórias
1. `franquia/FATOS_FRANQUIA.md`: **única** fonte de fatos, benefícios e proibições.
2. `franquia/PAUTA.md`: tema do dia pela data.
3. `franquia/kit/`: render.py (post), reels.py + reels.html (Reels), base.css, arcos.js, logo Franquia oficial.
4. `PUBLICACAO.md` (raiz): protocolo de publicação com verificação e até 3 tentativas, **trocando o
   account pelo da Franquia** (ver "Conta").
5. `ROTINA.md` e `ROTINA_1230.md` (raiz): mesmas regras visuais, de QA e de Reels da marca-mãe.
6. Instruções do projeto "GABRIEL - DIRETOR CRIATIVO" e Base Mestre: identidade, densidade, anti-clichê, QA.

## Conta (OBRIGATÓRIO antes de publicar)
Windsor.ai `get_connectors`: procure no connector `instagram` a conta cujo nome contém `santoseportela.franquia`.
- Encontrou: use o `id` dela em todas as chamadas (execute_action e get_data). **Nunca** publique no
  account `17841467778795999` (é a @_santoseportelalicitacoes).
- Não encontrou: crie a peça normalmente, faça commit/push, registre no histórico `status: "aguardando_conta"`
  e envie PushNotification começando com "NÃO PUBLICADO: conta @santoseportela.franquia ainda não conectada
  ao Windsor.ai", com o link raw do arquivo e a legenda pronta. Encerre.

## Regras fixas de formato
- Post: 1080×1350 (4:5), JPEG qualidade 90. (A API do Instagram não aceita 3:4.)
- **Fundo sempre claro** (`body.claro`) até existir `franquia/kit/logos/logo_franquia_fundo_escuro.png` oficial.
  O render bloqueia fundo escuro. **Nunca recolorir a logo.**
- Arcos (`data-arcos`): coluna | canto | diagonal | s | trio | ancora. Não repetir a composição dos últimos 3 posts.
  Como o fundo é sempre claro, a variedade vem da composição, do mecanismo e do tamanho da headline.
- Sem barras, filetes, ícones, listas, caixas, selos, telas simuladas ou CTA na arte.
- Texto: headline (2ª parte em itálico dourado com `<em>`) + no máximo 1 subheadline. Carrossel: até 25 palavras por slide.
- Logo: só o PNG oficial Franquia, aplicado pelo render (post) ou pelo card final (Reels). Nunca escrever o nome da marca como logo.
- Fonte provisória: TeX Gyre Pagella até chegar a The Seasons.

## Pilares (girar; não repetir o pilar do dia anterior no mesmo formato)
1. Oportunidade (o governo compra de todo segmento, todos os dias).
2. Do especialista ao dono (virada de carreira do consultor/analista).
3. Resultados da marca (números, trajetória, certificações da seção 1 dos FATOS).
4. Estrutura e suporte (jurídico, comercial, marketing, apoio operacional, operacional terceirizado).
5. Tecnologia própria (central de licitações: gestão de clientes, CRM, financeiro, radar, envio automatizado de oportunidades, gestão de documentos, auditoria, tarefas). Nunca robô de lance nem monitoramento de chat enquanto bloqueados.
6. Leads e crescimento na região (leads qualificados da região, leads para prospecção, tráfego pago).
7. Perfil e processo transparente (para quem é, para quem não é, COF).
8. Vantagens extras (desconto na Santos & Portela Contabilidade).

## A. Post de feed (rotina da manhã)
1. Clonar o repositório. Ler `franquia/posts/historico.json`. Se já houver entrada de hoje com status `publicado`, parar.
2. Tema: linha de hoje na `PAUTA.md`. Se for ⚠, já usado ou vencido, escolher tema novo pelos pilares.
3. Processo Gabriel: tese → 5 conceitos → filtro de clichê (inclusive de franquia: chave, dinheiro, carro, praia, foguete) → headline.
4. Estático: `franquia/posts/AAAA-MM-DD_slug.html` com `<link rel="stylesheet" href="../kit/base.css">` e
   `<script src="../kit/arcos.js">`. Renderizar: `python3 franquia/kit/render.py franquia/posts/X.html /tmp/X.png claro`,
   converter para JPEG 90 em `franquia/posts/X.jpg` e **abrir a imagem para conferir**.
   Carrossel: pasta `franquia/posts/AAAA-MM-DD_slug/` com um HTML por slide (`../../kit/...`), 5 a 8 slides, cada um renderizado e conferido.
5. QA da Base Mestre + estes itens: sem promessa de ganho; sem dado de franquia não informado; números só da seção 1 dos FATOS, como resultado da marca.
6. Legenda: gancho, 2–4 frases, CTA "A próxima unidade começa com uma conversa. Chame no direct ou toque no link da bio." e 3–5 hashtags (ex.: #franquia #licitacoes #santoseportela #franquiadeservicos #mercadopublico).
7. Registrar em `franquia/posts/historico.json` (data, arquivo(s), formato, headline, pilar, persona, mecanismo, composicao, legenda, status), commit/push.
8. Conta (seção "Conta"). Aguardar ~60 s e publicar pelo Windsor.ai: `create_image_post` (estático) ou
   `create_carousel_post` (carrossel, `image_urls` na ordem) com URLs
   `https://raw.githubusercontent.com/santoseportela-posts/santoseportela-posts/main/franquia/posts/...`.
   Seguir o `PUBLICACAO.md` com o account da Franquia (verificação + até 3 tentativas). Nunca publicar duas vezes.
9. Atualizar o histórico (publicado / falhou + motivo, media_id), commit/push, mensagem curta ao cliente
   (SendUserMessage + SendUserFile) com a headline, a imagem e o resultado.

## B. Reels (rotina da noite)
1. Clonar. Ler `franquia/reels/historico.json`. Se já houver Reels de hoje `publicado`, parar.
2. Tema: coluna Reels da `PAUTA.md` de hoje (ou tema novo pelos pilares). Não repetir o tema do post da manhã;
   complementar quando fizer sentido.
3. Roteiro `franquia/reels/AAAA-MM-DD_slug.json` no formato do `kit/reels.py`: 2 cenas de 4,5–5 s + final
   (2,6 s, logo Franquia e @santoseportela.franquia). Cena 1 com kicker curto ("Você sabia?", "Para quem
   trabalha com licitação", "Franqueado Santos & Portela"). Cada cena: até 4 linhas curtas + 1 linha em `em`.
   `fundo: "claro"`.
4. Quadros de conferência: `python3 franquia/kit/reels.py roteiro.json /tmp/stills --stills 1,4,7,11` e **olhar**.
   Vídeo: `python3 franquia/kit/reels.py roteiro.json franquia/reels/AAAA-MM-DD_slug.mp4`.
5. Legenda: gancho, 2–3 frases, CTA da Franquia e 3–5 hashtags.
6. Registrar em `franquia/reels/historico.json`, commit/push, conta (seção "Conta"), aguardar ~60 s e publicar com
   `create_video_post` (`video_url` raw do MP4, `share_to_feed: true`, `caption`), seguindo o `PUBLICACAO.md`.
7. Atualizar histórico, commit/push e mensagem curta ao cliente com o tema, a legenda e o resultado.
