/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let init_copy = init;
    return {
        increment : 
            function(){
                return init +=1;
            }
        ,
        decrement: 
            function(){
                return init -=1;
            }
        ,
        reset: function(){
            init = init_copy;
            return init;}
            }

    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */