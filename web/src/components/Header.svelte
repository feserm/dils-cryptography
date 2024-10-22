<script lang="ts">
    import { token } from "../stores/app";

    function logout() {
        localStorage.removeItem('token');
        $token = '';
    }
</script>

<header class="z-10">
	<nav class="bg-gradient-to-r from-primary to-accent text-[oklch(var(--nc))] p-2">
		<div class="containe</nav>r flex items-center justify-between min-w-full">
			<!-- Logo container -->
			<div class="">
				<div class="text-xl font-bold">Cryptography</div>
			</div>
			<!-- Navigation container -->
			<div class="flex justify-end mr-4">
				<button class="btn btn-secondary btn-sm" on:click={logout}>Logout</button>
			</div>
		</div>
	</nav>
</header>