// copy.config.js

const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  plugins: [
    new CopyPlugin([
      { from: 'assets/images/favicon.ico', to: '' },
      { from: 'assets/**', to: '' },
    ]),
  ],
}
