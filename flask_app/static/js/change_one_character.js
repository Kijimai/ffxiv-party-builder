const changeUserForm = document.getElementById("change_user_form")

//Search for characters then change
changeUserForm.addEventListener("submit", (e) => {
  e.preventDefault()
  console.log("submitted!")
  const charName = e.target[0].value
  const serverName = e.target[1].value
  console.log(charName, serverName)
  fetchCharacter(charName, serverName)
})

async function fetchCharacter(characterName, serverName = "") {
  const foundCharacters = await fetch(
    `https://xivapi.com/character/search?name=${characterName}&server=${serverName}`
  )
    .then((res) => res.json())
    .then((data) => data.Results)
    .catch((err) => console.log(err))

  console.log(foundCharacters)
}

function renderCharactersForChange(list) {
  
}