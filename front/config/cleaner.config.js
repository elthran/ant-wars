// cleaner.config.js

const { CleanWebpackPlugin } = require('clean-webpack-plugin')

const watching = process.env.npm_lifecycle_event === 'watch'
// only clean stale assets when "--watch" flag not set.
// This fixes a bug where my assets don't exist after "watch" rebuilds.
module.exports = {
  // plugins
  plugins: [
    new CleanWebpackPlugin(
      { cleanStaleWebpackAssets: !watching }
    )
  ],
}
