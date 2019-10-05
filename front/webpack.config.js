// This library allows us to combine paths easily
const path = require('path');

module.exports = {
  entry: path.resolve(__dirname, 'src', 'main.js'),
  output: {
    path: path.resolve(__dirname, '../output'),
    filename: 'bundle.js'
  },
  resolve: {
    extensions: ['.js', '.vue']
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },
      {
        test: /\.js$/,
        use: {
          loader: 'babel-loader',
          options: { presets: ['react', 'es2015'] }
        }
      },
      {
        test: /\.scss$/,
        use: ['style-loader', 'css-loader', 'sass-loader']
      }
    ]
  }
};
