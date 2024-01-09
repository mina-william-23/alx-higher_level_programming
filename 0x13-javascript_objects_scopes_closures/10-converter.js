#!/usr/bin/node
exports.converter = function (base) {
  const wrapper = function (num) {
    return num.toString(base);
  };
  return wrapper;
};
