(function(){

    const btn = document.querySelectorAll('.editar-producto')

    btn.forEach((btn) => {
        btn.addEventListener('click',function(){
            confirmaredicion();
        })
    })


    const confirmaredicion=async()=>{
        await fetch('http://127.0.0.1:5000/editarProducto',{
            method='POST',
            mode:'same-origin',
            headers:{
                'Content-Type':'application/json',
                'X-CSRF-TOKEN':''
            }
        })
    };

})();


