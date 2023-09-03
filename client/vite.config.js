import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: 'localhost',
    port: '8080',
    proxy: {
      '/api': {
        target: 'http://localhost:3000', 
        changeOrigin: true, 
        ws: true, // 支持 websocket
        rewrite: (path) => path.replace(/^\/api/, '/api') // 路径重写
      }
    }
  }
})
