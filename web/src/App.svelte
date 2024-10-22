<script lang="ts">
  import { onMount } from "svelte";
  import "./app.css";
  import { token } from "./stores/app";
    import Login from "./components/Login.svelte";
    import Home from "./components/Home.svelte";

  onMount(async () => {
    try {
      let tmp = localStorage.getItem("token");
      if (tmp) {
        $token = tmp;
      }
    } catch (error) {
      console.error(error);
    }
  });
</script>

<main>
  {#if $token}
  <Home/>
  {:else}
  <Login/>
  {/if}
</main>
