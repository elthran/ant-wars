// html.config.js

const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  plugins: [
    // plugins customize the webpack build process in a variety of ways
    new HtmlWebpackPlugin({
      template: '!!raw-loader!pug-plain-loader?pretty=true!./static/index.pug',
    }),
  ],
}
