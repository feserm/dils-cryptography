import { readable, writable } from "svelte/store";

export const token = writable("");

export const api = readable({base_url: 'http://localhost:3030'})