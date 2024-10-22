<script lang="ts">
    export let activeTab = 0;
</script>

<div role="tablist" class="tabs tabs-boxed">
    <button role="tab" class="tab" on:click={()=>{activeTab=0}} class:tab-active={activeTab===0}>Caesar</button>
    <button role="tab" class="tab" on:click={()=>{activeTab=1}} class:tab-active={activeTab===1}>Atbash</button>
    <button role="tab" class="tab" on:click={()=>{activeTab=2}} class:tab-active={activeTab===2}>Vigenere</button>
</div>