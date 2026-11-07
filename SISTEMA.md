# Pilar 7: Tecnologia própria (sistema Santos & Portela)

Pedido do cliente em 07/11/2026: mostrar as ferramentas e tecnologias que a Santos & Portela
desenvolve e usa em **sistema próprio** para trazer mais segurança e assertividade aos clientes.
Fonte: roteiro do sistema (repositório `sistema-licitacoes`, docs/roteiro.md), só etapas **publicadas**.

## Regra de intercalação
- Post das 8h: **alternar um a um** com os pilares 1 a 6 do ROTINA.md. Se o último post das 8h em
  `posts/historico.json` não for do pilar 7, hoje é pilar 7; se foi, hoje é um dos pilares 1 a 6.
- Registrar no histórico `"pilar": "7. Tecnologia própria: <funcionalidade>"`.
- Uma funcionalidade por post. Não repetir funcionalidade dos últimos 6 posts do pilar 7.
- Alternar entre os dois lados: **Painel do cliente** e **Painel do escritório**.

## Banco de funcionalidades (só estas; nada além do que está escrito)

### A. Painel do cliente: sessão Oportunidades
1. **Radar nacional próprio:** busca diária de licitações no PNCP e no Compras.gov.br, filtrada pelo
   perfil de cada cliente (grupos de palavras-chave, desejadas e indesejadas, portal, esfera, cidade,
   registro de preço) com pontuação de aderência e opção de ocultar o que não serve.
2. **Envio automático ao cliente:** de segunda a sexta, às 7h e às 14h, as oportunidades selecionadas
   chegam ao painel do cliente ("Licitações selecionadas pelo escritório para a sua empresa").
3. **Decisão em um clique:** para cada oportunidade o cliente escolhe participar, pedir análise ou
   descartar (com justificativa, que melhora as próximas seleções).
4. **Prazo de resposta calculado:** o sistema define o prazo de decisão 2 dias antes da abertura,
   antecipando fim de semana e feriado. Nada fica para a última hora.
5. **Participar com precisão:** ao confirmar, o cliente informa valor mínimo e marca/modelo (ou o
   serviço) item a item; o escritório é avisado na hora (painel e e-mail).
6. **Quadro de acompanhamento:** cada licitação percorre as fases aguardando abertura, em disputa,
   habilitação, recurso, ganha, homologada ou perdida, com totais, taxa de êxito e valor homologado
   da própria empresa.
7. **Resumo executivo por oportunidade:** card com detalhes, arquivos, itens e dados do edital, e
   perguntas do cliente ao escritório pelo próprio painel.

### B. Painel do escritório (especialistas)
1. **Analista de Editais com IA:** os documentos do edital são baixados do PNCP e analisados em um
   formulário padronizado de 19 campos (prazos, valor estimado, portal, garantia, amostra, atestados,
   pagamento, documentos fora do padrão). Regra: nada inventado; o que não está no edital é sinalizado.
2. **Pasta de habilitação por cliente:** certidões (federal, FGTS, trabalhista, estadual, municipal,
   falência), contrato social, balanço, atestados e outros, com validade controlada, **arquivos
   criptografados** e histórico de versões.
3. **Alertas de vencimento:** avisos com 10, 5 e 2 dias e no dia do vencimento, no painel e por e-mail,
   para o documento ser renovado antes de qualquer sessão.
4. **Checklist de habilitação por licitação:** cruza o que o edital exige com os documentos válidos
   **na data da sessão**; pasta exportável só com o exigido no edital.
5. **Proposta de preços montada pelo sistema:** usa o modelo do próprio edital quando existe (ou o
   modelo do escritório), itens conforme o Termo de Referência, preço, marca e modelo do cliente, total
   e valor por extenso, em Word ou PDF.
6. **Visão consolidada:** a equipe acompanha todas as oportunidades e fases de todos os clientes, com
   filtro por cliente, e permissões de acesso da equipe por cliente e por área.

## Fora dos posts (proibido mencionar)
- Financeiro (inteiro: mensalidades, comissões, cartões, lançamentos) e CRM.
- Robô de lances, monitoramento de chat do Compras.gov.br, envio de proposta pelo painel, empenhos/atas
  e agenda (em teste, pausados ou não publicados).
- Cliente modelo/demonstração e qualquer número do sistema (taxa de êxito, quantidades). Números só os
  oficiais da Seção 1 do projeto.
- Nomes técnicos, endereços, telas, prints ou dados de clientes. **Não desenhar nem simular telas do
  sistema:** a arte segue o ROTINA.md (headline + até 1 subheadline + arcos + logo oficial).

## Como escrever
- Tese sempre no benefício do empresário: segurança, prazo, assertividade, menos improviso. A
  tecnologia é o meio; a assessoria (especialistas) continua sendo o guia.
- Pode dizer "sistema próprio", "tecnologia própria", "desenvolvido pela Santos & Portela".
- Não prometer vitória, prazo garantido ou "risco zero".
- Exemplos de ângulo (não copiar literalmente): certidão vencida descoberta na véspera × alerta 10 dias
  antes; ler edital de 200 páginas × formulário de 19 campos; decidir no escuro × decidir com prazo.
