# Exercício 04 - Página de Vendas com Vue.js

📅 **Entrega:** 21/09/2025 até às 23h59  
📚 Baseado nas aulas 1 e 2 do curso de Vue.js.

---

## 📌 Descrição
O objetivo deste exercício foi criar uma página HTML utilizando as diretivas do Vue.js para implementar uma página de vendas com carrinho de compras.

---

## 🛠️ Funcionalidades

### Diretivas Vue.js Utilizadas
- **v-if**: Exibe mensagem condicionalmente
- **v-show**: Mostra/oculta opção de pagamento baseado no carrinho
- **v-for**: Lista produtos e itens do carrinho
- **v-on** (@click): Adiciona itens ao carrinho e remove itens
- **v-bind** (:key, :class): Vincula dados e classes dinamicamente

### Funcionalidades da Página
- Exibição de produtos com valores
- Botões para adicionar itens ao carrinho
- Carrinho de compras dinâmico
- Opção de pagamento que só aparece quando há itens no carrinho
- Cálculo automático do total
- Formas de pagamento: Cartão de Crédito, Débito, PIX, Boleto

---

## 🚀 Como executar

1. Abra o arquivo `index.html` em um navegador moderno
2. Ou use um servidor local:
```bash
# Com Python
python -m http.server 8000

# Com Node.js
npx serve
```

3. Acesse: http://localhost:8000

---

## 📝 Observações
- Utiliza Vue.js 3 via CDN
- A opção de pagamento só é exibida quando o carrinho possui itens (usando v-show)
- Todos os produtos podem ser adicionados ao carrinho
- É possível remover itens do carrinho
- O total é calculado automaticamente

---

## 🎯 Requisitos Atendidos
✅ Página HTML com diretivas Vue.js  
✅ v-if, v-show, v-for, v-on, v-bind implementados  
✅ Página de vendas com produtos e valores  
✅ Botões para adicionar itens no carrinho  
✅ Opção de pagamento exibida somente se houver itens no carrinho

