(function () {
    const btnElimnacion=document.querySelectorAll(".btnEliminacion");

btnElimnacion.forEach(btn =>{
    btn.addEventListener('click', (e) =>{
            const confirmacion=confirm('¿Estas seguro de borrar el siguiente curso?');
            if (!confirmacion){
                e. preventDefault();
            }
        });
    });
})();