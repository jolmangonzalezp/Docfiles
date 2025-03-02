const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
});

const path = require('path')

module.exports = {
  outputDir: path.resolve(__dirname, '../backend/static'),
  devServer: {
    proxy: 'http://127.0.0.1:5000' // Redirige peticiones API a Flask
  }
}
