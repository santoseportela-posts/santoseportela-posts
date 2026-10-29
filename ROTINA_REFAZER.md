# Rotina diária das 17h: refazer um post antigo do Instagram

Todo dia, perto das 17h (horário de Brasília), um post antigo do @_santoseportelalicitacoes é refeito
no padrão visual atual e publicado de novo. **Publicação automática, sem aprovação**, autorizada pelo
cliente em 29/10/2026. A rotina das 8h (ROTINA.md) continua publicando posts novos.

A API do Instagram não permite excluir posts. **Nunca tente apagar ou arquivar nada.**
O cliente arquiva o post antigo pelo app; a rotina só informa qual é.

## Fila
`refazer/fila.json`: posts antigos em ordem cronológica (mais antigo primeiro).
- `pendente`: a refazer · `refeito`: já republicado · `pular`: não refazer (o motivo está no item).
- `agendado`: refazer só no dia `data_alvo` (datas comemorativas). Nesse dia ele tem prioridade sobre a fila.
- `aguardando_confirmacao`: NÃO publicar até o cliente confirmar nesta conversa (o item diz o porquê).
- Leia sempre o campo `observacao` do item: ele traz instruções específicas
  (ex.: carrossel → `create_carousel_post`; Reels → imagem única; anúncio de cliente autorizado a citar o nome).
- O cliente pediu (29/10/2026) para refazer TODOS os posts, inclusive anúncios de clientes.

## Passo a passo
1. Se já existir item com `status: "refeito"` e `data_refeito` igual a hoje, pare (1 por dia).
2. Se houver item `agendado` com `data_alvo` igual a hoje, use-o. Senão, pegue o primeiro `pendente`.
   Leia `legenda_original` e `observacao` e extraia a **tese**.
   Se a tese for igual à de um item já refeito (posts duplicados), marque `pular` com motivo
   "duplicado de <media_id>" e pegue o próximo.
3. Recrie a peça seguindo TODAS as regras de formato, verdade e QA do ROTINA.md e da Base Mestre:
   - mesma ideia central, headline reescrita no padrão Gabriel (curta, forte, para o empresário);
   - **corrija a verdade**: remova números não oficiais, promessas de resultado, garantias,
     "devolvemos seu dinheiro", urgência falsa. Use só os fatos da Seção 1 das instruções do projeto;
   - sem logo de cliente; nome de cliente só nos anúncios de cliente, e só como estava no original;
     sem barras, ícones, listas ou CTA na arte;
   - fundo e composição de arcos diferentes do post das 8h de hoje e dos últimos 3 em `posts/historico.json`.
4. Arquivos em `refazer/AAAA-MM-DD_slug.html` e `.jpg` (1080×1350, JPEG 90). Abra a imagem e confira.
5. Legenda nova: gancho, 2–4 frases, CTA "O próximo contrato começa com uma conversa. Fale com nosso
   time: (11) 93624-7039." e 3–5 hashtags. Não copie a legenda antiga.
6. Commit/push para `main`, aguarde ~60 s e publique com Windsor.ai: connector `instagram`,
   action `create_image_post`, account `17841467778795999`, `image_url` =
   `https://raw.githubusercontent.com/santoseportela-posts/santoseportela-posts/main/refazer/<arquivo>.jpg`.
7. No item da fila: `status: "refeito"`, `data_refeito`, `novo_media_id`, `nova_headline`, `arquivo`.
   Acrescente também uma entrada em `posts/historico.json` com `"rotina": "17h-refazer"`. Commit/push.
8. Mensagem ao cliente (SendUserMessage + SendUserFile): headline nova, resultado da publicação e
   **o link do post antigo para arquivar** (`permalink` do item), com a instrução:
   "No app: abra o post → ⋯ → Arquivar."
