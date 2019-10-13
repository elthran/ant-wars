// webpack.config.js
const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  mode: 'development',
  entry: './src/index.js', // default entry point
  output: {
    path: path.join(__dirname, 'dist'), // default path
    filename: '[name].bundle.js', // default filename
  },
  module: {
    // configuration regarding modules
    rules: [
      // rules for modules (configure loaders, parser options, etc.)
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },
      // this will apply to both plain `.js` files
      // AND `<script>` blocks in `.vue` files
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.pug$/,
        oneOf: [
          // this applies to `<template lang="pug">` in Vue components
          {
            resourceQuery: /^\?vue/,
            use: ['pug-plain-loader'],
          },
          // this applies to pug imports inside JavaScript
          {
            use: ['raw-loader', 'pug-plain-loader'],
          },
        ],
      },
      // this will apply to both plain `.css` files
      // AND `<style>` blocks in `.vue` files
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader',
        ]
      },
      // this will apply to both plain `.scss` files
      // AND `<style lang="scss">` blocks in `.vue` files
      {
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'sass-loader',
        ],
      },
      // this will apply to both plain `.sass` files
      // AND `<style lang="sass">` blocks in `.vue` files
      {
        test: /\.sass$/,
        use: [
          'vue-style-loader',
          'css-loader',
          {
            loader: 'sass-loader',
            options: {
              indentedSyntax: true,
              // sass-loader version >= 8
              sassOptions: {
                indentedSyntax: true,
              },
            },
          },
        ],
      },
    ],
  },
  resolve: {
    alias: {
      "@": path.join(__dirname, 'src'),
    },
    // file types to load
    extensions: ['.sass', '.vue', '.js', '.json'],
  },
  plugins: [
    // plugins customize the webpack build process in a variety of ways
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: '!!raw-loader!pug-plain-loader?pretty=true!./static/index.pug',
      minimize: false,
    }),
    new VueLoaderPlugin(),
  ],
}
