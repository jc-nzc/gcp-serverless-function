function primNum(num){
  var primObj = [];
  for (var i = 0; i <=num; i++) {
    var outComes = i
    if( outComes === 2){
      primObj.push(outComes)
    }
    if ( outComes % 2 === 1){
      primObj.push(outComes)
    }
  }
  return primObj;
}

console.log(primNum(10));
