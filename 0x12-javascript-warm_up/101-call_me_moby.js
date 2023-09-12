#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  //while (x--) {
    //theFunction();
  //}
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
