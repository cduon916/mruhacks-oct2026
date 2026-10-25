let breakLoop = false;
let aVariable = 20;
let playerChar;
let enemyChar;
let playerCharCurrentHealth;
let enemyCharCurrentHealth;

document.addEventListener('DOMContentLoaded',  () => {
    document.addEventListener("click", fight);
    parseTheCharacters();

    function fight(e) {
        if(e.target.id == "fightBtn") {

            playerCharCurrentHealth = playerChar.Health;
            enemyCharCurrentHealth = enemyChar.Health;
            let isYourTurn = flipACoin()

            //Primary Loop!
            let loopID = setInterval(() => {
                console.log("Skibidi "+aVariable)

                if(isYourTurn) {
                    playerAttacks(e)
                    isYourTurn = !isYourTurn;
                } else {
                    enemyAttacks(e);
                    isYourTurn = !isYourTurn;
                }
                

                //enemyAttackLands(e);
                if(playerCharCurrentHealth < 1) enemyWins();
                if(enemyCharCurrentHealth < 1) playerWins();

                if(playerCharCurrentHealth < 1 || enemyCharCurrentHealth < 1) breakLoop = true;
                if(breakLoop) clearInterval(loopID);
            }, 1000);


        }
    }

    function enemyWins() {
        const playerCharObj = document.getElementById('playerChar');
        playerCharObj.classList.add("dead");
    }

    function playerWins() {
        const enemyCharObj = document.getElementById('enemyChar');
        enemyCharObj.classList.add("dead");
    }



    function playerAttacks(e) {
        if(flipACoin()) {
            let attackImpact = calculateAttackEffectiveness();
            let damage = playerChar.AttackDamage * attackImpact;
            console.log("Hit for "+damage+" damage!");
            enemyCharCurrentHealth = enemyCharCurrentHealth - damage;
            playerAttackLands(e, damage);
        } else {
            playerAttackFails(e);
        }
    }

    function enemyAttacks(e) {
        if(flipACoin()) {
            let attackImpact = calculateAttackEffectiveness();
            let damage = enemyChar.AttackDamage * attackImpact;
            console.log("Hit for "+damage+" damage!");
            playerCharCurrentHealth = playerCharCurrentHealth - damage;
            enemyAttackLands(e, damage);
        } else {
            enemyAttackFails(e);
        }
    }



    function playerAttackLands(e, damage) {
        console.log("Ouch!")
            const playerCharObj = document.getElementById('playerChar');
            const enemyCharObj = document.getElementById('enemyChar');
            playerCharObj.classList.add("attackingL");
            enemyCharObj.classList.add("ouchie")
            const enemyHealthbar = document.getElementById("rightHealthbar");
            console.log("Enemy max health is "+enemyChar.Health);
            console.log("Enemy health percent: "+(100*(enemyCharCurrentHealth/enemyChar.Health)));
            enemyHealthbar.style.width = ""+(100*(enemyCharCurrentHealth/enemyChar.Health))+"%";
            setTimeout(() => {
                playerCharObj.classList.remove("attackingL");
                enemyCharObj.classList.remove("ouchie")
            }, 100);
    }

    function playerAttackFails(e) {
        console.log("Dodge!")
            const playerCharObj = document.getElementById('playerChar');
            const enemyCharObj = document.getElementById('enemyChar');
            playerCharObj.classList.add("attackingL");
            enemyCharObj.classList.add("dodge")
            setTimeout(() => {
                playerCharObj.classList.remove("attackingL");
                enemyCharObj.classList.remove("dodge")
            }, 100);
    }

    function enemyAttackLands(e, damage) {
        console.log("Ouch!")
            const playerCharObj = document.getElementById('playerChar');
            const enemyCharObj = document.getElementById('enemyChar');
            enemyCharObj.classList.add("attackingR");
            playerCharObj.classList.add("ouchie")
            const enemyHealthbar = document.getElementById("leftHealthbar");
            enemyHealthbar.style.width = ""+(100*(playerCharCurrentHealth/playerChar.Health))+"%";
            setTimeout(() => {
                playerCharObj.classList.remove("ouchie");
                enemyCharObj.classList.remove("attackingR")
            }, 100);
    }

    function enemyAttackFails(e) {
        console.log("Dodge!")
            const playerCharObj = document.getElementById('playerChar');
            const enemyCharObj = document.getElementById('enemyChar');
            enemyCharObj.classList.add("attackingR");
            playerCharObj.classList.add("dodge")
            setTimeout(() => {
                enemyCharObj.classList.remove("attackingR");
                playerCharObj.classList.remove("dodge")
            }, 100);
    }


    function flipACoin() {
        let raw = Math.random()
        return raw > 0.5 ? true:false;
    }

    function calculateAttackEffectiveness() {
        return (Math.random() * (1.5));
    }
})


async function parseTheCharacters() {
    //const playerChar = await fetch(PLAYER_DATA);
    //const enemyChar = await fetch(ENEMY_DATA);
    playerChar = PLAYER_DATA;
    enemyChar = ENEMY_DATA;

    console.log("You have chosen "+playerChar.Name+" with attack "+playerChar.Attack);
    console.log("And you are fighting "+enemyChar.Name+" with attack "+enemyChar.Attack);

    const playerImage = document.querySelector('#playerChar img');
    const enemyImage = document.querySelector('#enemyChar img');
    playerImage.src = `/static/character_pictures/${playerChar.Name}.png`;
    enemyImage.src = `/static/character_pictures/${enemyChar.Name}.png`;
}