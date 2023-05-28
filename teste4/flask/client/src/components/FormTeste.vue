<template>
    <div class="container mt-5">
  <form @submit="pesquisar_operadoras">
  <div class="form-group">
    <label for="exampleFormControlInput1">Pesquisa: (texto, logradouro, cnpj, etc)</label>
    <input type="text" class="form-control" v-model="valor_parecido" placeholder="Exemplo: Unimed">
  </div>
  <div class="form-group">
    <label for="exampleFormControlSelect1">Pesquisar por:</label>
    <select class="form-control" v-model="campo">
      <option>registro_ans</option>
      <option>cnpj</option>
      <option>razao_social</option>
      <option>nome_fantasia</option>
      <option>modalidade</option>
      <option>logradouro</option>
      <option>numero</option>
      <option>complemento</option>
      <option>bairro</option>
      <option>cidade</option>
      <option>uf</option>
      <option>cep</option>
      <option>ddd</option>
      <option>telefone</option>
      <option>fax</option>
      <option>endereco_eletronico</option>
      <option>representante</option>
      <option>cargo_representante</option>
      <option>data_registro_ans</option>
    </select>
  </div>
  <button type="submit" class="btn btn-secondary mb-2" style="margin: 20px;">Pesquisar</button>
</form>
<div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5" role="alert">
<strong>{{error}}</strong>
</div> 
</div>

</template>

<script>

export default {
    data(){
      return {
        error: null,
        valor_parecido: null,
        campo: null
        
      }
    },
    methods: {
      pesquisar_operadoras() {
          
               
            if((this.valor_parecido == null || this.campo == null || this.valor_parecido == '')) {
              this.error = " Por favor escolha um critério de pesquisa"
            } else {
              this.$router.push({name:'OperadorasResultado', params: {campo: this.campo, valor_parecido: this.valor_parecido}})  
            } 

      }
    }
}
</script>

<style>

</style>