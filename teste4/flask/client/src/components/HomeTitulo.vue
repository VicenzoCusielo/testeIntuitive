<template>
  <nav class="navbar navbar-expand-lg bg-primary">
  <div class="container">
    <router-link class="navbar-brand text-style" to="/">Teste usando Flask e Vue 3</router-link>     
     <ul class="navbar-nav">
        <li class="nav-item" style="padding-right:20px;">
          <router-link class="btn btn-primary" aria-current="page" to="/">Home</router-link>
        </li>
      </ul>
  </div>
</nav>
</template>

<script>
export default {

}
</script>

<style>
.text-style {
    font-size: 35px !important; 
    font-family: 'sans-serif' !important;
    color: white !important;

}
</style>