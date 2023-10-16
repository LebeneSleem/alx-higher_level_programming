#!/usr/bin/node
function printArgs () {
  let Args = 0;
  for (let i = 2; i < process.argv.length; i++) {
    Args++;
  }

  if (Args === 0) {
    console.log('No argument');
  } else if (process.argv[2]) {
    console.log(process.argv[2]);
  }
}
printArgs();
