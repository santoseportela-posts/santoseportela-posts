# Protocolo de publicação à prova de falhas (vale para TODAS as rotinas)

Criado em 04/11/2026, a pedido do cliente, depois que o Reels das 12h30 não foi ao ar:
o Windsor.ai expirou (timeout de 180 s) sem publicar, e a rotina parou sem tentar de novo.
**Regra do cliente: o post do dia tem que ir ao ar.** Timeout ou erro NÃO é motivo para desistir.
Este protocolo substitui qualquer instrução "se falhar, tentar 1 vez" ou "não contornar" das outras
rotinas, **somente no que diz respeito a repetir a publicação pela mesma ferramenta**. Continua
proibido usar outros meios (outra API, navegador, outro conector).

## Antes de publicar
1. Arquivo commitado e enviado para `main`: confirme com `git fetch origin main && git ls-tree origin/main <caminho>`.
2. Aguarde pelo menos 60 s depois do push (o raw.githubusercontent.com tem cache). Um `curl` com 403 dentro
   do ambiente é bloqueio do proxy local, não do GitHub: não é motivo para parar.
3. Verifique se já não há post de hoje no histórico (status `publicado` com a data de hoje). Se houver, pare.

## Publicar (até 3 tentativas)
Para cada tentativa N (1, 2, 3):
1. Chame `execute_action` (Windsor.ai, connector `instagram`, account `17841467778795999`).
2. **Sucesso** = a resposta traz `Media id`. Registre o `media_id` e siga para "Depois de publicar".
3. **Erro ou timeout sem media_id:**
   a. Registre a tentativa no histórico na hora (`status: "tentando"`, `tentativas: N`, motivo) e faça commit/push.
   b. Aguarde ~3 min (vários `sleep 100`; cada comando de shell tem limite de 2 min).
   c. Verifique se o post entrou: `get_data` connector `instagram`, accounts `["17841467778795999"]`,
      fields `["media_id","media_caption","media_type","media_permalink"]`, `date_preset: "last_1dT"`
      (sem `force_refresh`: o plano gratuito não aceita). Procure um post cuja legenda comece igual
      à legenda enviada (primeiros ~80 caracteres).
   d. Se encontrar → é o post de hoje: registre o `media_id`, NÃO publique de novo.
   e. Se não encontrar → nova tentativa. Em 04/11 a 1ª tentativa com timeout NÃO publicou, e a 2ª,
      com os mesmos parâmetros, publicou na hora. Então "ausente no get_data" = tentar de novo.
4. Entre a 2ª e a 3ª tentativa, aguarde ~5 min.
5. Ao reenviar, use exatamente os mesmos parâmetros (mesmo arquivo, mesma legenda), para que um
   eventual duplicado seja fácil de identificar e arquivar.

## Depois de publicar
- Histórico: `status: "publicado"`, `media_id`, `tentativas: N` e, se houve falha antes, `observacao`.
- Commit/push e mensagem ao cliente (SendUserMessage + SendUserFile).
- Se precisou de mais de uma tentativa, diga isso na mensagem em uma linha, e diga também que, se
  aparecer um post duplicado, basta arquivar um deles no app (⋯ → Arquivar).

## Se as 3 tentativas falharem
- Histórico: `status: "falhou"`, com o motivo de cada tentativa. Commit/push.
- **PushNotification imediata** (é o que chega ao celular do cliente), começando com
  "NÃO PUBLICADO:", com o tema, o erro e o link raw do arquivo, para publicação manual.
- Mensagem ao cliente (SendUserMessage + SendUserFile) com a legenda pronta para copiar.
- Se o erro for de permissão ou de conta desconectada no Windsor.ai, diga isso explicitamente
  (reconectar a conta resolve; a rotina não consegue reconectar sozinha).
