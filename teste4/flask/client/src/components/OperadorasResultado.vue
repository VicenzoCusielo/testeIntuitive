<template>
    
    <div class="container mt-5"><ol>
        <div v-if="!operadoras.length">Nenhum resultado</div>
      <div v-for="operadora in operadoras" :key="operadora[0]"><li>
        <h3>Registro ANS: {{operadora[0]}}</h3>
        <h4>CNPJ: {{operadora[1]}}</h4>
        <p>Razão Social: {{operadora[2]}}
        Nome Fantasia: {{operadora[3]}} 
        Modalidade: {{operadora[4] }} 
        Logradouro: {{operadora[5] }} 
        Número: {{operadora[6] }} 
        Complemento: {{operadora[7] }} 
        Bairro: {{operadora[8] }} 
        Cidade: {{operadora[9] }} 
        UF: {{operadora[10] }} 
        CEP: {{operadora[11] }} 
        DDD: {{operadora[12] }} 
        Telefone: {{operadora[13] }}
        Fax: {{operadora[14] }} 
        Endereço de e-mail: {{operadora[15] }} 
        Representante: {{operadora[16] }} 
        Cargo do representante: {{operadora[17] }} 
        Data de registro: {{operadora[18] }} </p>
      </li>
      </div>
    </ol>
    </div></template>

<script>
export default {
                
         data(){
            return {
                    campo: this.$route.params.campo,
                    valor_parecido: this.$route.params.valor_parecido,
                    operadoras:[],
                 }
            },

        

            methods: {
                    pesquisar_operadoras(){
                                 console.log(  );
                                 console.log(  );
                        fetch('http://localhost:5000/pesquisar_operadoras/'+this.$route.params.campo+'/'+this.$route.params.valor_parecido+'/',{
                        method:"GET",
                        headers: {
                        "Content-Type": "application/json"
                            }
                             })
                             .then(resp => resp.json())
                             .then(data => {
                                    this.operadoras.push(...data)
                                        })
                                    .catch(error => {
                                    console.log(error)
                                   })
    
                          }



            },
            created() {
        
                this.pesquisar_operadoras()

            }


 }

</script>

<style>

</style>