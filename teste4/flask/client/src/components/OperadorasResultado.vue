<template>
    
    <div class="container mt-5"><ol>
        <div v-if="!operadoras.length">Nenhum resultado</div>
      <div v-for="operadora in operadoras" :key="operadora[0]"><li>
        <h3>Registro ANS: {{operadora[1]}}</h3>
        <h4>CNPJ: {{operadora[2]}}</h4>
        <p>Razão Social: {{operadora[3]}}
        Nome Fantasia: {{operadora[4]}} 
        Modalidade: {{operadora[5] }} 
        Logradouro: {{operadora[6] }} 
        Número: {{operadora[7] }} 
        Complemento: {{operadora[8] }} 
        Bairro: {{operadora[9] }} 
        Cidade: {{operadora[10] }} 
        UF: {{operadora[11] }} 
        CEP: {{operadora[12] }} 
        DDD: {{operadora[13] }} 
        Telefone: {{operadora[14] }}
        Fax: {{operadora[15] }} 
        Endereço de e-mail: {{operadora[16] }} 
        Representante: {{operadora[17] }} 
        Cargo do representante: {{operadora18 }} 
        Data de registro: {{operadora[19] }} </p>
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