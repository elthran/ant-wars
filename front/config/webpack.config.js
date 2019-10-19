// webpack.config.js

const path = require('path')
const merge = require('webpack-merge')

const babelConfig = require('./babel.config.js')
const cleanerConfig = require('./cleaner.config.js')
const copyConfig = require('./copy.config.js')
const fileConfig = require('./file.config.js')
const htmlConfig = require('./html.config.js')
const vueConfig = require('./vue.config.js')

const basePath = path.normalize(path.join(__dirname, '..', '..'))

const baseConfig = {
  mode: 'development',
  entry: './src/index.js', // default entry point
  output: {
    path: path.join(basePath, 'app', 'dist'), // default path
    filename: '[name].bundle.js', // default filename
  },
  module: {
    // configuration regarding modules
    rules: [
      // rules for modules (configure loaders, parser options, etc.)
    ],
  },
  resolve: {
    alias: {
      '@': path.join(process.env.PWD, 'src'),
    },
    // file types to load
    extensions: ['.js', '.json'],
  },
  plugins: [
    // plugins customize the webpack build process in a variety of ways
  ],
  watchOptions: {
    ignored: /node_modules/,
  },
}

module.exports = merge(
  baseConfig,
  cleanerConfig,
  copyConfig,
  fileConfig,
  htmlConfig,
  babelConfig,
  vueConfig
)
