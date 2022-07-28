const mathfunc = require('readline').createInterface({
    input: process.stderr,
    output: process.stdout
})



mathfunc.question('Enter operation text ', answer => {
    console.log(eval(answer));
    mathfunc.close()
})

