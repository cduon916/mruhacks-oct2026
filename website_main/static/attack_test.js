let breakLoop = false;
let aVariable = 20;
let playerChar;
let enemyChar;
let playerCharCurrentHealth;
let enemyCharCurrentHealth;

document.addEventListener('DOMContentLoaded',  () => {
    document.addEventListener("click", doohickey);
    parseTheCharacters();

    function doohickey(e) {
        if(e.target.id == "fightBtn") {

            logEvent("Your character, "+playerChar.Name+" is facing off against "+enemyChar.Name+"!", false);

            playerCharCurrentHealth = playerChar.Health;
            enemyCharCurrentHealth = playerChar.Health;
            let isYourTurn = flipACoin()
            
            if(playerCharCurrentHealth < 1 || enemyCharCurrentHealth < 1) return;

            //Primary Loop!
            let loopID = setInterval(() => {
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
        const enemyHealthbar = document.getElementById("leftHealthbar");
        enemyHealthbar.hidden = true;
        logEvent(enemyChar.Name+" has won!!", false);
        playerCharObj.classList.add("dead");
    }

    function playerWins() {
        const enemyCharObj = document.getElementById('enemyChar');
        const playerHealthbar = document.getElementById("rightHealthbar");
        playerHealthbar.hidden = true;
        logEvent("Your character, "+playerChar.Name+" has won!!", true);
        enemyCharObj.classList.add("dead");
    }



    function playerAttacks(e) {
        if(flipACoin()) {
            let attackImpact = calculateAttackEffectiveness();
            let damage = playerChar.AttackDamage * attackImpact;
            enemyCharCurrentHealth = enemyCharCurrentHealth - damage;
            logEvent(playerChar.Name+"'s "+playerChar.Attack+" hit "+enemyChar.Name+" for "+Math.floor(damage)+" damage!", true);
            playerAttackLands(e, damage);
        } else {
            logEvent(playerChar.Name+" used "+playerChar.Attack+", but "+enemyChar.Name+" dodged!", true);
            playerAttackFails(e);
        }
    }

    function enemyAttacks(e) {
        if(flipACoin()) {
            let attackImpact = calculateAttackEffectiveness();
            let damage = enemyChar.AttackDamage * attackImpact;
            playerCharCurrentHealth = playerCharCurrentHealth - damage;
            logEvent(enemyChar.Name+"'s "+enemyChar.Attack+" hit "+playerChar.Name+" for "+Math.floor(damage)+" damage!", false);
            enemyAttackLands(e, damage);
        } else {
            logEvent(enemyChar.Name+" used "+enemyChar.Attack+", but "+playerChar.Name+" dodged!", false);
            enemyAttackFails(e);
        }
    }



    function playerAttackLands(e, damage) {
        const playerCharObj = document.getElementById('playerChar');
        const enemyCharObj = document.getElementById('enemyChar');
        playerCharObj.classList.add("attackingL");
        enemyCharObj.classList.add("ouchie")
        const enemyHealthbar = document.getElementById("rightHealthbar");
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
    console.log("Hiiii")
    const response = await fetch(JSON_URL);
    const data = await response.json();

    const characterList = data.characters;

    let myCharacterName = "Harry Potter";
    playerChar = characterList.find(chara => chara.Name === myCharacterName);

    const randomIndex = Math.floor(Math.random() * characterList.length);
    enemyChar = characterList[randomIndex];

    console.log("You have chosen "+playerChar.Name+" with attack "+playerChar.Attack);
    console.log("And you are fighting "+enemyChar.Name+" with attack "+enemyChar.Attack);

    const playerImage = document.querySelector('#playerChar img');
    const enemyImage = document.querySelector('#enemyChar img');
    playerImage.src = `/static/character_pictures/${playerChar.Name}.png`;
    enemyImage.src = `/static/character_pictures/${enemyChar.Name}.png`;
}

function logEvent(str, isPlayerAction) {
    console.log(str);
    const template = document.querySelector("#tempItem");
    const clone = template.content.cloneNode(true);
    clone.querySelector(".item-text").textContent = str;
    if(isPlayerAction) clone.querySelector(".item-text").classList.add("yourActions");
    document.querySelector("#battleLog").appendChild(clone);
}