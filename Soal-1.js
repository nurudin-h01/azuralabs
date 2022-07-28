let store = [['Indomie', 3000, 5, 150], ['Laptop', 4000000, 4.5, 123], ['Aqua', 3000, 4, 250], ['Smart TV', 4000000, 4.5, 42], ['Headphone', 4000000, 3.5, 90], ['Very Smart TV', 4000000, 3.5, 87]]

function sortarray(a,b){
    if(a[1] === b[1]){
        if(a[2] === b[2]){
            if(a[3] === b[3]){
                return 0
            } else {
                return (a[3] > b[3] ? -1 :1 )
            }
        } else {
            return (a[2] > b[2] ? -1 :1 )
        }
    } else {
        return (a[1] < b[1] ? -1 :1 )
    }
}

store.sort(sortarray)
console.log(store)
