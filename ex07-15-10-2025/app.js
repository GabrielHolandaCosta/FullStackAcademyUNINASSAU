new Vue({
  el: '#app',
  data: {
    titulo: 'Projeto de Interpolação e Diretivas - Vue.js',
    nome: 'Gabriel Holanda',
    curso: 'Ciência da Computação',
    ano: 2025,
    exibirMensagem: true,
    mostrarTexto: true,
    linguagens: ['JavaScript', 'Python', 'C++', 'Vue.js'],
    imagem: 'https://vuejs.org/images/logo.png',
    descricaoImagem: 'Logo do Vue.js',
    mensagemBotao: 'Clique no botão acima para alterar esta mensagem!'
  },
  methods: {
    mudarMensagem() {
      this.mensagemBotao = 'Mensagem alterada com sucesso! 🎉';
    }
  }
});
