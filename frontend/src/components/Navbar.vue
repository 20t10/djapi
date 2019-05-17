<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light c-navbar">
        <div class="container">
                            <router-link
                    :to="{ name: 'home' }"
                    class="navbar-brand"
                >Mini Panti
                </router-link>
     

            <div class="collapse navbar-collapse" >
            <ul class="navbar-nav ml-auto">
            <li class="nav-item  mx-1">
                <router-link
                    :to="{ name: 'question-editor' }"
                    class="nav-link"
                >Add Topic
                </router-link>
            
            </li>
            <li class="nav-item mx-1">

                <router-link
                    :to="{ name: 'about' }"
                    class="nav-link"
                >About
                </router-link>

            </li>
            <li class="nav-item mx-1">
                <router-link
                    :to="{ name: 'example' }"
                    class="nav-link"
                >Example
                </router-link>

            </li>
            <li class="nav-item">
            <a class="btn btn-secondary" href="/accounts/logout/" tabindex="-1" >Logout</a>
            </li>
            </ul>

            </div>
     </div>
</nav>
</template>

<script>
export default {
    name: "NavbarComponent"
    
}
</script>

<style>
    .c-navbar{
        border-bottom: 1px #DDD;

    }

</style>
