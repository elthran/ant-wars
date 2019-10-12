const path = require('path');

module.exports = {
  mode: 'development',
  entry: './src/index.js', // default entry point
  output: {
    path: path.join(__dirname, 'dist'), // default path
    filename: './main.js', // default filename
  }
}
