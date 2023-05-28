<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Operadoras</h1>
        <hr><br><br>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Registro Ans</th>
              <th scope="col">CNPJ</th>
              <th scope="col">Razão Social</th>
              <th scope="col">Nome Fantasia</th>
              <th scope="col">Modalidade</th>
              <th scope="col">Logradouro</th>
              <th scope="col">Número</th>
              <th scope="col">Complemento</th>
              <th scope="col">Bairro</th>
              <th scope="col">Cidade</th>
              <th scope="col">UF</th>
              <th scope="col">Cep</th>
              <th scope="col">DDD</th>
              <th scope="col">Telefone</th>
              <th scope="col">Fax</th>
              <th scope="col">Endereço Eletrônico</th>
              <th scope="col">Representante</th>
              <th scope="col">Cargo Representante</th>
              <th scope="col">Data Registro Ans</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(rs, index) in todas_operadoras" :key="index">
              <td>{{ rs[0] }}</td>
              <td>{{ rs[1] }}</td>
              <td>{{ rs[2] }}</td>
              <td>{{ rs[3] }}</td>
              <td>{{ rs[4] }}</td>
              <td>{{ rs[5] }}</td>
              <td>{{ rs[6] }}</td>
              <td>{{ rs[7] }}</td>
              <td>{{ rs[8] }}</td>
              <td>{{ rs[9] }}</td>
              <td>{{ rs[10] }}</td>
              <td>{{ rs[11] }}</td>
              <td>{{ rs[12] }}</td>
              <td>{{ rs[13] }}</td>
              <td>{{ rs[14] }}</td>
              <td>{{ rs[15] }}</td>
              <td>{{ rs[16] }}</td>
              <td>{{ rs[17] }}</td>
              <td>{{ rs[18] }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
 
<script>
 
export default {

  data(){
    return {
      todas_operadoras:[],
    }
  },

  methods: {
    getTodasOperadoras(){
      fetch('http://localhost:5000/pegar_todas_operadoras',{
          method:"GET",
          headers: {
            "Content-Type": "application/json"
          }
      })
      .then(resp => resp.json())
      .then(data => {
      this.todas_operadoras.push(...data)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created(){
    console.log('teste');
    this.getTodasOperadoras()
  }
}
</script>