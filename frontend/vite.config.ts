import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import path from 'path'
import tailwindcss from '@tailwindcss/vite'

import { fileURLToPath } from 'url';
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    port: 9973,           
    host: true,  
    watch: {
      usePolling: true,      // включаем polling
      interval: 500          // интервал проверки в мс
    },         
  },
    resolve: {
    alias: {
      src: path.resolve(__dirname, 'src')
    }
  }
})
