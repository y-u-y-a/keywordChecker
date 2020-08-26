// 分割代入(配列やオブジェクトの中身を順番に取り出す)
const { PROJECT_NAME, API_URL } = process.env;

export default {
  /*
  ** Nuxt rendering mode
  ** See https://nuxtjs.org/api/configuration-mode
  */
  mode: 'universal',
  srcDir: 'src/', // 追加

  /*
  ** Nuxt target
  ** See https://nuxtjs.org/api/configuration-target
  */
  target: 'server',
  /*
  ** Headers of the page
  ** See https://nuxtjs.org/api/configuration-head
  */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Global CSS
  */
  css: [
    './src/assets/sass/app.scss'
  ],
  /*
  ** Plugins to load before mounting the App
  ** https://nuxtjs.org/guide/plugins
  */
  plugins: [
  ],
  /*
  ** Auto import components
  ** See https://nuxtjs.org/api/configuration-components
  */
  components: true,

  buildModules: [
  ],

  modules: [
    ['bootstrap-vue/nuxt', {css: false}],
    '@nuxtjs/axios',
    '@nuxtjs/dotenv'
  ],
  env: {
    PROJECT_NAME,
    API_URL
  },

  // 参照：https://axios.nuxtjs.org/options
  axios: {
    proxy: true
  },

  // key名の先頭にvalue部分が追加される(例：'/api/v2/items')
  proxy: {
    '/api/': process.env.API_URL
  },

  build: {
  }
}
