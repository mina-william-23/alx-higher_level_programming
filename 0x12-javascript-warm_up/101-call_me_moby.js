#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
  //for (let i = 0; i < x; i++) {
    //theFunction();
  //}
};
