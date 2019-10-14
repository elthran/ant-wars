// cleaner.config.js

const { CleanWebpackPlugin } = require('clean-webpack-plugin')

module.exports = {
  plugins: [
    // plugins customize the webpack build process in a variety of ways
    new CleanWebpackPlugin(),
  ],
}
