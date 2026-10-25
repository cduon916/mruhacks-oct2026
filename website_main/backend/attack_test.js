let breakLoop = false;
let aVariable = 20;

document.addEventListener('DOMContentLoaded',  () => {
    document.addEventListener("click", doohickey);

    function doohickey(e) {
        if(e.target.id == "fightBtn") {
            let loopID = setInterval(() => {
                console.log("Skibidi "+aVariable)
                aVariable--;

                playerAttackLands(e);
                enemyAttackLands(e);

                if(aVariable<1) breakLoop = true;
                if(breakLoop) clearInterval(loopID);
            }, 1000);


        }
    }



    function playerAttackLands(e) {
        console.log("Ouch!")
            const playerChar = document.getElementById('playerChar');
            playerChar.classList.add("attacking");
            enemyChar.classList.add("ouchie")
            setTimeout(() => {
                playerChar.classList.remove("attackingL");
                enemyChar.classList.remove("ouchie")
            }, 100);
    }

    function playerAttackFails(e) {
        console.log("Dodge!")
            const playerChar = document.getElementById('playerChar');
            playerChar.classList.add("attacking");
            enemyChar.classList.add("dodge")
            setTimeout(() => {
                playerChar.classList.remove("attackingL");
                enemyChar.classList.remove("dodge")
            }, 100);
    }
})
