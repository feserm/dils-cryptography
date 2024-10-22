<script lang="ts">
    import { api, token } from "../stores/app";
    import Header from "./Header.svelte";
    import Tabs from "./Tabs.svelte";

    let activeTab = 0, encoded = "", decoded = "";

    async function encode() {
        let alg;
        if (activeTab === 0) {
            alg = "caesar";
        } else if (activeTab === 1) {
            alg = "atbash";
        } else if (activeTab === 2) {
            alg = "vigenere";
            encoded = encoded.toUpperCase().replaceAll(' ', '');
        }

        if (alg) {
            const response = await fetch(`${$api.base_url}/api/v1/${alg}/encode`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${$token}`,
                },
                body: JSON.stringify({ message: encoded }),
            });
            if (response.ok) {
                decoded = await response.text();
                encoded = "";   
            }
        }
    }

    async function decode() {
        let alg;
        if (activeTab === 0) {
            alg = "caesar";
        } else if (activeTab === 1) {
            alg = "atbash";
        } else if (activeTab === 2) {
            alg = "vigenere";
        }

        if (alg) {
            const response = await fetch(`${$api.base_url}/api/v1/${alg}/decode`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${$token}`,
                },
                body: JSON.stringify({ message: decoded }),
            });
            if (response.ok) {
                encoded = await response.text();
                decoded = "";
            }
        }    }
</script>

<Header />

<Tabs bind:activeTab/>
<div class="flex flex-row w-11/12 mx-auto space-x-1 mt-4">
    <textarea class="p-2 border border-neutral w-full" rows="10" placeholder="Decoded Text Here" bind:value={encoded}></textarea>
    <div class="flex flex-col space-y-2 my-auto mx-auto w-1/6">
        <button class="btn btn-neutral btn-sm" on:click={encode}>Encode {">>"}</button>
        <button class="btn btn-neutral btn-sm" on:click={decode}>{"<<"} Decode</button>
    </div>
    <textarea class="p-2 border border-neutral w-full" rows="10" placeholder="Encoded Text Here" bind:value={decoded}></textarea>
</div>