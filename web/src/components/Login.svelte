<script lang="ts">
    import { api, token } from "../stores/app";

    let username = '', password = '', register_state = false;

    async function login() {
        const response = await fetch(`${$api.base_url}/aai/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('token', data.access_token);
            $token = data.access_token;
        } else {
            alert('Login failed');
        }
    }

    async function register() {
        const response = await fetch(`${$api.base_url}/aai/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            alert('Registration successful');
            register_state = false;
        } else {
            alert('Registration failed');
        }
    }
</script>

<div
	class="hero min-h-screen bg-neutral bg-cover bg-center"
>
	<div class="hero-content flex-col lg:flex-row-reverse">
		<div class="text-center lg:text-left text-white">
			<h1 class="text-5xl font-bold">Cryptography</h1>
			<p class="py-6">DILS Seminar WiSe24/25</p>
		</div>
        <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100 p-4 space-y-2">
            {#if register_state}
            <h1 class="text-2xl font-semibold flex justify-center">Register</h1>
            <input type="text" class="input input-bordered" placeholder="Username" bind:value={username} />
            <input type="password" class="input input-bordered" placeholder="Password" bind:value={password} />
            <button class="btn btn-accent" on:click={register}>Register</button>
            <div class="flex justify-end">
                <button class="link" on:click={()=>{register_state=false}}>Login</button>
            </div>
            {:else}
            <h1 class="text-2xl font-semibold flex justify-center">Login</h1>
            <input type="text" class="input input-bordered" placeholder="Username" bind:value={username} />
            <input type="password" class="input input-bordered" placeholder="Password" bind:value={password} />
            <button class="btn btn-accent" on:click={login}>Login</button>
            <div class="flex justify-end">
                <button class="link" on:click={()=>{register_state=true}}>Register</button>
            </div>
            {/if}
        </div>
        </div>
</div>