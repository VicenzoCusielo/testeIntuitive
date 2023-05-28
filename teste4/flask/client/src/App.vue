<template>
 <div id="App">
    <HomeTitulo/>
    <FormTeste/>
  <router-view/>
  
  </div>
</template>

<script>
import HomeTitulo from './components/HomeTitulo.vue'
import FormTeste from './components/FormTeste.vue'

export default {
  name: 'App',
  components: {
    HomeTitulo,
    FormTeste
}
}
</script>

<style>


</style>