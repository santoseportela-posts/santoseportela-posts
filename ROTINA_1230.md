# Rotina das 12h30: terceiro post (complementar)

Roda de segunda a sexta, perto das 12h30 (horário de Brasília). **Publicação automática, sem aprovação**
(autorizada pelo cliente em 02/11/2026, que aprovou o Reels de teste). Fim de semana: não publicar.

- **Segunda, quarta, sexta → Reels "Curiosidades da Santos & Portela"** (vídeo 9:16, 10–14 s).
- **Terça, quinta → Carrossel educativo sobre licitações** (5–7 slides 4:5).

O formato muda de propósito: os posts das 8h e das 17h são imagens únicas. Não repetir aqui o tema
nem a headline do post das 8h do mesmo dia; quando fizer sentido, **complementar** o tema do dia.

## Já aprovado: quarta-feira 04/11/2026
Neste dia NÃO crie um Reels novo: publique o vídeo já aprovado pelo cliente,
`reels/2026-11-04_campos-alphaville.mp4` (roteiro no .json ao lado), com esta legenda:

"Tudo começou em 2009, em Campos dos Goytacazes, no interior do Rio. Uma convicção guiava a gente: empresas competentes perdiam contratos públicos por falta de método, não de capacidade.

Em agosto de 2026, inauguramos a nova matriz em Alphaville, perto do maior volume de licitações do país. Campos e Vitória seguem ativas como filiais.

Do interior do Rio para o centro do mercado público brasileiro.

O próximo contrato começa com uma conversa. Fale com nosso time: (11) 93624-7039.

#santoseportela #licitacoes #mercadopublico #alphaville #curiosidades"

## Reels: curiosidades da Santos & Portela
Ferramentas: `kit/reels.py` + `kit/reels.html` (modelo: `reels/2026-11-04_campos-alphaville.json`).
1. Escolha UMA curiosidade do banco abaixo que ainda não esteja em `reels/historico.json`.
   Só fatos do banco ou da Seção 1 das instruções do projeto. Nada inventado.
2. Roteiro: 1 ou 2 cenas (4,5–5 s cada) + final com logo (2,6 s). Cena 1 começa com o kicker
   "Você sabia?". Cada cena: até 4 linhas curtas + 1 linha em itálico dourado (`em`).
   Não escreva "Santos & Portela" como texto de destaque (use "nós", "nascemos", "nossa equipe").
3. Alternar `fundo` escuro/claro em relação ao último Reels.
4. Gerar quadros de conferência (`--stills`) e **olhar**: texto cortado, sobreposição com os arcos,
   ortografia. Depois o vídeo completo: `python3 kit/reels.py roteiro.json reels/AAAA-MM-DD_slug.mp4`.
5. Commit/push, aguardar ~60 s e publicar seguindo o **PUBLICACAO.md** (verificação + até 3 tentativas): Windsor.ai, connector `instagram`, action `create_video_post`,
   account `17841467778795999`, `video_url` = raw.githubusercontent.com do MP4, `share_to_feed: true`, `caption`.
6. Registrar em `reels/historico.json` (data, curiosidade, fundo, media_id, status). Commit/push.

### Banco de curiosidades (fatos oficiais)
- Nascemos em 2009 em Campos dos Goytacazes, no interior do Rio.
- A primeira filial, em Vitória/ES, cresceu tanto que foi a matriz por três anos.
- Em agosto de 2026 inauguramos a nova matriz em Alphaville/SP, perto do maior volume de licitações do país.
- Crescer nunca significou ir embora: Campos e Vitória seguem como filiais; Belo Horizonte tem um escritório franqueado.
- Também estamos do outro lado do balcão: já treinamos e assessoramos 123 órgãos públicos.
- 36 clientes estão conosco há mais de 10 anos: 31% da carteira.
- Somos certificados ISO 9001 (gestão da qualidade) e ISO 27001 (segurança da informação), pela SGS.
- Participamos do Pacto Brasil pela Integridade Empresarial, da CGU, e temos o Selo Empresa Limpa.
- Temos o selo RA1000 do Reclame Aqui.
- Nosso fundador, Paulo Portela, é presidente da ABPL.
- Usamos Inteligência Artificial na análise de editais, preços e concorrentes.
- Cada cliente tem um Key Account dedicado, do primeiro edital à gestão do contrato.
- 28 mil+ processos disputados em 17 anos.
- Cada oportunidade chega ao cliente em um resumo executivo de uma página.
- Do interior do Rio para o centro do mercado público brasileiro (frase-assinatura; bom para fechar uma série).
Quando o banco acabar, recomeçar com outra abordagem visual/texto do mesmo fato.

## Carrossel educativo
Ferramentas: `kit/render.py` (um HTML por slide, como em `posts/2026-11-02_novo-site/`).
1. Tema prático sobre licitações para empresários, sem repetir `carrosseis/historico.json`. Exemplos:
   documentos que mais eliminam empresas na habilitação; como ler um edital com método; etapas de um pregão
   eletrônico; o que é impugnação e quando usar; erros de preço que custam contrato; como escolher
   em quais licitações entrar; gestão do contrato depois da vitória; o que é o PNCP e como usar.
2. **Informação legal precisa**: tudo sobre a Lei 14.133/2021, prazos, modalidades e procedimentos deve ser
   conferido com WebSearch em fonte oficial (planalto.gov.br, gov.br) antes de publicar. Na dúvida, generalize
   ou corte. Nunca citar artigo, prazo ou valor sem conferir.
3. Slide 1: gancho forte (headline + `em`). Slides do meio: 1 ideia por slide, até 25 palavras.
   Último slide: "O próximo contrato começa com uma conversa." + `em` santoseportela.com.br.
   Mesmo visual de sempre (fundos do site, arcos, logo pelo render.py, sem barras/ícones/listas).
4. Conferir cada slide renderizado. Publicar (seguindo o **PUBLICACAO.md**) com `create_carousel_post` (2 a 10 `image_urls`, na ordem).
5. Registrar em `carrosseis/historico.json`. Commit/push.

## Legenda (ambos)
Gancho, 2–4 frases, CTA "O próximo contrato começa com uma conversa. Fale com nosso time: (11) 93624-7039."
e 3–5 hashtags. Mensagem final ao cliente com o resultado (e o arquivo).
