import { defineConfig } from 'astro/config';
import alpinejs from '@astrojs/alpinejs';
import path from 'path';

// https://astro.build/config
export default defineConfig({
  integrations: [alpinejs()],
  vite: {
    resolve: {
      alias: {
        '@app': path.resolve('./src/app'),
      }
    }
  }
});
