# Petshop Amigo Fiel — Fase 2

Projeto acadêmico da disciplina de Fundamentos de Sistemas Web, desenvolvido por Rafael Achtenberg.

## Objetivo

Continuar o sistema web iniciado na Fase 1 e torná-lo mais atrativo, responsivo, acessível e dinâmico por meio de CSS, Bootstrap e JavaScript. A Fase 2 também permite simular o cadastro do responsável e do pet e o agendamento dos serviços de banho ou tosa.

## Metas

- preservar as informações de produtos e serviços desenvolvidas na Fase 1;
- aplicar um layout responsivo com Bootstrap e CSS próprio;
- apresentar destaques em um carrossel;
- reunir os dados do responsável e do pet em um formulário;
- permitir a escolha do serviço, modalidade, data e horário;
- validar os dados no navegador e apresentar um resumo da simulação;
- ampliar a acessibilidade da navegação, das imagens e do formulário;
- publicar a nova fase no mesmo repositório e no GitHub Pages.

## Tecnologias utilizadas

- HTML5;
- CSS3;
- Bootstrap 5.3.8 pelo CDN oficial;
- JavaScript puro.

Não são utilizados frameworks JavaScript, gerenciadores de pacotes, servidor, API ou banco de dados.

## Estrutura

```text
fase-2-petshop/
├── index.html
├── produtos.html
├── servicos.html
├── agendamento.html
├── README.md
├── css/
│   └── estilos.css
├── js/
│   └── script.js
└── imagens/
    ├── brinquedo-corda.webp
    ├── cama-cachorro.webp
    ├── fraldas-pets.png
    ├── racao-caes.png
    ├── racao-gatos.webp
    └── tapete-higienico.webp
```

## Páginas

- `index.html`: apresentação, carrossel e atalhos para as áreas do site;
- `produtos.html`: três categorias com dois produtos em cada uma;
- `servicos.html`: banho e tosa, valores e modalidades;
- `agendamento.html`: cadastro do cliente, cadastro do pet e simulação do agendamento.

## Produtos e categorias

O catálogo possui exatamente dois produtos em cada categoria:

- **Acessórios:** brinquedo de corda e cama para cachorro;
- **Rações não perecíveis:** ração para cães e ração para gatos;
- **Higiene e limpeza:** tapete higiênico e fraldas descartáveis para pets.

Cada produto apresenta imagem, nome, descrição e valor.

## Serviços

- **Banho:** R$ 55,00 com entrega no local ou R$ 75,00 com tele-busca;
- **Tosa:** R$ 70,00 com entrega no local ou R$ 90,00 com tele-busca.

Todos os serviços exigem agendamento. Na modalidade tele-busca, o endereço informado no cadastro é utilizado como referência para buscar e devolver o pet.

## Cadastro e agendamento

O formulário solicita dados de identificação e contato do cliente, endereço, sexo e preferências de contato. Para o pet, solicita nome, espécie, raça, idade, porte e observações.

O responsável escolhe banho ou tosa, tele-busca ou entrega no local, uma data e um horário. O formulário usa campos de texto, número, e-mail, telefone, data, hora, radio buttons, checkboxes, selects e textarea.

## Funções JavaScript

O arquivo `js/script.js`:

- exibe a data e a hora atuais;
- configura a data mínima como o dia atual;
- impede datas passadas e domingos;
- verifica horários do expediente;
- informa como funciona a modalidade escolhida;
- utiliza a validação nativa do formulário;
- impede o envio real;
- apresenta um resumo do agendamento com segurança por meio de `textContent`;
- permite pausar ou retomar o carrossel.

Depois de uma simulação válida, o formulário é preservado para que os dados possam ser revisados. Nada é salvo no navegador.

## Acessibilidade

- idioma `pt-BR` e títulos de página descritivos;
- elementos semânticos como `header`, `nav`, `main`, `section` e `footer`;
- um título principal `h1` por página;
- textos alternativos descritivos;
- link “Pular para o conteúdo principal”;
- labels associados aos campos;
- agrupamento de opções com `fieldset` e `legend`;
- mensagens dinâmicas com `aria-live`;
- foco visível e navegação por teclado;
- contraste entre texto e fundo;
- controle para pausar o carrossel;
- respeito à preferência por movimento reduzido;
- erros informados por texto, sem depender somente de cor.

## Ajustes realizados na Fase 2

1. A estrutura original foi copiada para uma pasta independente, mantendo a Fase 1 intacta.
2. O layout foi reorganizado com navbar, grid, cards, botões, formulário e rodapé do Bootstrap.
3. Um arquivo CSS próprio definiu a identidade visual e os ajustes responsivos.
4. A página inicial recebeu um carrossel com três imagens autorizadas, indicadores, controles e pausa.
5. Foi criado o formulário de cadastro do cliente e do pet.
6. Foram incluídas as escolhas de banho ou tosa, tele-busca ou entrega no local, data e horário.
7. O JavaScript passou a validar datas e horários e a apresentar mensagens dinâmicas.
8. O resumo da simulação informa os dados principais sem enviar ou armazenar informações.
9. A acessibilidade foi ampliada com textos alternativos, labels, fieldsets, link de salto, foco visível e regiões ao vivo.
10. O código foi dividido em arquivos de HTML, CSS e JavaScript e recebeu comentários apenas nas decisões menos evidentes.
11. Os testes corrigiram restrições de datas, horários de sábado, domingos e preferências de movimento.

## Limitações da demonstração

- o formulário não envia, registra ou persiste dados;
- o agendamento não representa uma reserva real;
- não existe autenticação, pagamento, carrinho, banco de dados ou integração com sistemas externos;
- preços, endereço, telefone e e-mail são fictícios e usados somente para fins acadêmicos;
- a disponibilidade final dependeria da confirmação do petshop.

## Imagens

As seis imagens de produtos foram fornecidas pelo aluno e reaproveitadas da Fase 1. Nenhuma imagem adicional foi baixada ou gerada para esta fase.

## Como executar

1. Baixe ou clone o repositório.
2. Abra `fase-2-petshop/index.html` em um navegador conectado à internet, pois o Bootstrap é carregado por CDN.
3. Navegue pelas páginas e utilize o formulário apenas com dados fictícios.

## Links

- [Código-fonte no GitHub](https://github.com/Faelkk/estudos-faculdade/tree/master/fundamentos-de-sistemas-web/fase-2-petshop)
- [Site no GitHub Pages](https://faelkk.github.io/estudos-faculdade/fundamentos-de-sistemas-web/fase-2-petshop/)

## Autor

Rafael Achtenberg — 2026.
