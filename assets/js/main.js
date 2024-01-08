/*
 * Main Javascript file for guard_tower.
 *
 * This file bundles all of your javascript together using webpack.
 */

// JavaScript modules

require.context(
  "../img", // context folder
  true, // include subdirectories
  /.*/, // RegExp
);

// Your own code
require("./plugins");
require("./script");
require("../css/style.css")
