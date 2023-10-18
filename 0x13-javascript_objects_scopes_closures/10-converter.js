#!/usr/bin/node
exports.converter = function (base) {
  function convertToBase (n) {
    return n.toString();
  }

  return convertToBase;
};
